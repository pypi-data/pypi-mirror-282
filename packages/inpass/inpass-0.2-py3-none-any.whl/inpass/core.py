import requests

def login(username, password):
    session = requests.Session()
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    initial_response = session.get('https://www.instagram.com/')
    csrf_token = initial_response.cookies['csrftoken']
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    headers = {
        'X-CSRFToken': csrf_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.instagram.com/accounts/login/'
    }
    login_response = session.post(login_url, data=payload, headers=headers)
    if login_response.status_code == 200 and login_response.json().get('authenticated'):
        return True
    else:
        return False
