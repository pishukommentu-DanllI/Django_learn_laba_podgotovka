from django import forms
from .models import Dishes, Hall


class Order_form(forms.Form):
    customer_name = forms.CharField(max_length=50, label='FIO')

    COICE_HALL = [(i.id, i.name) for i in Hall.objects.all()]
    hall = forms.ChoiceField(choices=COICE_HALL, label='Hall')

    COICE_DISHES = [(i.id, i.name) for i in Dishes.objects.all()]
    dishes = forms.MultipleChoiceField(choices=COICE_DISHES, label='Dishes')

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    Times_Data_Choice = [(1, 'Morhing'), (2, 'Lunch'), (3, 'Evening')]

    times_day = forms.ChoiceField(choices=Times_Data_Choice)

    chekbox = CheckBox = forms.CharField(label='consent to the processing of personal data', widget=forms.CheckboxInput())

    people_count = forms.IntegerField(label='Count people')

