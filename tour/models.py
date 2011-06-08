from django.db import models
from django.contrib.localflavor.us.models import USStateField
from datetime import datetime
# Create your models here.


class EventManager(models.Manager):
    def get_upcoming(self):
        return self.filter(end_date__gte=datetime.now()).order_by('start_date')[:3]

class Event(models.Model):
    title = models.CharField("Title",max_length=200,null=False,blank=False)
    slug = models.SlugField("Slug",help_text="Don't worry abou this. It's used for URL's.")
    start_date = models.DateField("Start Date/Time",blank=False,null=False)
    end_date = models.DateField("End Date/Time",blank=True,null=True,help_text="Leave blank for one day event")
    description = models.TextField("Event Description",blank=True)
    #TODO: add photo field, 
    link = models.URLField("Link",blank=True,verify_exists=True,help_text="Link to event's official website. \
    For instance Harley Rendezvous' website.")
    address = models.CharField("Address",max_length=256,blank=True)
    city = models.CharField("City",max_length=100,blank=True)
    state = USStateField("State",blank=True)
    zipcode = models.CharField("Zipcode",max_length=5,blank=True)
    
    
    objects = EventManager()