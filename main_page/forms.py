from django import forms

from main_page.models import Congratulation


class CongratulationForm(forms.ModelForm):
    class Meta:
        model = Congratulation
        fields = ('congratulation',)
