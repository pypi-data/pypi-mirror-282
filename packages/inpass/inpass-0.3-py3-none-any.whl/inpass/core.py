import requests
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A5341f Safari/604.1',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
]

def login(username, password):
    session = requests.Session()
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    initial_response = session.get('https://www.instagram.com/')
    csrf_token = initial_response.cookies['csrftoken']
    user_agent = random.choice(user_agents)
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }
    headers = {
        'X-CSRFToken': csrf_token,
        'User-Agent': user_agent,
        'Referer': 'https://www.instagram.com/accounts/login/'
    }
    login_response = session.post(login_url, data=payload, headers=headers)
    if login_response.status_code == 200 and login_response.json().get('authenticated'):
        return True
    else:
        return False
