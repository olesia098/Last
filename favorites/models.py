from django.contrib.auth import get_user_model
from django.db import models
from main.models import BooksDescription

User = get_user_model()


class Favorites(models.Model): # корзина
    # CART_STATUS = (
    #     ('IN_PROCESSING', 'in_processing'),
    #     ('COMPLETED', 'completed'), # ЗАВЕРШЕННЫЙ
    #     ('DECLINED', 'declined') # ОТКЛОНЕННЫЙ
    # )

    title = models.ForeignKey(BooksDescription, on_delete=models.CASCADE, related_name='favorites_item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    favorites = models.BooleanField('избранное', default=False)
    # status = models.CharField(max_length=30, choices=CART_STATUS, default='in_processing')

    def __str__(self):
        return self.user.email


class FavoritesItem(models.Model):
    title = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='favorites_item')
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    # quantity = models.PositiveIntegerField(default=1)
    # total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    # def __str__(self):
    #     return self.title

    # def save(self, *args, **kwargs):
    #     self.total_cost = self.product.price * self.quantity
    #     super(Favorites, self).save(*args, **kwargs)


