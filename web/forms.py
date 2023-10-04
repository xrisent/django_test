from django.forms import ModelForm
from .models import *

class CreateForm(ModelForm):
    class Meta:
        model = Article
        fields = {'name', 'description'}