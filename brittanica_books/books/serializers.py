from rest_framework import serializers
from .models import User,Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserCreationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    user_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = "__all__"

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name","last_name","email")



class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    locccn = serializers.IntegerField(required=True)

    class Meta:
        model = Book
        fields = "__all__"

class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("locccn","title")