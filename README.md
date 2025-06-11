Login Brute-Force Tool
Overview
This Python script is a simple brute-force login tool designed for educational purposes. It attempts to log into a specified web login page by trying different passwords from a provided password file. The tool supports both POST and GET HTTP request methods and allows optional cookie input to bypass certain restrictions. This tool is intended for authorized security testing only.
⚠️ Warning: Unauthorized use of this tool against systems you do not own or have explicit permission to test is illegal and unethical. Always obtain explicit consent before performing security testing.
Features

Supports HTTP POST and GET requests.
Allows optional cookie input for session-based authentication.
Reads passwords from a user-provided text file.
Detects login failures based on a user-specified failure string.
Color-coded output (green for success, red for failures) in supported terminals.
Handles common errors (e.g., file not found, network issues).

Prerequisites

Python 3.x
requests library (pip install requests)
A text file containing passwords (one per line, UTF-8 encoded)
A terminal that supports ANSI color codes (optional, for colored output)

Installation

Clone the repository:
git clone https://github.com/ChetanyaGarg/bruteforce_py.git


Install the required Python library:
pip install requests



Usage

Run the script:
python bruteforce.py


Follow the prompts to enter:

The login page URL (e.g., https://example.com/login)
The username to test
The path to your password file
The text displayed on failed login attempts (e.g., "Invalid credentials")
The HTTP request type (1 for POST, 2 for GET)
An optional cookie value (press Enter to skip)


The script will attempt to log in with each password and display the results:

Green output indicates a successful login.
Red output indicates failures or errors.


If a valid password is found, the script stops and displays the credentials. Otherwise, it completes the password list and reports no success.


Example
=== Login Brute-Force Tool ===
Enter the login page URL (e.g., https://example.com/login): https://example.com/login
Enter the username to test: admin
Enter the path to your password file: passwords.txt
Enter the text shown when login fails (e.g., 'Invalid credentials'): Invalid credentials
Select HTTP request type:
1. POST
2. GET
Enter the number for request type (1 or 2): 1
Enter value of Cookie (optional, press Enter to skip): session=abc123

Starting brute-force for username 'admin'...
Total passwords to try: 100
Request type: POST
Using Cookie: session=abc123
----------------------------------------
Trying password 1/100: password123
  ↳ Failed
Trying password 2/100: admin123
✅ Success! Valid credentials found:
Username: admin
Password: admin123
Cookie: session=abc123
----------------------------------------

Ethical Use

Only use this tool on systems you own or have explicit permission to test.
Unauthorized brute-forcing is illegal and can lead to severe consequences.
This tool is for educational purposes, such as learning about security vulnerabilities or testing your own systems.

Disclaimer
The author is not responsible for any misuse of this tool. Use it responsibly and in compliance with all applicable laws and regulations. Ensure you have explicit permission from the system owner before testing.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements or bugs.
Contact
For questions or feedback, open an issue on this repository or contact [your-contact-info].
