from django import forms

from .models import Staff
from .widgets import CropWidget


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=CropWidget())

    class Meta:
        model = Staff
        fields = ('lname', 'fname', 'sname')
