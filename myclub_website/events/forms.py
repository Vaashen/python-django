from django import forms
from django.forms import ModelForm
from .models import Venue, Event


class VenueForm(ModelForm):
    """This is a class that will create a Venue form for my website.
        The form will ask for: venue name, address, zip code, phone number, web address, and email address.
    """
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone_num', 'web', 'email_address')
        labels ={
            'name': '',
            'address':'',
            'zip_code':'',
            'phone_num':'',
            'web':'',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Venue Name'}),
            'address':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code'}),
            'phone_num':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'web':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Web Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),   
        }
        

class EventForm(ModelForm):
    """This is a class that will create a event form for my website.
        It will be used to ask the user to input details about the event they wan to book, details such as:
        name of the event, evet date, maager of the event, attendees of the event etc.
    """
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels ={
            'name': '',
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Venue',
            'manager':'Manager',
            'attendees':'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Event Name'}),
            'event_date':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'venue':forms.Select(attrs={'class': 'form-select', 'placeholder': 'Venue'}),
            'manager':forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),   
        }