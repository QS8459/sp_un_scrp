from src.services.add_to_db import sp_adder, uns_adder;
from src.configs import settings
if __name__ == "__main__":
    # print(category_mapping.get("3","OTHER"))
    # category_service().add(label = category_mapping.get('Свой бизнес'))

    sp_adder();
    uns_adder();
    #print(settings.u_base_api)
