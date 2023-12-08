from django import forms

class testingform(forms.Form):
    prompt = forms.CharField(label='prompt', required=False)