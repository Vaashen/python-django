from django.contrib import admin
from .models import Venue
from . models import Event
from .models import MyClubUser

# Register your models here.
admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
