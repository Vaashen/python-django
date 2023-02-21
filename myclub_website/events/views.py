from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm

# Create your views here.
def add_event(request):
    """This function will allow the user to add an event using the event form.
    If the request method is POST, and if the details entered are all valid, save the form and store in the database.
    
    :param request: will be used to determine if the method is POST or GET
    :type request: Any
    
    :return: render the add_event.html
    :rtype: render request
    """
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
    """This function will allow the user to update a venue.
    It will fetch the Venue form using the Venues id number.
    If the form details are valid, save the changes.
    
    :param venue_id: the id number for the venue in the database
    :type venue_id: int
    
    :return: redirects you back to the url called list-venues
    :rtype: redirect
    
    :return: loads the update_venue.html file 
    :rtype: render
    """
    venue= Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    
    return render(request, 'events/update_venue.html',
                  {'venue': venue,
                   'form':form})


def list_venues(request):
    """This function returns all the venues in a readable manner on the website.
    
    :return: loads the venues.html file
    :rtype: render
    """
    venues_list = Venue.objects.all()
    return render(request, 'events/venues.html',
                  {'venues_list': venues_list}) 


def add_venue(request):
    """This function will allow the user to add a new venue.
    If the request method is post, it will call the Venue form and allow the user to fill in the details,
    if all the details are valid, save the form and post it to the database
    
    :return: will redirect the user to thier submiited form
    :rtype: HttpResponseRedirect
    
    :return: will load the add_venue.html file
    :rtype: render
    """
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
    """This function will display all the events that have been submiited in a readable manner on the website.
    
    :return: it will load the event_list.html file and will get all the events in the database and display it here
    :rtype: render
    """
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})    
    
    
    
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    """This function will display a calendar on the home page of the website, it will autmatically update each month for every year.
    
    :param year: this will use the datetime module to get the current year
    :type year: int
    
    :param month: this will also use the datetime module to get the curret month
    :type month: str
    
    :return: it will return a calendar showing the current month and the days with the current year on the home page
    :rtypeL: render
    """
    
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