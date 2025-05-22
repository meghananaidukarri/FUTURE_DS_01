import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
import re

# Load dataset
file_path = "sentimentdataset.csv"  # or your absolute path
df = pd.read_csv(file_path)

# Step 1: Clean the text
def clean_text(text):
    text = str(text)
    text = BeautifulSoup(text, "html.parser").get_text()  # remove HTML tags
    text = re.sub(r"http\S+|www.\S+", "", text)           # remove URLs
    text = re.sub(r"@\w+", "", text)                      # remove @mentions
    text = re.sub(r"#\w+", "", text)                      # remove hashtags
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)            # remove special characters
    return text.lower().strip()

df["Cleaned_Text"] = df["Text"].apply(clean_text)

# Step 2: Sentiment analysis using TextBlob
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

df["Calculated_Sentiment"] = df["Cleaned_Text"].apply(get_sentiment)

# Step 3: Save the new data
df.to_csv("cleaned_sentiment_output.csv", index=False)
print("✅ Sentiment analysis complete. Output saved as 'cleaned_sentiment_output.csv'")
