from django import forms
from django.forms.models import modelformset_factory

from products import models


class VariationInventoryForm(forms.ModelForm):
    class Meta:
        model = models.Variation
        fields = [
            "price",
            "sale_price",
            "inventory",
            'active',
        ]

VariationInventoryFormSet = modelformset_factory(models.Variation, form=VariationInventoryForm, extra=0)