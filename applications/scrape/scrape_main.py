from bs4 import BeautifulSoup
from urllib import request
import csv
import time
from typing import List, Tuple
from pathlib import Path
import yaml

path = Path(__file__).parent
with open(str(path) + '/config.yml') as yml:
    config = yaml.load(yml)


def initializingModelData() -> str:
    """
    Create csv header for input data
    and
    Return csv file name
    :return: csv filename
    """
    global path
    print(path)
    path /= '../ML_learning/templates'
    # print(path.resolve())
    file = str(path.resolve()) + '/' + config['BACKUP_FILE_NAME']
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Name','FarFromStation','Age','Price','ManagementPrice','TotalPrice'])

    return file


def getHyperTextMarkUpText(num: int) -> BeautifulSoup:
    # url = config['MAIN_URL']

    response = request.urlopen(config['MAIN_URL'] + str(num))
    soup = BeautifulSoup(response)
    response.close()

    return soup


def createData(soup_data):
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
                                        not 'detailnote-box-item' in str(i)]
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

            print(name[i].get_text(), )
            print(far_from_station_only_myoden[i].get_text()[
                  far_from_station_trim_start_index: far_from_station_trim_end_index], )
            print(age_remove_new_line[i][age_trim_start_index: age_trim_end_index], )
            # floor_plan[i].get_text(),
            print(price_remove_char[i])
            print(management_price_list_remove_other_rows[i])
            print(price_remove_char[i] + management_price_list_remove_other_rows[i])
            print('*' * 22)

            result.append((
                name[i].get_text(),
                far_from_station_only_myoden[i].get_text()[
                far_from_station_trim_start_index: far_from_station_trim_end_index],
                age_remove_new_line[i][age_trim_start_index: age_trim_end_index],
                price_remove_char[i],
                management_price_list_remove_other_rows[i],
                price_remove_char[i] + management_price_list_remove_other_rows[i]
            ))

            # result.append((name[i]))

            # result.append((name[i].get_text(), far_from_station.get_text(), age[i].get_text(), floor_plan[i].get_text(), price[i].get_text(),))

        return result

    except IndexError as indexerror:
        print(indexerror)
        return result


def generateCsv(csvList: List[Tuple[str]], file):
    global path
    print(path)
    path /= '../templates'
    # print(path.resolve())
    # file = str(path.resolve()) + '/' + config['BACKUP_FILE_NAME']

    for name, farFrom, age, price, managementPrice, totalPrice in csvList:
        print(name, farFrom, age, price, managementPrice, totalPrice)
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([name, farFrom, age, price, managementPrice, totalPrice])


def scrape_main_func():
    file_name = initializingModelData()

    cnt = 0

    for page_num in range(1, 6):
        suumo_html = getHyperTextMarkUpText(page_num)
        rows = createData(suumo_html)

        generateCsv(rows, file_name)

        time.sleep(10)
