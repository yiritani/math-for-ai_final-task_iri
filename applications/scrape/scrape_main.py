from bs4 import BeautifulSoup
from urllib import request
import csv
import time
from typing import List, Tuple, Any
from pathlib import Path

from .config import config_getter

config = config_getter.config_initialize()
path = Path(__file__).parent


def initializing_model_data() -> str:
    """
    Create csv header for input data
    and
    Return csv file name
    :return: csv filename
    """
    path = config_getter.get_templates_directory()
    file = path + '/' + config['FILE']['BACKUP_FILE_NAME']

    with open(file, 'w') as f:
        writer = csv.writer(f)
        # writer.writerow(['Name','FarFromStation','Age','Price','ManagementPrice','TotalPrice'])
        writer.writerow(['FarFromStation', 'Age', 'Price', 'ManagementPrice', 'TotalPrice'])

    return file


def get_hyper_text_mark_up_text(target_url:str, num: int) -> BeautifulSoup:
    response = request.urlopen(str(target_url) + str(num))
    soup = BeautifulSoup(response)
    response.close()

    return soup


def create_data(soup_data):
    result = []
    try:
        name = soup_data.find_all('a', class_='js-cassetLinkHref')
        far_from_station = soup_data.find_all('div', class_='detailnote-box')
        age = soup_data.find_all('td', class_='detailbox-property-col detailbox-property--col3')
        # floor_plan = soup_data.find_all('span', class_='cassetteitem_madori')
        price = soup_data.find_all('div', class_='detailbox-property-point')
        management_price = soup_data.find_all('td', class_='detailbox-property-col detailbox-property--col1')

        # タグや改行など除去
        far_from_station_only_myoden = [i.find('div', style="font-weight:bold") for i in far_from_station if
                                        'detailnote-box-item' not in str(i)]
        age_remove_new_line = [i.get_text().replace('\n', '') for i in age if '<!-- 築年 -->' in str(i)]
        price_remove_char = [float(i.get_text().replace('万円', '')) for i in price]

        management_price_list = str(management_price).split('\n')
        management_price_list_remove_other_rows = []
        for i in management_price_list:
            if '管理費' in i:
                tmp_i = i.replace('<div>管理費 ', '').replace('</div>', '').replace('円', '')
                if tmp_i == '-':
                    management_price_list_remove_other_rows.append(0.0)
                else:
                    management_price_list_remove_other_rows.append(float(tmp_i) / 10000.0)

        for i in range(len(name)):
            far_from_station_trim_start_index = far_from_station_only_myoden[i].get_text().rfind('歩') + 1
            far_from_station_trim_end_index = far_from_station_only_myoden[i].get_text().rfind('分')

            age_trim_start_index = age_remove_new_line[i].rfind('築') + 1
            age_trim_end_index = age_remove_new_line[i].rfind('年')

            result.append((
                # name[i].get_text(),
                far_from_station_only_myoden[i].get_text()[far_from_station_trim_start_index: far_from_station_trim_end_index],
                age_remove_new_line[i][age_trim_start_index: age_trim_end_index],
                price_remove_char[i],
                management_price_list_remove_other_rows[i],
                price_remove_char[i] + management_price_list_remove_other_rows[i]
            ))

        return result

    except:
        pass


def generate_csv(csvList: List[Tuple[Any, Any, float, float, float]], file):
    config_getter.get_templates_directory()

    for farFrom, age, price, managementPrice, totalPrice in csvList:
        # print(farFrom, age, price, managementPrice, totalPrice)
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([farFrom, age, price, managementPrice, totalPrice])


def scrape_main_func(target_url):
    file_name = initializing_model_data()
    print("*"*55,target_url)
    for page_num in range(1, 100):
        suumo_html = get_hyper_text_mark_up_text(target_url, page_num)
        rows = create_data(suumo_html)

        generate_csv(rows, file_name)

        if len(rows) <= 0:
            print('END')
            break

        print(f'=== page {page_num} done ===')
        break
        time.sleep(10)
        # break
