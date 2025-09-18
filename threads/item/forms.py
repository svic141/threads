from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'category', 'quantity', 'price', 'item_image', 'item_image2', 'item_image3', 'on_sale', 'discount',)

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'category', 'quantity', 'price', 'item_image', 'item_image2', 'item_image3', 'on_sale', 'discount', 'is_sold')

        