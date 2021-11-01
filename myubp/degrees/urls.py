from rest_framework.routers import DefaultRouter
from degrees.views import DegreeViewSet

router = DefaultRouter()
router.register('degrees', DegreeViewSet, basename="degrees")

urlpatterns = router.urls
