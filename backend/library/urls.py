from django.urls import path
from .views import get_authors, get_books, get_borrows, export_excel

urlpatterns = [
    path("authors/", get_authors),
    path("books/", get_books),
    path("borrows/", get_borrows),
    path("export/", export_excel),
]
