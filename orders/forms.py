from django import forms
from django.contrib.auth import get_user_model

from orders import models

User = get_user_model()


class GuessCheckoutForm(forms.Form):
    email = forms.EmailField()
    email2 = forms.EmailField(label='verify Email')

    def clean(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")

        if email == email2:
            user_exists = User.objects.filter(email=email).count()
            if user_exists != 0:
                raise forms.ValidationError("This User allready exists. Please login instead.")
            return email2
        else:
            raise forms.ValidationError("Please confirm emails are the same")


class AddressForm(forms.Form):
    billing_address = forms.ModelChoiceField(
        queryset=models.UserAddress.objects.filter(type="billing"),
        empty_label=None,
        widget=forms.RadioSelect,
    )
    shipping_address = forms.ModelChoiceField(
        queryset=models.UserAddress.objects.filter(type="shipping"),
        empty_label=None,
        widget=forms.RadioSelect,
    )


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = models.UserAddress
        fields = [
            'street',
            'city',
            'state',
            'zipcode',
            'type'
        ]
