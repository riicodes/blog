from django.urls import path
from .views import (
    PostList,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete,
    UserPostList
)

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('user/<str:username>/', UserPostList.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('post/new/', PostCreate.as_view(), name='create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='delete'),
]
