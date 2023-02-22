from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Review, RATE_CHOICES, School



class ReviewForm(ModelForm):

    location = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range  ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'locationid', 'style': 'form-range-thumb-bg: #A38D5E;'}), required=True)
    opportunities = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'opportunitiesid'}), required=True)
    facilities = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'facilitiesid'}), required=True)
    food = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'foodif'}), required=True)
    clubs = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'clubs'}), required=True)
    social = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-range ', 'type': 'range', 'min': '1', 'max': '5', 'id': 'social'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height:130px'}))

    class Meta:
        model = Review
        fields = ['location', 'opportunities', 'facilities', 'food', 'clubs', 'social','body']
        exclude = ['user', 'school', 'overall']