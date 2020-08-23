from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Poem
from .serializers import PoemSerializer

class HelloView(APIView):
  permission_classes = (IsAuthenticated,)
  
  def get(self, request):
    content = {'message': 'Hello World'}
    return Response(content)

class PoemList(generics.ListCreateAPIView):
  queryset = Poem.objects.all()
  serializer_class = PoemSerializer

class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Poem.objects.all()
  serializer_class = PoemSerializer
