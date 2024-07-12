from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Product
        fields = ["name", "price", "product_code", "age_start", "age_end", "height", "width", "length", "weight", "concrete", "installation_time", "photo"]


class TagForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Tag
        fields = ["name"]
