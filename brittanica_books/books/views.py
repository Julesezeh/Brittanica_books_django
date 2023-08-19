from django.shortcuts import render
from rest_framework.response import Response
from .models import User,Book
from .serializers import UserSerializer,BookSerializer
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
        # return Response(request.data)

    
