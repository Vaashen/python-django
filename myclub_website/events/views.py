from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm

# Create your views here.
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if  'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_event.html', 
                  {"form":form,
                   'submitted': submitted})


def update_venue(request, venue_id):
    venue= Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    
    return render(request, 'events/update_venue.html',
                  {'venue': venue,
                   'form':form})


def list_venues(request):
    venues_list = Venue.objects.all()
    return render(request, 'events/venues.html',
                  {'venues_list': venues_list}) 


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if  'submitted' in request.GET:
            submitted = True
            
    return render(request, 'events/add_venue.html', 
                  {"form":form,
                   'submitted': submitted})
    
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})    
    
    
    
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    
    month = month.title()
    
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    
    return render(request, 'events/home.html', 
                  {
                      'year': year,
                      'month': month,
                      "cal": cal
                  })