from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet, AvgNoteViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet, basename="notes")
router.register('notes-avg', AvgNoteViewSet, basename="avg-notes")

urlpatterns = router.urls
