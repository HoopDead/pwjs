from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
from .forms import api_request_query
from django.shortcuts import redirect
from django.core.paginator import Paginator
import math as m


newsapi = NewsApiClient(api_key = 'b0307aaaee13449f8a2e6b100a862b08')


def index(request):
    form = api_request_query()
    if request.method == "GET":
        form = api_request_query(request.GET)
        if form.is_valid():
            page = 1
            page = int(request.GET.get('page'))
            query = request.GET.get('query')
            if page == 1:
                pages = {'1': 1, '2': 2, '3': 3}
            elif page > 1:
                pages = {'1': page-1, '2': page, '3': page+1}
            print(pages)
            all_articles = newsapi.get_everything(q = query, page = int(page), page_size = 25, language = 'en', sort_by = 'relevancy')
            num_of_pages = m.ceil(all_articles['totalResults']/25)
            return render(request, 'website/index.html', {'form': form, 'all_articles': all_articles, 'pages': pages, 'query': query, 'page': page})
    return render(request, 'website/index.html', {'form': form})

def science(request):
    top_headlines = newsapi.get_top_headlines(category = 'science', language='en', country = 'us')
    return render(request, 'website/science.html', {
        'articles': top_headlines['articles']
})

def business(request):
    top_headlines = newsapi.get_top_headlines(category = 'business', language = 'en', country = 'us')
    return render(request, 'website/business.html', {
        'articles': top_headlines['articles']
    })

def entertainment(request):
    top_headlines = newsapi.get_top_headlines(category = 'entertainment', language = 'en', country = 'us')
    return render(request, 'website/entertainment.html', {
        'articles': top_headlines['articles']
    })

def health(request):
    top_headlines = newsapi.get_top_headlines(category = 'health', language = 'en', country = 'us')
    return render(request, 'website/health.html', {
        'articles': top_headlines['articles']
    })

def sport(request):
    top_headlines = newsapi.get_top_headlines(category = 'sports', language = 'en', country = 'us')
    return render(request, 'website/sport.html', {
        'articles': top_headlines['articles']
    })

def technology(request):
    top_headlines = newsapi.get_top_headlines(category = 'technology', language = 'en', country = 'us')
    return render(request, 'website/technology.html', {
        'articles': top_headlines['articles']
    })
