from rest_framework import generics
from .serializers import CharacterSerializer
from .models import Character

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()