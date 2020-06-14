from django import forms

class BuildingForm(forms.Form):

    id = forms.IntegerField(required=True)
    element_name = forms.CharField(max_length="50",required=True)