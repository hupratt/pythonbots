import praw, unicodedata, datetime
# from .bayes.bayes import reddit_classify


username = 'cortohprattdo'
userAgent = "MyApp/0.1 by " + username
clientId = 'SY_YQNuqfZkeSQ'
clientSecret = "r7FrGfvLcV-YnMWkm9mbYw5B8Dc"


def remove_accented_chars(text):
    if type(text) == str:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def get_date(submission):
    time = submission.created
    time = datetime.datetime.fromtimestamp(time)
    return time.strftime("%A %dth of %B, %Y")

def get_articles_comments(subred, lim, top=False, hot=False, time=None):
    reddit = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)
    subreddit = reddit.subreddit(subred)
    subreddit_ = remove_accented_chars(subreddit.title) # or display_name
    i = 0
    # print(top,hot)
    if top is True:
        dic={'subreddit':subreddit_}
        for article in subreddit.top(time_filter='week', limit=lim):
            article_dict = {}
            comment_dict = {}
            i+=1
            title_ = remove_accented_chars(article.title)
            all_comments = article.comments.list()
            j = 0
            for top_level_comment in all_comments:
                try:
                    comment_ = remove_accented_chars(top_level_comment.body)
                    url = "http://www.reddit.com" + top_level_comment.permalink
                    comment_dict[j] = {"comment":comment_, "comment_url":url}
                    j+=1
                except AttributeError:
                    pass
            article_dict['date'] = get_date(article)
            article_dict['title'] = title_
            article_dict['comments'] = comment_dict
            article_dict['score'] = article.score
            article_dict['article_url'] = article.url
            dic[i]=article_dict
    elif hot is True:
        dic={'subreddit':subreddit_}
        for article in subreddit.hot(limit=lim):
            article_dict = {}
            comment_dict = {}
            i+=1
            title_ = remove_accented_chars(article.title)
            all_comments = article.comments.list()
            j = 0
            for top_level_comment in all_comments:
                try:
                    comment_ = remove_accented_chars(top_level_comment.body)
                    url = "http://www.reddit.com" + top_level_comment.permalink
                    comment_dict[j] = {"comment":comment_, "comment_url":url}
                except AttributeError:
                    pass
            article_dict['date'] = get_date(article)
            article_dict['title'] = title_
            article_dict['comments'] = comment_dict
            article_dict['score'] = article.score
            article_dict['article_url'] = article.url
            dic[i]=article_dict
    else:
        raise Exception('Either top or hot boolean needs to be defined')
    return dic


# dic = get_articles_comments(subred="technology", time='week', lim=1, top=True)