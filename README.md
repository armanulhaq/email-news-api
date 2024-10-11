# News Email Notification Script

## Description
The News Email Notification Script is a Python application that retrieves the latest technology news headlines from the News API and sends them via email. It connects to Gmail's SMTP server to send an email containing the top articles, including their titles, descriptions, and URLs.

## Features
- Fetches top technology news headlines from TechCrunch.
- Compiles article titles and descriptions into an email body.
- Sends the compiled news via email using Gmail's SMTP server.

## Technologies Used
- Python
- smtplib
- requests
- SSL for secure email transmission

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/armanulhaq/news-email-news-api.git
   cd news-email-notification
```  
2. Create a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:
```bash
pip install requests
```
4. Set up your email credentials in the script:
```bash
username = "your_email@gmail.com"
password = "your_email_password"
```
5. Replace the api_key in the script with your own News API key:
```bash
api_key = "your_news_api_key"
```
6. Run the script:
```bash
python script.py
```
