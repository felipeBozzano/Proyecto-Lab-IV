from rest_framework.routers import DefaultRouter
from correlatives.views import CorrelativeViewSet

router = DefaultRouter()
router.register('correlatives', CorrelativeViewSet, basename="correlatives")

urlpatterns = router.urls
