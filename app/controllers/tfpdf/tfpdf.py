# import models
from ...models import News, Vocabulary, Cluster, Time_Period, Cluster_Time_Period, Cluster_News, Website
import math
websites=[]
time_period = {}

def website_index():
    website_objects = Website.objects.all()
    news_objects = News.objects.all()
    for news in news_objects:
        if (news.website_id is None):
            for website in website_objects:
                if (website.name in news.url):
                    news.website_id = website.id
                    news.save()
                    break
    for website in website_objects:
        query = 'SELECT * FROM app_news as n JOIN app_cluster_news as cn ON n.id = cn.news_id JOIN app_cluster_time_period as ctp ON cn.cluster_id = ctp.cluster_id where ctp.time_period_id = 2 AND n.website_id = ' + str(website.id)
        news_objects_of_website = News.objects.raw(query)
        this_website={}
        this_website['id'] = website.id
        this_website['number_of_news'] = len(list(news_objects_of_website))
        this_website['weight'] = website.weight
        sumW=0.0
        for cluster in Cluster.objects.filter(cluster_time_period__time_period_id = time_period.id):
            news_objects_of_cluster = News.objects.filter(cluster_news__cluster_id = cluster.id, website_id = website.id)
            Dcs = len(news_objects_of_cluster)
            sumW +=Dcs**2 + 0.0
        this_website['sumW'] = sumW
        websites.append(this_website)


def ranking_topic(fromDate, toDate):
    global time_period
    time_period = Time_Period.objects.filter(fromDate=fromDate, toDate=toDate).first()
    website_index()

    # define hot topics on each cluster
    cluster_objects = Cluster.objects.filter(cluster_time_period__time_period_id=time_period.id)
    # cluster_time_period = Cluster_Time_Period.objects.filter(time_period_id=time_period.id).values()
    print ("number clusters " + str(len(cluster_objects)))
    for cluster in cluster_objects:
        tfpdf(cluster)

def tfpdf(cluster):
    jt=0.0
    website_objects = Website.objects.all()
    for website in websites:
        # Djs là số lượng document thuộc topic j trên website s
        news_objects_of_cluster = News.objects.filter(cluster_news__cluster_id = cluster.id, website_id = website['id'])
        Djs = len(news_objects_of_cluster)
        # Ns la so luong bai bao cua website s
        Ns = website['number_of_news']

        # jt la do hot
        jt += normF(Djs, website) * math.exp(Djs/Ns) * float(website['weight'])
    print('Hot level of topic ' + str(cluster.id) + ' is ' + str(jt))


def normF(Djs, website):
    # global sumW
    # if (not sumW):
    return Djs / math.sqrt(website['sumW'])
