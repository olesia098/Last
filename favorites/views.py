from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from favorites.models import Favorites
from favorites.serializers import FavoritesSerializer
from rest_framework.decorators import action


class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    def favorites(self, request, *args, **kwargs):
        title = self.get_object()
        favorites_obj, _ = Favorites.objects.get_or_create(title=title, user=request.user)
        favorites_obj.favorites = not favorites_obj.favorites
        favorites_obj.save()
        status = 'liked'
        if not favorites_obj.favorites:
            status = 'unlike'
        return Response({'status': status})
