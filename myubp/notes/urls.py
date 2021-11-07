from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet, basename="notes")

urlpatterns = router.urls
