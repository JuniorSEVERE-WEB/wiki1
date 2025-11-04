from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
def markdown_to_html(text):
    """
    Convertit le texte Markdown en HTML
    """
    if text:
        html = markdown.markdown(text, extensions=['extra', 'codehilite'])
        return mark_safe(html)
    return ""