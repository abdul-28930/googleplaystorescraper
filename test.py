# !pip install -q google_play_scraper #scrape
# !pip install -q transformers #sentiment analysis
# !pip install -q plotly-express #for data viz
# !pip install pyyaml
# Run the above commands in google colab at first, in case you're using google colab
# Prefer using google colab for this code as it is a bit heavy and might take time to run on local machine

import pandas as pd
import numpy as np
from google_play_scraper import app, reviews_all, Sort
import plotly.express as px
from transformers import pipeline
import re
from gradio_client import Client
import gradio as gr

def appGoodorBad():
    appcode = input("Enter app link: ")
    match = re.search(r'id=([^&]+)', appcode)
    if match:
        extracted_code = match.group(1)
        print(f"Extracted app code: {extracted_code}")
    else:
        print("App code could not be extracted.")
        
    project = reviews_all(extracted_code, sleep_milliseconds=0, lang = 'en', country = 'IN', sort=Sort.NEWEST)
    
    df = pd.json_normalize(project)
    
    sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

    df['content'] = df['content'].astype('str')

    df['result'] = df['content'].apply(lambda x: sentiment_analysis(x))

    df['sentiment'] = df['result'].apply(lambda x: (x[0]['label']))
    df['score'] = df['result'].apply(lambda x: (x[0]['score']))

    df['sentiment'].value_counts(normalize=True)

    fig = px.histogram(df, x='sentiment', color='sentiment', title='Sentiment Analysis', text_auto=True)
    fig.show()

appGoodorBad()

