from sklearn.feature_extraction.text import TfidfVectorizer
from ...models import News, Vocabulary

def make_doc_list():
    news_objects = News.objects.filter(date='2017-11-01')
    doc_list = []
    for news in news_objects:
        doc = news.title
        doc_list.append(doc)
    return doc_list

def execute_tfidf(fromDate, toDate):
    doc_list = make_doc_list()
    print (doc_list)
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(doc_list)
    print (tfidf_matrix.todense())

    return tfidf_matrix.todense()
