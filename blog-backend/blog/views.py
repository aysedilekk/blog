from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from blog.models import User, Todo, Post, Comment, Album, Photo
from blog.serializers import UserSerializer, TodoSerializer, PostSerializer, CommentSerializer, AlbumSerializer, \
    PhotoSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=True, methods=["post"])
    def add_todo_by_user_id(self, request, user_id=None):
        request.data.update({"user": user_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["patch"])
    def update_todo_by_user_id(self, request, user_id=None, todo_id=None):
        todo = self.queryset.get(user_id=user_id, id=todo_id)
        todo.completed = request.data["completed"]
        todo.save()
        serializer = self.get_serializer(todo)
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["get"])
    def get_todos_by_user_id(self, request, user_id=None):
        todos = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(todos, many=True)

        return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=["post"])
    def add_post_by_user_id(self, request, user_id=None):
        request.data.update({"user": user_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["get"])
    def get_posts_by_user_id(self, request, user_id=None):
        posts = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=["post"])
    def add_comment_by_post_id(self, request, user_id=None, post_id=None):
        request.data.update({"user": user_id})
        request.data.update({"post": post_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["get"])
    def get_comments_by_post_id(self, request, user_id=None, post_id=None):
        posts = self.queryset.filter(post_id=post_id)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @action(detail=True, methods=["post"])
    def add_album_by_user_id(self, request, user_id=None):
        request.data.update({"user": user_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["get"])
    def get_albums_by_user_id(self, request, user_id=None):
        albums = self.queryset.filter(user_id=user_id)
        serializer = self.get_serializer(albums, many=True)
        return Response(serializer.data)


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(detail=True, methods=["post"])
    def add_photo_by_album_id(self, request, user_id=None, album_id=None):
        request.data.update({"user": user_id})
        request.data.update({"album": album_id})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["get"])
    def get_photos_by_album_id(self, request, user_id=None, album_id=None):
        photos = self.queryset.filter(album_id=album_id)
        serializer = self.get_serializer(photos, many=True)
        return Response(serializer.data)
