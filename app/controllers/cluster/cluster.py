# os library
import time

# import models
from ...models import News, Vocabulary, Cluster, Time_Period, Cluster_Time_Period, Cluster_News
from ..tfidf import tfidf

#Calc tfidf and cosine similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clustering(fromDate, toDate):
    # threshold of cosine similarity
    threshold = 0.2

    # get cluster
    time_period_object = Time_Period.objects.filter(fromDate=fromDate, toDate=toDate).first()

    # create if not exist
    if(not time_period_object):
        time_period_object = Time_Period.objects.create(fromDate=fromDate, toDate=toDate)


    # get all news between fromDate and toDate
    news_objects = News.objects.filter(date__range=(fromDate, toDate))

    # clusters
    clusters_list = []

    # calc tfidf of news objects
    tfidf_matrix = tfidf.execute_tfidf(news_objects)

    # find the max similarity with all documents of clusters, if cosine_similarity >= 0.2, current document belongs to that cluster
    # if not then create a new cluster
    print("clusters list", clusters_list)
    cluster_id = 1
    for news_index in range(len(news_objects)):
        print (news_index)
        max_topic_similatary = 0.0
        belong_to_cluster=None
        this_document = {}
        this_document["id"] = news_objects[news_index].id
        this_document["news_index"] = news_index

        # get max similarity from cosine_similarity
        for cluster in clusters_list:
            for document in cluster['documents']:
                topic_similarity = cosine_similarity(tfidf_matrix[news_index], tfidf_matrix[document['news_index']])[0][0]
                print ("news id " + str(news_objects[news_index].id) + " vs news id " + str(document["id"]) + ": " + str(topic_similarity) )
                if (topic_similarity >= threshold and topic_similarity > max_topic_similatary):
                    belong_to_cluster = cluster
                    max_topic_similatary = topic_similarity

        # add to an existed cluster if max_topic_similatary > 0.2
        if (belong_to_cluster):
            print ("document id " + str(this_document["id"]) +" belongs to topic id " + str(belong_to_cluster["id"]) + "max_topic_similatary: " + str(max_topic_similatary))
            belong_to_cluster["documents"].append(this_document)
        else:
            belong_to_cluster = {}
            belong_to_cluster["id"] = cluster_id
            belong_to_cluster["documents"] = []
            belong_to_cluster["documents"].append(this_document)
            clusters_list.append(belong_to_cluster)
            cluster_id+=1

    # insert clusters to database
    print ("adding clusters of (" + fromDate + ", " + toDate +") to database...")
    try:
        time_period_object.total_news = len(news_objects)
        time_period_object.save()
        Cluster_Time_Period.objects.filter(time_period_id=time_period_object.id).delete()
        for cluster in clusters_list:
            cluster_object = Cluster.objects.create(cluster_core=cluster["documents"][0]["id"], number_of_news=len(cluster["documents"]))
            Cluster_Time_Period.objects.create(cluster_id=cluster_object.id, time_period_id=time_period_object.id)
            for document in cluster["documents"]:
                Cluster_News.objects.create(news_id = document["id"], cluster_id=cluster_object.id)

    except Exception:
        print ("some errors")
    print ("added clusters to database successfully")
    return
