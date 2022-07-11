from django.forms import ModelForm
from django import forms
from basedatos.models import producto
    
class productoForm(ModelForm):
        class Meta:
            model = producto
            fields = "__all__"