from datetime import datetime
from django import forms
from .models import Room, Application

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['house_name', 'block_num', 'room_num', 'available']

class ApplicationForm(forms.ModelForm):
    application_date = forms.DateTimeField(
        initial=datetime.now(),  # Set the initial value to the current date and time
        widget=forms.HiddenInput(),  # You can hide this field if you don't want the user to see it
    )

    class Meta:
        model = Application
        fields = ['application_date']
