from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginApiView, UserProfileViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename="profiles")

urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
