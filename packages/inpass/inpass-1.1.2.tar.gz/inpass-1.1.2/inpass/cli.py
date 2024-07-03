import argparse
import inpass

def main():
    parser = argparse.ArgumentParser(description="Login to Instagram and track URL changes.")
    parser.add_argument('--username', required=True, help="Your Instagram username")
    parser.add_argument('--password-file', required=True, help="File containing passwords to try")
    
    args = parser.parse_args()
    
    inpass.track_url_change(args.username, args.password_file)

if __name__ == '__main__':
    main()
