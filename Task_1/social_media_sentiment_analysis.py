from bs4 import BeautifulSoup
from textblob import TextBlob
import csv
import re

# Step 1: Load your CSV file
file_path = "sentimentdataset.csv"

# Step 2: Clean the text (LESS aggressive)
def clean_text(text):
    text = str(text)
    text = BeautifulSoup(text, "html.parser").get_text()  # Remove HTML
    text = re.sub(r"http\S+|www.\S+", "", text)           # Remove URLs
    text = re.sub(r"@\w+", "", text)                      # Remove mentions
    text = re.sub(r"#", "", text)                         # Remove only '#' symbol, not words
    return text.strip()

# Step 3: Analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"

# Step 4: Process file
results = []
with open(file_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row.get("content", "")
        cleaned = clean_text(raw)
        sentiment = get_sentiment(cleaned)
        results.append((cleaned, sentiment))

# Step 5: Export to new CSV
import pandas as pd
df = pd.DataFrame(results, columns=["Cleaned_Text", "Sentiment"])
df.to_csv("cleaned_sentiment_output.csv", index=False)

# Step 6: Preview sample
print(df.head(10))
