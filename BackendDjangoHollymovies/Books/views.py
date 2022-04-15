from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView

from Books.forms import ContactForm, BookForm, AuthorForm
from Books.models import Book, Author, Contact
from django.views import View


class HomepageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_books': Book.objects.all().count(),
            'number_of_authors': Author.objects.all().count(),
            'page_name': 'Homepage'
        }
        return TemplateResponse(request, 'homepage.html', context=context)


# def homepage_view(request):
#     if request.method == 'GET':
#         context = {
#             'number_of_books': Book.objects.all().count(),
#             'number_of_actors': Actor.objects.all().count(),
#             'page_name': 'Homepage'
#         }
#         return TemplateResponse(request, 'homepage.html', context=context)
#     elif request.method == 'POST':
#         return HttpResponse(request, 'method not allowed')


class BooksDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(BooksDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'authors.html'
    extra_context = {'page_name': 'Authors'}


class AuthorDetailView(BooksDetailView):
    model = Author
    template_name = 'author_detail.html'


class BookListView(ListView):
    queryset = Book.objects.all().order_by('-rating')
    template_name = 'books.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BookListView, self).get_context_data(*args, **kwargs)
        context.update({
            'best_books': Book.objects.filter(rating__gte=80).order_by('-rating'),
            'worst_books': Book.objects.filter(rating__lte=20).order_by('rating'),
            'page_name': 'Books',
        })
        return context


class BookDetailView(BooksDetailView):
    model = Book
    template_name = 'book_detail.html'

    def post(self, request, pk, *args, **kwargs):
        book = self.get_object()
        book.likes += 1
        book.save(update_fields=['likes', ])
        return redirect('book_detail', pk=pk)

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        phone_number = form.cleaned_data.get('phone_number')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        contact_at = form.cleaned_data.get('contact_at')

        Contact.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            subject=subject,
            contact_at=contact_at
        )
        return TemplateResponse(self.request, 'contact.html', context={'form': ContactForm()})

    def form_invalid(self, form):
        return TemplateResponse(self.request, 'contact.html', context={'form': form})


class CreateBookView(CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book


class CreateAuthorView(CreateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author


class UpdateBookView(UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book


class UpdateAuthorView(UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author


class DeleteBookView(DeleteView):
    template_name = 'book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('books')


class DeleteAuthorView(DeleteView):
    template_name = 'author_confirm_delete.html'
    model = Author
    success_url = reverse_lazy('authors')