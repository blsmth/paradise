from django import template

register = template.Library()



#@register.filter()
#@register.inclusion_tag(template,takes_context=True/False)

@register.inclusion_tag('bikes/latest_front.html')
def latest_bike_front():
	bike = Bike.objects.get_latest()
	return bike
