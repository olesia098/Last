
from rest_framework.routers import DefaultRouter

from favorites.views import FavoritesViewSet

router = DefaultRouter()
router.register('', FavoritesViewSet)

urlpatterns = []
urlpatterns.extend(router.urls)