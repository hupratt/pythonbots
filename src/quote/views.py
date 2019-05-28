from django.http import JsonResponse
import sys, json, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup



def quote_json(request):
    """
    Random Movie quote method

    """
    context = get_quote()
    return JsonResponse(context)

def famous_quote_json(request):
    """
    Random Famous quote method

    """
    context = get_quote_famous()
    return JsonResponse(context)

def get_picture_url(query):
    """
    Random Movie quote method

    """
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu') 
    options.add_argument('--no-sandbox')

    url="https://www.google.com/search?q="+query+" movie poster&source=lnms&tbm=isch"
    if (sys.platform == "win32"):
        driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe', chrome_options=options)
    else:
        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    im=[] # contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"] ,json.loads(a.text)["ity"]
        im.append((link,Type))
        break
    url = im[0][0]
    return url

def get_quote(*args):
    """
    Random Movie quote method

    """
    response = requests.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=1",
      headers={
        "X-Mashape-Key": "ZbCv9zWnbjmshR6al0Uoj6MDsGe1p1gaGH7jsnsa6RxFVQSZcI",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }
    )
    print(type(response.json()))
    dic = {}
    for i, res in enumerate(response.json()):
        url = get_picture_url(res['author'])
        res['picture_url'] = url
        dic[i] = res
    # for key, value in dic.items():
    #     print(value['0'])

    return dic

def get_quote_famous(*args):
    """
    Random Famous quote method

    """
    response = requests.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
      headers={
        "X-Mashape-Key": "ZbCv9zWnbjmshR6al0Uoj6MDsGe1p1gaGH7jsnsa6RxFVQSZcI",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
      }
    )
    print(type(response.json()))
    dic = {}
    for i, res in enumerate(response.json()):
        # url = get_picture_url(res['author'])
        # res['picture_url'] = url
        dic[i] = res
    # for key, value in dic.items():
    #     print(value['0'])
    return dic