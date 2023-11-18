# Secure Notepad Web Application

<img src="https://th.bing.com/th/id/OIG.Ugk9hKHmoYMrh_T1s5g8?w=1024&h=1024&rs=1&pid=ImgDetMain" width="300" height="300" style="display: block; margin: auto;">

## Description

The Secure Notepad Web Application is a robust and secure platform designed for managing and organizing notes online. Built on the Flask framework and utilizing Conda for dependency management, this application provides a feature-rich experience with a strong emphasis on user security.

## Features

### User Management

- **User Registration and Login:** New users can register for an account, and existing users can log in securely.

### Note Management

- **Create and Customize Notes:** Users can create and customize their notes with a diverse range of styling options.

- **Note Deletion:** The application allows users to delete unnecessary notes.

- **Public Sharing:** Users can share selected notes publicly, complete with date and author details.


### Security Measures Implemented

- **IP Address Checking:** The system includes a feature for checking and verifying IP addresses.

- **Protection Against Injection Attacks:** The application is fortified against injection attacks to ensure the integrity of user data.

- **Secure Password Storage:** Passwords are securely stored to prevent unauthorized access.

- **Password Strength Evaluation:** The application assesses and enforces password strength for user accounts.

- **Brute-Force Protection:** The system blocks attempts to crack passwords through brute-force attacks.

- **Communication Encryption:** Server-client communication is encrypted to safeguard sensitive information.

- **Self-Signed Certificate:** The application uses a self-signed certificate to enhance communication security.

- **Registration Data Validation:** Data entered during registration is rigorously validated to ensure its quality and accuracy.

- **Cookie Security:** The application implements security measures to ensure the safe handling of cookies.

## Used libraries

1. **Flask==0.11.1:**
   - **Flask** is a lightweight web framework for Python. It's designed to be simple and easy to use, providing the essentials for building web applications. Flask is known for its flexibility and is often used for small to medium-sized projects.

2. **gunicorn==19.6.0:**
   - **Gunicorn (Green Unicorn)** is a WSGI HTTP server for running Python web applications. It's widely used for deploying Flask applications in production environments. Gunicorn can handle multiple requests concurrently and is known for its performance and reliability.

3. **Jinja2==2.8:**
   - **Jinja2** is a modern and designer-friendly templating engine for Python. It is used with Flask to dynamically generate HTML pages. Jinja2 allows embedding Python-like expressions and statements in templates, making it easy to build dynamic web pages.

4. **MarkupSafe==0.23:**
   - **MarkupSafe** is a library that provides a simple API for escaping and unescaping strings to be included in HTML, XML, JSON, or other markup languages. It helps prevent cross-site scripting (XSS) attacks by ensuring that user-generated content is properly escaped before rendering.

5. **SQLAlchemy==1.4:**
   - **SQLAlchemy** is a SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of high-level API for interacting with relational databases. SQLAlchemy simplifies database operations by allowing developers to work with database tables and queries using Python objects.

6. **bleach==4.1.0:**
   - **Bleach** is a library for sanitizing and cleaning HTML input. It helps prevent Cross-Site Scripting (XSS) attacks by removing potentially harmful HTML and script tags from user-generated content. In the context of web applications, it is often used to sanitize input before displaying it on a webpage.

7. **password-strength==0.0.3.post2:**
   - **password-strength** is a Python library for evaluating and enforcing password strength. It allows developers to define and enforce password policies, including complexity requirements such as length, character types, and uniqueness. This helps enhance the security of user accounts by encouraging the use of strong passwords.

8. **Flask-Login==0.5.0:**
   - **Flask-Login** is an extension for Flask that simplifies the management of user sessions and authentication. It provides functionality for user login, session management, and protection of routes that require authentication. Flask-Login integrates well with Flask applications and is commonly used for user authentication in web applications.

## Getting Started

Install dependencies from requirements file.

## Useful commands

1. **`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`**:
   - `wget` is a command-line utility for downloading files from the web.
   - Downloads the latest Miniconda installer script for Linux x86_64 from the Anaconda repository.

2. **`bash Miniconda3-latest-Linux-x86_64.sh`**:
   - `bash` is used to execute the Miniconda installer script.
   - Installs Miniconda, a minimal installer for Conda (a package manager and environment manager).

3. **`wsl --shutdown`**:
   - Shuts down the WSL instance, likely to ensure that the changes made by the Miniconda installation take effect.

4. **`conda update conda`**:
   - Updates the Conda package manager to the latest version.

5. **`conda env export > bezpieczna_aplikacja.yml`**:
   - Activates the base Conda environment and exports its configuration to a YAML file named `bezpieczna_aplikacja.yml`.
   - This file will likely contain a list of all installed packages and their versions, allowing someone else to recreate the exact environment.

6. **`gunicorn --bind 0.0.0.0:5000 connector:app`**:
   - Starts Gunicorn, a WSGI HTTP server for running Python web applications.
   - Binds Gunicorn to listen on all available network interfaces (`0.0.0.0`) on port 5000.
   - `connector:app` specifies the location of the Flask application object (`app`), assuming it's defined in a file named `connector`.


1. **`sudo systemctl daemon-reload`**:
   - Reloads the systemd manager configuration. This is necessary after making changes to systemd unit files.

2. **`sudo systemctl restart myapp`**:
   - Restarts the "myapp" service managed by systemd. This assumes there is a systemd service unit file named `myapp.service` defining the configuration for the "myapp" application.

3. **`sudo systemctl restart nginx`**:
   - Restarts the Nginx web server. This is often done after making changes to Nginx configuration files to apply the changes.

4. **`sudo nano /etc/nginx/sites-available/myapp`**:
   - Opens the Nginx configuration file for the "myapp" site in the nano text editor. The configuration file likely contains settings for the Nginx server related to the "myapp" application.

5. **`sudo nano /etc/systemd/system/myapp.service`**:
   - Opens the systemd service unit file for the "myapp" application in the nano text editor. This file defines how the "myapp" service should be managed by systemd, including details such as the command to start the service, dependencies, etc.

6. **`ls /etc/nginx/sites-enabled/`**:
   - Lists the files in the Nginx "sites-enabled" directory. This directory typically contains symbolic links to the configuration files in "sites-available" that are currently active and being used by Nginx.

7. **`journalctl -xe`**:
   - Displays the journal (system logs) using `journalctl` with extended information (`-xe`). This can be helpful for troubleshooting issues with the application or server.

8. **`https://localhost/login`**:
   - Assumes that the "myapp" application is accessible via HTTPS at `https://localhost/login`. This is the login page for the application.


## Usage

Once the installation is complete, access the application at `https://localhost/login`. Enjoy the secure and feature-rich notepad experience!

## Contributing

Contributions to the project are encouraged. To contribute, follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your branch to your fork.
5. Create a pull request.
