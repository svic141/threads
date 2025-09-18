from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class  Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering =('name', )
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class  Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price =models.FloatField()
    item_image =models.ImageField(upload_to="item_images", blank=True, null=True)
    item_image2 =models.ImageField(upload_to="item_images", blank=True, null=True)
    item_image3 =models.ImageField(upload_to="item_images", blank=True, null=True)
    on_sale = models.BooleanField(default=False, null=True)
    discount = models.FloatField(null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)

    class Meta:
        ordering =('name', )
        verbose_name_plural='Items'

    def __str__(self):
        return self.name