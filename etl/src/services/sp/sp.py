from src.requester import request as r
from lxml import html
from datetime import (datetime)
from src import category_mapping;
from src.utils.date_fixer import date_cleaner
from src.configs import settings

def sp_scrape():

    request = r.get(
        url= settings.s_base,
        params={
            'html': True,
            'before_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    )

    items: list = []
    for item in request.json().get('news'):
        p = html.fromstring(item.get('html'))
        items.append(
            {
                'post_id': int(item.get('id')),
                'title': next(iter(p.xpath('//h2[@class="itemTitle"]/a/text()')), None),
                'link': settings.s_base + next(iter(p.xpath('//h2[@class="itemTitle"]/a/@href')), None),
                'description': next(iter(p.xpath('//div[@class="txt"]/text()')), None),
                'image_url': settings.s_base + next(iter(p.xpath('//img/@src')), None),
                # To clean date use call the date_cleaner that takes one argument
                'posted_on': date_cleaner(next(iter(p.xpath('//span[1]/text()')), 'None').lower()),
                'category': category_mapping.get(
                    next(iter(p.xpath('//span[@class="itemCat"]/text()')), None)
                ,"OTHER"),
                'source': 'sp'

            }
        )


    return items

