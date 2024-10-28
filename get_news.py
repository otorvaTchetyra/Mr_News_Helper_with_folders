import requests

def get_news(topic, from_date, to_date, language='ru', api_key='9e3c2104624d4b8982ba5bb8908aded3'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=publishedAt&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = {}
    for article in articles:
        results[article['title']] = article['description']
    return results

res = get_news(topic='space', from_date='2024-10-22', to_date='2024-10-23')
for title, description in res.items():
    print(f"TITLE: {title}\nDESCRIPTION: {description}")

# Here I used API key from Newsapi.org because I wanted to create an assist to it shows last news from 'evrything'. 
# I tryed follow the instructions. I could complete the task using Rust and Cargo,-> 
# -> but I don't have expirience to use their and Decided to avoid it.











