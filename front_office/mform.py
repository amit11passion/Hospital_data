from django import forms


class msearchform(forms.Form):
    patientid = forms.IntegerField(required=True)
