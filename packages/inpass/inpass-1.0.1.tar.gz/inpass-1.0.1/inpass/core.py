import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

def login(username, password):
    max_attempts = 3
    attempt_delay = 12  # seconds to wait before retrying

    session = requests.Session()
    login_url = "https://www.instagram.com/accounts/login/ajax/"

    for attempt in range(max_attempts):
        try:
            initial_response = session.get('https://www.instagram.com/')
            
            if initial_response.status_code != 200:
                logging.error('Failed to load Instagram login page.')
                return False
            
            csrf_token = initial_response.cookies.get('csrftoken')
            if not csrf_token:
                logging.error('Failed to retrieve CSRF token.')
                return False
            
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
            
            if login_response.status_code != 200:
                logging.error('Failed to submit login form.')
                return False
            
            response_json = login_response.json()
            if response_json.get('authenticated'):
                logging.info('Login successful.')
                return True
            elif response_json.get('message') == 'checkpoint_required':
                logging.warning('Checkpoint required (likely CAPTCHA). Waiting for manual intervention...')
                handle_captcha(session)
                continue
            else:
                logging.info('Login failed.')
                return False

        except Exception as e:
            logging.error(f'An error occurred: {e}')
            return False
        
        time.sleep(attempt_delay)
    
    logging.error(f'Reached maximum login attempts ({max_attempts}). Please try again later.')
    return False

def handle_captcha(session):
    logging.warning('CAPTCHA detected. Please solve the CAPTCHA in the browser and press Enter to continue...')
    input('Press Enter to continue after solving the CAPTCHA...')
