from src.crud.category import category_service
from src.crud.source import source_service
from src.services.sp.sp import sp_scrape
from src.utils.model_to_dict import model_to_dict
from src.crud.post import post_service
from datetime import datetime, timedelta
from src.services.un.un import un_scrape

def sp_adder():
    start_date = datetime.now() - timedelta(days=7)
    end_date = datetime.now()
    exiting_posts: list = []

    sp_posts = sp_scrape()

    for sp_post in sp_posts:
        source_uuid = source_service().get(name=sp_post.get('source'))
        print(sp_post.get('category'))
        category_uuid = category_service().get(label=sp_post.get('category'))
        sp_post.update({'source': source_uuid.id})
        sp_post.update({'category': category_uuid.id})

        post_service().add(**sp_post)


def uns_adder():
    start_date = datetime.now() - timedelta(weeks=54 * 2)
    end_date = datetime.now()
    uns_posts = un_scrape()

    for uns_post in uns_posts:
        source_uuid = source_service().get(name=uns_post.get('source'))
        category_uuid = category_service().get(label=uns_post.get('category'))

        uns_post.update({'source': source_uuid.id})
        uns_post.update({'category': category_uuid.id})

        post_service().add(**uns_post)

