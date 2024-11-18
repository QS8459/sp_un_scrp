from src.requester import request;
from src.utils.date_fixer import date_cleaner;
from src import category_mapping
from src.configs import settings
def un_scrape():
    req = request.get(
        url = settings.u_base_api,
        params={
            'page':1,
            'fresh':True
        }
    )
    posts_a:list = []
    posts = req.json().get('result').get('posts');
    for post in req.json().get('result').get('posts'):
        for i in post.get('data'):
            posts_a.append(
                {
                    'post_id': (i.get('id')),
                    'title':i.get('title'),
                    'link': i.get("id"),
                    'description':i.get('meta_description'),
                    'image_url':i.get('image'),
                    'posted_on':date_cleaner(i.get('created_at').lower()),
                    'category': category_mapping.get(
                        i.get('category').get('name') if i.get('category') is not None else None
                    ,"OTHER"),
                    'source': 'un'
                }
            )
            # print(i.get('category').get('name') if i.get('category') is not None else None)
    return posts_a;
