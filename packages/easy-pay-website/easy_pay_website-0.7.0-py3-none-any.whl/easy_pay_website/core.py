import requests
import re
import os
import time
from bs4 import BeautifulSoup
import ddddocr
from odin_functions import check
from typing import Union
import urllib.parse

def get_session():
    return requests.Session()

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def handle_response(response, message):
    if check.type_name(response) == 'NoneType':
        return {
            "result": False,
            "message": message,
            "data": []
        }
    return None

def fetch_captcha(session, url, cookies, timestamp):
    response = session.get(url, cookies=cookies, timeout=5)
    captcha_path = f"captcha_{str(timestamp)}.png"
    with open(captcha_path, "wb") as file:
        file.write(response.content)
    return captcha_path

def solve_captcha(captcha_path):
    ocr = ddddocr.DdddOcr()
    with open(captcha_path, 'rb') as f:
        image = f.read()
    if os.path.exists(captcha_path):
        os.remove(captcha_path)
    return ocr.classification(image)

def login(url: str, username: str, password: str, query_key: Union[str, int], query_value: Union[str, int]) -> dict:
    session = get_session()
    timestamp = int(time.time())
    response = session.get(url=f"{url}/manage.php?{query_key}={query_value}", timeout=5)

    result = handle_response(response, "Failed to get initial response")
    if result:
        return result

    cookiesPHPSESSID = response.cookies.get_dict().get("PHPSESSID")
    if not cookiesPHPSESSID:
        return {
            "result": False,
            "message": "Failed to get PHPSESSID",
            "data": []
        }

    cookiesLogin = {
        'QINGZHIFU_PATH': 'qingzhifu',
        'PHPSESSID': cookiesPHPSESSID
    }

    response = session.get(url=f"{url}/manage.php?{query_key}={query_value}", cookies=cookiesLogin, timeout=5)
    result = handle_response(response, "Failed to get response with cookies")
    if result:
        return result

    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form', {'method': 'post'})
    action_value = form.get('action') if form else None
    if not action_value:
        return {
            "result": False,
            "message": "Failed to find form action",
            "data": []
        }

    match = re.search(r'/(\d+)\.html$', action_value)
    number = match.group(1) if match else None
    if not number:
        return {
            "result": False,
            "message": "Failed to extract number from form action",
            "data": []
        }

    captcha_path = fetch_captcha(session, f"{url}/Manage/Index/verify.html", cookiesLogin, timestamp)
    code = solve_captcha(captcha_path)

    if len(code) != 4:
        return {
            "result": False,
            "message": "Invalid captcha code",
            "data": []
        }

    data = {
        "username": username,
        "password": password,
        "yzm": code
    }

    responseLogin = session.post(url=f"{url}/Manage/Index/login/{number}.html", data=data, cookies=cookiesLogin, timeout=5)
    result = handle_response(responseLogin, "Failed to login")
    if result:
        return result

    if responseLogin.cookies:
        cookiesR = responseLogin.cookies.get_dict()
        fx_admin_user_CODE = cookiesR.get("fx_admin_user_CODE")
        save_to_file('fx_admin_user_CODE.txt', fx_admin_user_CODE)
        save_to_file('PHPSESSID.txt', cookiesPHPSESSID)
        return {
            "result": True,
            "message": "success",
            "data": [{
                "fx_admin_user_CODE": fx_admin_user_CODE,
                "PHPSESSID": cookiesPHPSESSID
            }]
        }

    return {
        "result": False,
        "message": "Failed to get login cookies",
        "data": []
    }

def check_login_status(url: str, admin_name: str, admin_id: str) -> dict:
    if not os.path.exists('fx_admin_user_CODE.txt') or not os.path.exists('PHPSESSID.txt'):
        return {
            "result": False,
            "message": "Login information not found",
            "data": []
        }

    fx_admin_user_CODE = read_from_file('fx_admin_user_CODE.txt')
    cookiesPHPSESSID = read_from_file('PHPSESSID.txt')

    cookies = {
        "JSESSIONID": cookiesPHPSESSID,
        'QINGZHIFU_PATH': 'qingzhifu',
        'fx_admin_user_UNAME': admin_name,
        'menudd': '0',
        'fx_admin_user_UID': admin_id,
        'fx_admin_user_CODE': fx_admin_user_CODE
    }

    session = get_session()
    response = session.get(url=f"{url}/manage/main/index.html", cookies=cookies, timeout=5)

    result = handle_response(response, "Failed to check login status")
    if result:
        return result

    if "Cache-Control" in response.headers and response.headers["Cache-Control"] == "private":
        return {
            "result": True,
            "message": "success",
            "data": [{
                "fx_admin_user_CODE": fx_admin_user_CODE,
                "PHPSESSID": cookiesPHPSESSID
            }]
        }

    return {
        "result": False,
        "message": "Login failed, please check your username and password",
        "data": []
    }

