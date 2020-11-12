from django import template
from datetime import datetime

register=template.Library()

@register.filter            # 1
def add_str(left, right):
	return left +' '+ right

@register.simple_tag            # 2
def today():
	return datetime.now().strftime("%Y-%m-%d %H:%M")



