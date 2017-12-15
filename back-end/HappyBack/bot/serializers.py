from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Character
        fields = ('user_id', 'book_name' , 'reading_start_time', 'book_length', 'start_date','expected_end_date','average_pages_to_read','pages_read')
        read_only_fields = ('user_id', 'date_modified')