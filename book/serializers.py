from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200, default='Django REST Framework')
#     author = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.save()
#         return instance
#
#     def validate_title(self, value):
#         if 'django' not in value.lower():
#             raise serializers.ValidationError('В имени должно присутствовать слово django!')
#         return value
#
#     def validate(self, data):
#         if data['title'] == data['author']:
#             raise serializers.ValidationError('Введены одинаковые значения полей')
#         return data