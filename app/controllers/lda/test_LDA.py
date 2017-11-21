from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation
from ...models import News, Cluster_News, Cluster



def display_topics(cluster):

    data_sets = News.objects.filter(cluster_news__cluster_id=cluster.id)
    documents = []
    for data in data_sets:
        documents.append(data.title + ' ' + data.description)
    # dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
    #
    # documents = dataset.data
    try:

        # print documents
        no_features = 1000

        # NMF is able to use tf-idf
        tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
        tfidf = tfidf_vectorizer.fit_transform(documents)
        tfidf_feature_names = tfidf_vectorizer.get_feature_names()

        # LDA can only use raw term counts for LDA because it is a probabilistic graphical model
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
        tf = tf_vectorizer.fit_transform(documents)
        feature_names = tf_vectorizer.get_feature_names()

        no_topics = 1

        # Run NMF
        nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)

        # Run LDA
        model = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

        no_top_words = 10
        result = ''
        for topic_idx, topic in enumerate(model.components_):
            result = " ".join([feature_names[i]
                            for i in topic.argsort()[:-no_top_words - 1:-1]])

        return result
            # print "Topic %d:" % (topic_idx)
            # print " ".join([feature_names[i]
            #                 for i in topic.argsort()[:-no_top_words - 1:-1]])
    except:
        return None
# display_topics(nmf, tfidf_feature_names, no_top_words)
# display_topics(lda, tf_feature_names, no_top_words)
