from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import resolve_url
from movies.models import BasePersonModel


class Author(BasePersonModel):
    def get_absolute_url(self):
        return resolve_url('author_detail', pk=self.pk)


class Book(models.Model):
    LANGUAGE_ENG = 'eng'
    LANGUAGE_CZ = 'cz'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENG, 'english'),
        (LANGUAGE_CZ, 'czech'),
    )

    GENRE_1 = 'drama'
    GENRE_2 = 'komedia'
    GENRE_3 = 'thriller'
    GENRE_4 = 'romance'
    GENRE_5 = 'naucne'

    GENRE_CHOICES = (
        (GENRE_1, 'drama'),
        (GENRE_2, 'komedia'),
        (GENRE_3, 'thriller'),
        (GENRE_4, 'romance'),
        (GENRE_5, 'naucne'),
    )


    name = models.CharField(max_length=256)
    description = models.TextField()
    rating = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(100)
    ])
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    genres = models.CharField(choices=GENRE_CHOICES, max_length=10)
    released = models.DateField()
    authors = models.ForeignKey(
        'Author',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True, blank=True,
    )
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} : {self.id}'

    def get_absolute_url(self):
        return resolve_url('book_detail', pk=self.id)


class Contact(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    subject = models.TextField()
    phone_number = models.IntegerField()
    contact_at = models.DateField()