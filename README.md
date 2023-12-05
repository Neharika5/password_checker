# password_checker
mini project 
Password Checker
This Python script checks whether a password has been compromised or appeared in known data breaches using the Have I Been Pwned API.

Overview
The script takes a password as input and checks if it has been previously exposed in known data breaches. It uses the SHA-1 hash of the password to securely search the database of breached passwords without transmitting the actual password.

Features
Check Passwords: You can input passwords in various ways:
Provide a file containing passwords.
Manually enter passwords through the command line.
Pass passwords as command-line arguments.
Secure: The script hashes the passwords before querying the Have I Been Pwned API, ensuring that the actual passwords are not transmitted.
Informative: Informs whether the password has been seen before and advises whether it's prudent to change the password.
Prerequisites
Python 3.x installed.
Required Python modules: requests
