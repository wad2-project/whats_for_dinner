from django import template
from whats_for_dinner.models import *

register = template.Library()


@register.inclusion_tag('whats_for_dinner/cats.html')

def get_category_list(cat=None):
	return {'cats': Category.objects.all(), 'act_cat': cat}
