from django.contrib import admin
from django.utils.safestring import mark_safe
from django.core.mail import mail_managers, send_mail
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.template import Template, Context, RequestContext, loader, get_library
from datetime import datetime, date
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.contrib import messages

from bikes.models import Bike, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fieldsets = (
        (' ', {
            'classes': ('collapse',),
            'fields': ('title','description','file'),
        }),
    )


class BikeAdmin(admin.ModelAdmin): 
    inlines = [ImageInline]
    list_display = ['name','motto','description']
    prepopulated_fields = {'slug': ('name',)}
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title','description',]


admin.site.register(Bike,BikeAdmin)
admin.site.register(Image,ImageAdmin)