from django.shortcuts import render
from .models import Snack,Post
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer,PostSerializer
from rest_framework.permissions import AllowAny ,IsAuthenticated



class SnackListView(ListCreateAPIView):  
    queryset = Snack.objects.all() 
    serializer_class = SnackSerializer


class SnackListView(ListCreateAPIView):  
    queryset = Snack.objects.all() 
    serializer_class = SnackSerializer 
    permission_classes = [AllowAny]


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsAuthenticated]


class PostListView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class  PostDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

# Create your views here.
