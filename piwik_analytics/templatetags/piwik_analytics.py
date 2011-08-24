from django import template
from google_analytics.templatetags import analytics

register = template.Library()
register.tag('piwik_analytics', analytics.do_get_analytics)
