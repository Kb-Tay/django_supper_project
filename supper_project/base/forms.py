from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["supper_places","food"]


