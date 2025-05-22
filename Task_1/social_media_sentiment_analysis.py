from bs4 import BeautifulSoup
from textblob import TextBlob
import csv
import re

# Step 1: Load your CSV file (make sure it's in the same folder as this script)
file_path = "sentimentdataset.csv"

# Step 2: Clean the text
def clean_text(text):
    text = str(text)
    text = BeautifulSoup(text, "html.parser").get_text()  # remove HTML tags
    text = re.sub(r"http\S+|www.\S+", "", text)           # remove URLs
    text = re.sub(r"@\w+", "", text)                      # remove @mentions
    text = re.sub(r"#\w+", "", text)                      # remove hashtags
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)            # remove punctuation
    return text.lower().strip()

# Step 3: Analyze sentiment using TextBlob
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Step 4: Read the file and analyze each row
results = []

with open(file_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row.get("content", "")
        cleaned = clean_text(raw)
        sentiment = get_sentiment(cleaned)
        results.append((cleaned, sentiment))

# Step 5: Show some results
for i, (text, sentiment) in enumerate(results[:10], start=1):
    print(f"{i}. {text}\n   Sentiment: {sentiment}\n")
