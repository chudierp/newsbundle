from django.shortcuts import render

from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key='93ec2510842647889c3913445b754c83')
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge',
                                            category='health',
                                            language='en',
                                            country='us')
    
    all_articles = top_headlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(all_articles)):
        my_articles = all_articles[i]

        news.append(my_articles['title'])
        desc.append(my_articles['description'])
        img.append(my_articles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={'mylist':mylist})