import feedparser

# List of RSS feed URLs
rss_urls = [
    'https://feeds.content.dowjones.io/public/rss/mw_topstories',
    'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
    'https://www.cnbc.com/id/100003114/device/rss/rss.html'
    # Add more RSS feed URLs here
]

# Initialize a list to store articles
all_articles = []

# Loop through each RSS feed
for rss_url in rss_urls:
    # Parse the feed
    feed = feedparser.parse(rss_url)
    
    # Extract and append articles to the list
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'summary': entry.summary,
            'link': entry.link,
            'published': entry.published
        }
        all_articles.append(article)

# Display the fetched articles
for article in all_articles:
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary']}")
    print(f"Link: {article['link']}")
    print(f"Published: {article['published']}")
    print("\n---\n")
