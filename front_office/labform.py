from django import forms
from .models import Labdata


class LabDetail(forms.ModelForm):
    PatientId = forms.IntegerField(required=True)
    BloodGlucoseRange = forms.IntegerField(required=True, help_text="mg/dL")
    BloodPressure = forms.IntegerField(required=True, help_text="mm Hg")
    HeartRates = forms.IntegerField(required=True, help_text="bpm")
    SkinThikness = forms.FloatField(required=True)
    PragnencyParYear = forms.IntegerField(required=True)
    # pateintid = models.ForeignKey(Pdata, on_delete=models.CASCADE)
    # BloodGlucoseRang = models.IntegerField(default=0)
    # BloodPressure = models.IntegerField(default=0)
    # HeartRates = models.IntegerField(default=0)
    # SkinThikness = models.FloatField(default=0)
    # PragnencyParYear = models.IntegerField(default=0)
    # Diabetes = models.IntegerField(default=0)

    class Meta:
        model = Labdata
        # fields name should be same as forms field name
        fields = ( 'PatientId','BloodGlucoseRange', 'BloodPressure', 'HeartRates', 'SkinThikness','PragnencyParYear')




