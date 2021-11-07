from rest_framework.routers import DefaultRouter
from subjects.views import SubjectViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename="subjects")

urlpatterns = router.urls
