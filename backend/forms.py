from django.forms import ModelForm 
from backend.models import Carausel


class FormCarausel(ModelForm):
    class Meta:
        model = Carausel
        fields = '__all__'
