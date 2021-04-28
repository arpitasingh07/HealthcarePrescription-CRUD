from django import forms
from health.models import Prescription

class Patientforms(forms.ModelForm):
    class Meta:
        model=Prescription
        fields="__all__"