from django import template
import markdown2

register = template.Library()

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    htmlversion=markdown2.markdown(markdown_text)
    return htmlversion