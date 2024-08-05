from django.shortcuts import get_object_or_404

from rest_framework import filters, generics, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from posts.models import Comment, Follow, Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        post = self.get_object()
        self.check_object_permissions(request, post)
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        self.check_object_permissions(request, post)
        return super().destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(post_id=post_id, author=self.request.user)

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response(
                {"detail": "You dont have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({
                "detail": "Authentication credentials were not provided."},
                status=status.HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED)
