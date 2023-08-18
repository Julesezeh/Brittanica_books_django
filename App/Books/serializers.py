from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = "__all__"

    def validate(self, data):
        if not data.get("username"):
            return serializers.ValidationError("username field is required")
        if not data.get("first_name"):
            raise serializers.ValidationError("first_name field is required")
        if not data.get("last_name"):
            raise serializers.ValidationError("last_name field is required")
        if not data.get("email"):
            raise serializers.ValidationError("email field is required")
        return data

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
