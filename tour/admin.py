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

from tour.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['title','start_date','end_date','description']
    prepopulated_fields = {'slug': ('title',)}
    
    
admin.site.register(Event,EventAdmin)