from rest_framework.routers import DefaultRouter
from users_degrees.views import UserDegreeViewSet

router = DefaultRouter()
router.register('users_degrees', UserDegreeViewSet, basename="users_degrees")

urlpatterns = router.urls
