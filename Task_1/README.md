# Social Media Trend Analysis

This project analyzes trending topics and user sentiment from Twitter, Instagram, and LinkedIn. It helps understand what people are talking about online and how they feel about those topics. The insights are visualized using Power BI.

## 🎯 What This Project Does
- Collects posts from Twitter and Instagram, and uses sample data for LinkedIn
- Identifies trending topics and hashtags
- Analyzes how people feel (positive, negative, neutral) about those topics
- Visualizes everything in a clear dashboard

## 🛠 Tools Used
- **Python**: Tweepy, Instaloader, TextBlob, Pandas, Matplotlib
- **Power BI**: To build the dashboard
- **Jupyter Notebook**: For coding and analysis

## 📁 Files in This Project
- `twitter_analysis.ipynb` – Collects tweets, analyzes trends & sentiment
- `instagram_analysis.ipynb` – Scrapes public Instagram posts & analyzes sentiment
- `linkedin_analysis.ipynb` – Uses sample data for LinkedIn trend and sentiment analysis
- `twitter_sentiment.csv` – Processed Twitter data
- `instagram_sentiment.csv` – Processed Instagram data
- `linkedin_sample.csv` – Sample LinkedIn post data
- `dashboard.pbix` – Power BI dashboard file
- `dashboard.png` – Screenshot of the dashboard

## 🚀 How to Use
1. Clone the repo
2. Add your Twitter API keys in `twitter_analysis.ipynb`
3. Run all three notebooks to generate the sentiment datasets
4. Open `dashboard.pbix` in Power BI to view the insights

## 📊 Final Output
- Sentiment trends across all three platforms
- Top hashtags and topics people are discussing
- Visual comparisons of user sentiment in Power BI
