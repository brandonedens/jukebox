
from django import template

register = template.Library()

LEADING_PAGE_RANGE_DISPLAYED = TRAILING_PAGE_RANGE_DISPLAYED = 3
LEADING_PAGE_RANGE = TRAILING_PAGE_RANGE = 2
NUM_PAGES_OUTSIDE_RANGE = 2
ADJACENT_PAGES = 1

def digg_paginator(context):
    if (context["is_paginated"]):
        " Initialize variables "
        in_leading_range = in_trailing_range = False
        pages_outside_leading_range = pages_outside_trailing_range = range(0)

        paginator = context['paginator']
        page_obj = context['page_obj']

        if (paginator.num_pages <= LEADING_PAGE_RANGE_DISPLAYED):
            in_leading_range = in_trailing_range = True
            page_numbers = [n for n in range(1, paginator.num_pages + 1) if n > 0 and n <= paginator.num_pages]
        elif (page_obj.number <= LEADING_PAGE_RANGE):
            in_leading_range = True
            page_numbers = [n for n in range(1, LEADING_PAGE_RANGE_DISPLAYED + 1) if n > 0 and n <= paginator.num_pages]
            pages_outside_leading_range = [n + paginator.num_pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)]
        elif (page_obj.number > paginator.num_pages - TRAILING_PAGE_RANGE):
            in_trailing_range = True
            page_numbers = [n for n in range(paginator.num_pages - TRAILING_PAGE_RANGE_DISPLAYED + 1, paginator.num_pages + 1) if n > 0 and n <= paginator.num_pages]
            pages_outside_trailing_range = [n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)]
        else:
            page_numbers = [n for n in range(page_obj.number - ADJACENT_PAGES, page_obj.number + ADJACENT_PAGES + 1) if n > 0 and n <= paginator.num_pages]
            pages_outside_leading_range = [n + paginator.num_pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)]
            pages_outside_trailing_range = [n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)]
        return {
            "is_paginated": context["is_paginated"],
            "page_obj": context["page_obj"],
            "page_numbers": page_numbers,
            "in_leading_range" : in_leading_range,
            "in_trailing_range" : in_trailing_range,
            "pages_outside_leading_range": pages_outside_leading_range,
            "pages_outside_trailing_range": pages_outside_trailing_range
        }

register.inclusion_tag("digg_paginator.html", takes_context=True)(digg_paginator)