def main(url: str, path: str, query: dict, admin_name: str, admin_id: str) -> dict:
    if not os.path.exists('fx_admin_user_CODE.txt') or not os.path.exists('PHPSESSID.txt'):
        return {
            "result": False,
            "message": "Login information not found",
            "data": []
        }

    fx_admin_user_CODE = read_from_file('fx_admin_user_CODE.txt')
    cookiesPHPSESSID = read_from_file('PHPSESSID.txt')

    cookies = {
        "JSESSIONID": cookiesPHPSESSID,
        'QINGZHIFU_PATH': 'qingzhifu',
        'fx_admin_user_UNAME': admin_name,
        'menudd': '0',
        'fx_admin_user_UID': admin_id,
        'fx_admin_user_CODE': fx_admin_user_CODE
    }

    session = get_session()
    response = session.get(url=f"{url}{path}", params=query, cookies=cookies, timeout=5)

    result = handle_response(response, "Failed to get main response")
    if result:
        return result

    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form', {'method': 'post'})
    table = form.find('table', {'class': 'table table-hover'}) if form else None
    tbody = table.find('tbody') if table else None

    if not tbody:
        return {
            "result": False,
            "message": "Failed to find table body",
            "data": []
        }

    data = [[td.text for td in tr.find_all('td')] for tr in tbody.find_all('tr') if tr.find_all('td')]

    data_top = []
    tagtopdiv = soup.find('div', class_='row tagtopdiv')
    if tagtopdiv:
        data_top = [[h4.text.strip() for h4 in div.find('div', class_='panel-body').find_all('h4', class_='pull-left text-danger')]
                    for div in tagtopdiv.find_all('div', class_='panel')]

    data_page = {}
    page_info = soup.find('div', id='wypage')
    if page_info:
        page_info_text = page_info.find('a', class_='number').text.strip()
        match = re.search(r'(\d+) 条记录 (\d+)/(\d+) 页', page_info_text)
        if match:
            record_count, page_number, total_pages = map(int, match.groups())
            data_page = {
                "record_count": record_count,
                "page_number": page_number,
                "total_pages": total_pages
            }

    return {
        "result": True,
        "message": "success",
        "data": data,
        "data_top": data_top,
        "data_page": data_page
    }

def read_cookie(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return file.read()
    return None

def handle_response(response, message):
    if check.type_name(response) == 'NoneType':
        return {
            "result": False,
            "message": message,
            "data": []
        }
    return None

def auto_record_payment(url: str, path: str, query: dict, admin_name: str, admin_id: str, amount: Union[int, float]) -> dict:
    fx_admin_user_CODE = read_cookie('fx_admin_user_CODE.txt')
    cookiesPHPSESSID = read_cookie('PHPSESSID.txt')

    if not fx_admin_user_CODE or not cookiesPHPSESSID:
        return {
            "result": False,
            "message": "Login information not found",
            "data": []
        }

    cookies = {
        "JSESSIONID": cookiesPHPSESSID,
        'QINGZHIFU_PATH': 'qingzhifu',
        'fx_admin_user_UNAME': admin_name,
        'menudd': '0',
        'fx_admin_user_UID': admin_id,
        'fx_admin_user_CODE': fx_admin_user_CODE
    }

    session = requests.Session()

    try:
        response = session.get(url=f"{url}{path}", params=query, cookies=cookies, timeout=10)
        result = handle_response(response, "Failed to get initial response")
        if result:
            return result
    except Exception as e:
        return {
            "result": False,
            "message": f"Error: {e}",
            "data": []
        }

    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find('form', {'method': 'post'})
    if not form:
        return {
            "result": False,
            "message": "Form not found",
            "data": []
        }

    table = form.find('table', {'class': 'table table-hover'})
    if not table:
        return {
            "result": False,
            "message": "Table not found",
            "data": []
        }

    tbody = table.find('tbody')
    if not tbody:
        return {
            "result": False,
            "message": "Table body not found",
            "data": []
        }

    trs = tbody.find_all('a')[4]
    payment_path = trs.get('href').split('=')[-1]

    response = session.get(url=f"{url}{payment_path}", params=query, cookies=cookies, timeout=10)

    soup = BeautifulSoup(response.text, 'html.parser')
    input_tag = soup.find('input', {'name': 'balancestyle'})
    value = input_tag.get('value') if input_tag else 0

    select_tag = soup.find('select', {'name': 'yhk'})
    option_tags = select_tag.find_all('option') if select_tag else []
    second_option_value = option_tags[1].get('value') if len(option_tags) > 1 else 0

    input_tags = soup.find('div', class_='col-md-offset-2 col-md-4').find_all('input')
    data = {input_tag.get('name'): input_tag.get('value') for input_tag in input_tags}

    data.update({
        "balancestyle": value,
        "yhk": second_option_value,
        "status": "1",
        "money": amount
    })

    encoded_data = urllib.parse.urlencode(data)

    try:
        response = session.post(url=f"{url}{payment_path}", data=encoded_data, cookies=cookies, timeout=10, headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
        result = handle_response(response, "Failed to post data")
        if result:
            return result
    except Exception as e:
        return {
            "result": False,
            "message": f"Error: {e}",
            "data": []
        }

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', type='text/javascript')

    if script_tag:
        msg_html = script_tag.string.split("let msg = '")[1].split("';")[0]
        msg_soup = BeautifulSoup(msg_html, 'html.parser')
        p_tag = msg_soup.find('p')
        message = p_tag.text if p_tag else "Success"
        return {
            "result": True,
            "message": "Success",
            "data": [{"msg": message}]
        }

    return {
        "result": True,
        "message": "Success",
        "data": []
    }