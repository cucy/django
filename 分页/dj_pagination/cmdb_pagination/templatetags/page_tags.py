from django import template

register = template.Library()


@register.simple_tag
def get_pagination_html(pager):
    return pager.to_html()
