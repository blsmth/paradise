from django.contrib.sites.models import Site
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.mail import mail_managers, send_mail
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.context import RequestContext
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from paradise.forms import ContactForm

from paradise.tour.models import Event

def home(request):
    events = Event.objects.get_upcoming()
    return render(request,'home.html', {'events': events })
    
def contact(request):
    locked = False
    if not request.method == 'POST':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            recipients = ['steve@paradisechoppers.com','chuck@paradisechoppers.com','brendan@thronegroup.com']
            send_mail(subject, message, email, recipients)
            messages.success(request, 'Thanks for your email.  We will get back to you ASAP.')
            locked = True    
    template_data = {'form': form, 'locked': locked }
    return render(request, 'contact.html', template_data)
    
    
    

def coming_soon(request):
    return render(request, 'coming_soon.html')