from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key = '7e3dd5355ae1494d83ee58dec951eb7e')


def index(response):
    return render(response, 'website/index.html', {})

def science(request):
    top_headlines = newsapi.get_top_headlines(category = 'science', language='en', country='pl')
    return render(request, 'website/science.html', {
        'articles': top_headlines['articles']
})

def business(request):
    top_headlines = newsapi.get_top_headlines(category = 'business', language = 'en', country = 'pl')
    return render(request, 'website/business.html', {
        'articles': top_headlines['articles']
    })

def entertainment(request):
    top_headlines = newsapi.get_top_headlines(category = 'entertainment', language = 'en', country = 'pl')
    return render(request, 'website/entertainment.html', {
        'articles': top_headlines['articles']
    })

def health(request):
    top_headlines = newsapi.get_top_headlines(category = 'health', language = 'en', country = 'pl')
    return render(request, 'website/health.html', {
        'articles': top_headlines['articles']
    })

def sport(request):
    return HttpResponse("Hello world")
