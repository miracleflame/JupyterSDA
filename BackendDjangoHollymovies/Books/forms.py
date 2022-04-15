from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from Books.models import Book, Author


class DatePickerDateInput(forms.DateInput):
    def __init__(self, *args, **kwargs):
        kwargs.update({'attrs': {'type': 'date'}})
        super(DatePickerDateInput, self).__init__(*args, **kwargs)


class DateFieldSevenDaysFromNow(forms.DateField):
    widget = DatePickerDateInput

    def validate(self, value):
        super(DateFieldSevenDaysFromNow, self).validate(value)
        if value < timezone.now().date() + timedelta(days=7):
            raise ValidationError('Cannot create contact at earlier that 7 days from now')


def contact_name_is_not_david(value):
    if 'david' in value.lower():
        raise ValidationError('David cannot create contact')


class ContactForm(forms.Form):
    name = forms.CharField(validators=[contact_name_is_not_david, ])
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea)
    phone_number = forms.IntegerField()
    age = forms.IntegerField(min_value=1, max_value=99)
    contact_at = DateFieldSevenDaysFromNow()
    subscribe = forms.BooleanField()

    def clean_name(self):
        return self.data.get('name').lower()


class BookForm(forms.ModelForm):
    released = forms.DateField(widget=DatePickerDateInput())

    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['likes', ]



class AuthorForm(forms.ModelForm):
    born_at = forms.DateField(widget=DatePickerDateInput())
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = '__all__'

    def save(self, commit=True):
        author = super(AuthorForm, self).save(commit=commit)
        author.books.add(*self.cleaned_data.get('books'))
        return author
