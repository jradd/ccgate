from rest_framework import generics
from rest_framework import permissions

from tags.models import Tag
from tags.serializers import TagSerializer


class TagList(generics.ListAPIView):
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        """
        List specific tags, else return all.
        """

        queryset = Tag.objects.all()
        query = self.request.QUERY_PARAMS.get('q', None)
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete tag instance.
    """
    model = Tag
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)