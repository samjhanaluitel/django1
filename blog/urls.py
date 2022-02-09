from django.urls import path
from .import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('path/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('path/new/', PostCreateView.as_view(), name='post-create'),
    path('path/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('path/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]