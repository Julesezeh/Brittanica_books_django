from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

# Create your views here.


@api_view(("GET",))
def all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)
