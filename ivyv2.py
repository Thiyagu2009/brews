import streamlit as st
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import pandas as pd

nltk.download('vader_lexicon')


def analyze_sentiment(message):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(message)
    sentiment_score = sentiment_scores.get('compound', 0.0)

    return sentiment_score


def categorize_messages(messages):
    data = {'timestamp': [], 'sender': [], 'text': [], 'sentiment_score': [], 'sentiment_score_group': []}
    pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')

    for message in messages:
        match = pattern.match(message)

        if match:
            timestamp, sender, text = match.group(1), match.group(2), match.group(3)
            sentiment_score = analyze_sentiment(text)
            sentiment_group = 'positive' if sentiment_score >= 0.05 else (
                'negative' if sentiment_score <= -0.05 else 'neutral')

            data['timestamp'].append(timestamp)
            data['sender'].append(sender)
            data['text'].append(text)
            data['sentiment_score'].append(sentiment_score)
            data['sentiment_score_group'].append(sentiment_group)

    df = pd.DataFrame(data)
    return df


def main():
    st.title("IVY Analytics WhatsApp Sentiment Analyzer")

    uploaded_file = st.file_uploader("Upload a WhatsApp chat file", type=["txt"])

    if uploaded_file is not None:
        # Read the content of the uploaded file
        chat_content = uploaded_file.read().decode('utf-8').splitlines()

        df = categorize_messages(chat_content)

        st.header("Messages:")
        st.dataframe(df)  # Use st.dataframe instead of st.table

        st.header("Sentiment Scores Distribution:")
        fig = px.histogram(df, x='sentiment_score', nbins=30, title='Sentiment Scores Distribution',
                           labels={'sentiment_score': 'Sentiment Score'},
                           color_discrete_map={'negative': 'red', 'positive': 'green', 'neutral': 'orange'},
                           color='sentiment_score_group'
                           )

        fig.update_layout(showlegend=False)  # Hide the legend
        st.plotly_chart(fig)


if __name__ == "__main__":
    main()
