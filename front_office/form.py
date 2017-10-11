from django import forms
from .models import Pdata

CHOICES = [(0, 'Non-diabetic'),
           (1, 'Diabetic')]


class Personalform(forms.ModelForm):
    patientid = forms.IntegerField(required=True)
    Name = forms.CharField(required=True)
    DateofBirth = forms.DateField(required=True,help_text="YYYY-MM-DD")
    Email = forms.CharField(required=True)
    Address = forms.CharField(required=True)

    class Meta:
        model = Pdata
        #fields name should be same as forms field name
        fields = ('patientid','Name', 'DateofBirth', 'Email', 'Address')



class PictureForm(forms.Form):
    # like = forms.ChoiceField()
        analyses = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())