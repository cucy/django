from django import template

register = template.Library()

from django.utils.html import format_html


@register.simple_tag
def cut_page(curr_page, loop_page):
    """ [1,2,3,,4,5]   总是显示5个元素 即使有100个分页长度"""

    try:
        curr_page = int(curr_page)
        loop_page = int(loop_page)
    except Exception as e:
        return ''
    offest = abs(curr_page - loop_page)
    page_el_ = """  <li class="page-item {}">
      <a class="page-link" href="?page={}">{}</a>
    </li>"""

    if offest < 5:
        if curr_page == loop_page:
            page_el = page_el_.format("active", loop_page, loop_page)
        else:
            page_el = page_el_.format("ff", loop_page, loop_page)
        return format_html(page_el)
    return ''
