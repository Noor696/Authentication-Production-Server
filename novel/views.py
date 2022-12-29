from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Novel
from .serializers  import NovelSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class NovelListView(ListCreateAPIView):
# queryset means show user the data and can create another data from list
   queryset=Novel.objects.all()
   serializer_class = NovelSerializer # afile resposible to convert python code to JSON data/ format
#    permission_classes = [IsAuthenticatedOrReadOnly]

class NovelDetailView(RetrieveUpdateDestroyAPIView):
# RetrieveUpdateDestroyAPIView : mean reading , can Updating and delete

   queryset=Novel.objects.all()
   serializer_class = NovelSerializer
   permission_classes = [IsOwnerOrReadOnly]
