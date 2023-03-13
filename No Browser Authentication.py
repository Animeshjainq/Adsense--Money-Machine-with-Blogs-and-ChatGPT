import openai
import pandas as pd
from pytrends.request import TrendReq
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import json
import datetime

# Set up service account credentials
SCOPES = ['https://www.googleapis.com/auth/blogger']
creds = service_account.Credentials.from_service_account_file(
    'C:\\Users\\anime\\OneDrive\\Desktop\\client_secret.json',
    scopes=SCOPES
)

# Set up OpenAI API credentials
openai.api_key = "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"

# Get top chart keywords
pytrend = TrendReq()
top_charts_df = pytrend.top_charts(2021, hl='en-US', geo='GLOBAL')
top_keywords = top_charts_df['title'].tolist()[:9]

for top_keyword in top_keywords:
    # Generate article
    prompt = f"Write an article about the word '{top_keyword}' in 500-1500 words with long tail keywords at the end."
    data = {
        "prompt": prompt,
        "model": "text-davinci-002",
        "max_tokens": 1000,
        "n": 1,
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/completions", headers={"Authorization": f"Bearer {openai.api_key}"}, json=data)
    article_text = response.json()["choices"][0]["text"].strip()

    # Save article title and body to separate variables
    tt = f"{top_keyword}"
    bb = article_text

    # Create the blog post
    blog_post = {
        'kind': 'blogger#post',
        'title': tt,
        'content': bb,
        'labels': [top_keyword],
        'published': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-08:00')
    }

    try:
        # Insert the blog post
        url = f"https://www.googleapis.com/blogger/v3/blogs/1285296339281754534/posts?key=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"
        headers = {"Authorization": f"Bearer {creds.token}"}
        response = requests.post(url, headers=headers, json=blog_post)
        insert_result = json.loads(response.text)
        print(f"Blog post with ID {insert_result['id']} published successfully.")
    except Exception as error:
        print(f"An error occurred: {error}")
