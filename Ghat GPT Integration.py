import openai
import pandas as pd
from pytrends.request import TrendReq

# Get top chart keyword
pytrend = TrendReq()
top_charts_df = pytrend.top_charts(2022, hl='en-US', geo='GLOBAL')
top_keyword = top_charts_df.iloc[0]['title']

def generate_article():
    # Set up OpenAI API credentials
    openai.api_key = "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"


    # Generate article
    prompt = f"Write an article about the word '{top_keyword}' in 500-1500 words with long tail keywords at the end."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    article_text = response.choices[0].text.strip()

    # Save article title and body to separate variables
    tt = f"'{top_keyword}'"
    bb = article_text

    return tt, bb

# Generate the article and save the title and body to separate variables
title, body = generate_article()

# Print the title and body
print(title)
print(body)
