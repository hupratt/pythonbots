from django.http import JsonResponse
import json
# Create your views here.
from .reddit_api import get_articles_comments
from .bayes.bayes import reddit_classify
from django.http import HttpResponse


def get_classification(request):
    """
    Top 5 on reddit method

    """
    if request.method == 'POST':
        # transform the incoming byte string into a dictionary object, classical request.POST.get and request.POST only works with form data
        # string = request.POST.get('content',"key not found in the dictionary")
        dic = json.loads(request.body.decode('utf8'))
        red = reddit_classify(dic['content'])
        print("\n\n")
        print(red)      
        print("\n\n")
        return JsonResponse(red)
    return HttpResponse("<p>"+"string"+"</p>")

def get_reddit_article(request):
    """
    Top 5 on reddit method
    
    """
    dic = get_articles_comments(subred="technology", time='week', lim=5, top=True)
    return JsonResponse(dic)