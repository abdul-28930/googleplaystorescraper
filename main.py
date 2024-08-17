# !pip install -q google_play_scraper #scrape
# !pip install -q transformers #sentiment analysis
# !pip install -q plotly-express #for data viz
# !pip install pyyaml
# Run the above commands in google colab at first, in case you're using google colab
# Prefer using google colab for this code as it is a bit heavy and might take time to run on local machine

from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from google_play_scraper import app, reviews_all, Sort
import plotly.express as px
from transformers import pipeline
import re
from io import StringIO

app = Flask(__name__)

def appGoodorBad(appcode):
    match = re.search(r'id=([^&]+)', appcode)
    if match:
        extracted_code = match.group(1)
    else:
        return "App code could not be extracted.", None

    project = reviews_all(extracted_code, sleep_milliseconds=0, lang='en', country='IN', sort=Sort.NEWEST)

    df = pd.json_normalize(project)

    sentiment_analysis = pipeline("sentiment-analysis", model="siebert/sentiment-roberta-large-english")

    df['content'] = df['content'].astype('str')

    df['result'] = df['content'].apply(lambda x: sentiment_analysis(x))

    df['sentiment'] = df['result'].apply(lambda x: (x[0]['label']))
    df['score'] = df['result'].apply(lambda x: (x[0]['score']))

    sentiment_counts = df['sentiment'].value_counts(normalize=True)
    sentiment_text = sentiment_counts.to_frame().to_html()

    fig = px.histogram(df, x='sentiment', color='sentiment', title='Sentiment Analysis', text_auto=True)
    fig_html = fig.to_html(full_html=False)

    return sentiment_text, fig_html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    appcode = request.form['appcode']
    sentiment_text, fig_html = appGoodorBad(appcode)
    return render_template('result.html', sentiment_text=sentiment_text, fig_html=fig_html)

if __name__ == '__main__':
    app.run(debug=True)
