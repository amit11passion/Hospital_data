from django import forms

diabet = 0
ndiabet = 1
PREFERRED_DB_CHOICES = (
    (diabet, 'diabet'),
    (ndiabet, 'ndiabet'),
)


class DForm(forms.Form):
    preferred_drink = forms.ChoiceField(choices=PREFERRED_DB_CHOICES,
                                        widget=forms.RadioSelect())