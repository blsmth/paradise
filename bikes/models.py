from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse
from filebrowser.fields import FileBrowseField


class BikeManager(models.Manager):
    pass

class Bike(models.Model):
    name = models.CharField("Name",max_length=256,blank=False,null=False)
    slug = models.SlugField()
    motto = models.CharField("Motto",max_length=256, blank=True,null=True)
    description = models.TextField("Description",blank=False,null=False)

    
    objects = BikeManager()
    
    class Meta:
        verbose_name = "Bike"
        verbose_name_plural = "Bikes"


    def get_absolute_url(self):
        return (reverse('bike-display', args=[self.slug]))
    
    # TO DO: Add Image Gallery.  Either another class or part of Build class
class Image(models.Model):
    bike = models.ForeignKey(Bike,related_name="bike") 
    title = models.CharField("Title",max_length=256,blank=True,null=True)
    slug = models.SlugField() 
    description = models.TextField("Description",blank=True)
    file = FileBrowseField("File", 
        max_length=200, 
        format="Image", 
        directory="bikes/",
        blank=True)