from django.db import models

# Create your models here.
class Venue(models.Model):
    """This is a class that will be used for the venues, it will have all the fields needed to make a bookig fo ra venue.
    
    :return: it will return a string output showing the name of the venue
    :rtype: str
    """
    
    name = models.CharField(max_length=120) 
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=25, blank=True)
    web = models.URLField(blank=True)
    email_address = models.EmailField(blank=True)
    
    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    """This is a class that will store the details for the users that register on the website
    
    :return: it will return thier first and last names 
    :rtype: str
    """
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
        
class Event(models.Model):
    """This is a class that will have the fields to the events that have been booked, including the venues details.
    
    :return: it will return the name of the event 
    :rtype: str
    """
    
    name = models.CharField('Event Name', max_length=120)
    event_date =models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    
    def __str__(self):
        return self.name
    
