from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowView, GroupViewSet, PostViewSet

app_name = 'api'
v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register(
    'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments',
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowView.as_view()),
]
