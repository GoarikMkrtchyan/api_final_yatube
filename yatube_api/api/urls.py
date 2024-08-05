from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
]
