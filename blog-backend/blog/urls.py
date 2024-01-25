from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoViewSet, PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    *router.urls,
    # path('users/<int:pk>/', UserViewSet.as_view({'get': 'get_user_by_pk'}), name='get_user_by_pk'),
    path('users/<int:user_id>/todos', TodoViewSet.as_view(
        {'get': 'get_todos_by_user_id', 'post': 'add_todo_by_user_id'}), name='user_todos'),
    path('users/<int:user_id>/todos/<int:todo_id>', TodoViewSet.as_view(
        {'patch': 'update_todo_by_user_id'}), name='user_todos'),
    path('users/<int:user_id>/posts', PostViewSet.as_view(
        {'get': 'get_posts_by_user_id', 'post': 'add_post_by_user_id'}), name='user_posts'),
    path('users/<int:user_id>/posts/<int:post_id>', CommentViewSet.as_view(
        {'get': 'get_comments_by_post_id', 'post': 'add_comment_by_post_id'}), name='user_posts'),
    path('users/<int:user_id>/albums', AlbumViewSet.as_view(
        {'get': 'get_albums_by_user_id', 'post': 'add_album_by_user_id'}), name='user_albums'),
    path('users/<int:user_id>/albums/<int:album_id>', PhotoViewSet.as_view(
        {'get': 'get_photos_by_album_id', 'post': 'add_photo_by_album_id'}), name='user_photos'),
]
