from rest_framework import serializers

from favorites.models import FavoritesItem, Favorites


class FavoritesItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritesItem
        fields = ('user', 'title')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('title', 'user', 'favorites')

