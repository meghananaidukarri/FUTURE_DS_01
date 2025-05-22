import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data pools
usernames = ["alice", "bob", "charlie", "david", "emma", "frank"]
platforms = ["Twitter", "Instagram", "LinkedIn"]
hashtags_pool = ["#AI", "#Tech", "#Startup", "#Coding", "#Python", "#ML"]
positive_phrases = ["I love using AI tools", "Python makes life easier", "Excited about the future of tech"]
negative_phrases = ["I hate the new update", "Tech is ruining everything", "Not happy with the service"]
neutral_phrases = ["Just read an article", "Using the platform", "Attended a webinar today"]

# Generate random posts
def generate_post():
    sentiment = random.choice(["Positive", "Negative", "Neutral"])
    if sentiment == "Positive":
        text = random.choice(positive_phrases)
    elif sentiment == "Negative":
        text = random.choice(negative_phrases)
    else:
        text = random.choice(neutral_phrases)

    post = {
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S"),
        "username": random.choice(usernames),
        "content": text,
        "platform": random.choice(platforms),
        "hashtags": random.choice(hashtags_pool),
        "likes": random.randint(0, 1000),
        "shares": random.randint(0, 500),
        "sentiment": sentiment
    }
    return post

# Create a DataFrame of fake data
data = [generate_post() for _ in range(100)]
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("generated_sentimentdataset.csv", index=False)
print("✅ Sample dataset created: generated_sentimentdataset.csv")
