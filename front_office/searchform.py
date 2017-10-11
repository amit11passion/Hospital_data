from django import forms


class searchform(forms.Form):
    patientid = forms.IntegerField(required=True)
