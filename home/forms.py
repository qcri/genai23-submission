from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList

class testingform(forms.Form):
    prompt = forms.CharField(label='Prompt', required=False)