from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status

from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    List all posts or create a new post.
    """
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.author = self.request.user


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post [instance].
    """
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


def home(request, template_name="home.html"):
        return render_to_response(template_name,
                                                    context_instance=RequestContext(request))