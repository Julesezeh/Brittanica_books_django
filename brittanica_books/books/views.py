from django.shortcuts import render
from rest_framework.response import Response
from .models import User,Book
from .serializers import UserSerializer,BookSerializer, BookUpdateSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class UserView(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"successful": serializer.data }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BooksView(APIView):
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request):
        title = request.query_params.get("title")
        try:
            print(title)
            book = Book.objects.get(title=title)
            print(book)
            if book:
                serializer = BookUpdateSerializer(book,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error":"book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response({"success":"Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist:
            return Response({"Error":"Book does not exist"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)