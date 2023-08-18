from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework.views import APIView

# Create your views here.


@api_view(("GET",))
def all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)


class AuthorViews(APIView):
    def get(self, reuquest):
        all = Author.objects.all()
        serializer = AuthorSerializer(all)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        try:
            serializer = AuthorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                with Exception as e:
                    return Response(e)
        except Exception as e:
            return Response(e)
