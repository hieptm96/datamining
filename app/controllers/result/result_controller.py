from ...models import News, Cluster, Time_Period, Cluster_Time_Period, Cluster_News
from ..cluster import cluster
from ..tfpdf import tfpdf

def show_result(fromDate, toDate):
    # check time period
    time_period = Time_Period.objects.filter(fromDate=fromDate, toDate=toDate).first()

    # if not existed, run clustering
    if (not time_period):
        cluster.clustering(fromDate, toDate)
    
    tfpdf.ranking_topic(fromDate, toDate)

    time_period = Time_Period.objects.filter(fromDate=fromDate, toDate=toDate).first()
    cluster_objects = Cluster.objects.filter(cluster_time_period__time_period_id = time_period.id).order_by('-hot_level')
    result = []
    for cluster_object in cluster_objects:
        element={}
        element['name'] = News.objects.get(id = cluster_object.cluster_core).title
        element['ranking'] = cluster_object.hot_level
        result.append(element)
    return result
