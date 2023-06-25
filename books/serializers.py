from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'massage': "Kitob sarlovhasi hariflardan tashkel topgan bo'lishi kerak!"
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'massage': "Kitob sarlovhasi va mualifi birxil bo'lgan kitobni yuklay olmaysiz."
                }

            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 100000000000:
            raise ValidationError(
                {
                    'status': False,
                    'massage': "narx kiritishda xatolikka yo'l qo'ydiz"
                }

            )
