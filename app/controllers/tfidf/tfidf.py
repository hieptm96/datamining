from sklearn.feature_extraction.text import TfidfVectorizer
from ...models import News

def make_doc_list(news_objects):
    doc_list = []
    i=0
    for news in news_objects:
        # if (i == 131 or i == 305):
        #     print (news.id)
        #     print (news.title)
        # i = i+1
        doc = news.title + " " + news.description + " " + news.content
        # print (doc)
        doc_list.append(doc)
    return doc_list

def execute_tfidf(news_objects):
    doc_list = make_doc_list(news_objects)
    # print (doc_list)
    tfidf_vectorizer = TfidfVectorizer(min_df = 1)
    tfidf_matrix = tfidf_vectorizer.fit_transform(doc_list)
    # print (tfidf_matrix.todense())

    return tfidf_matrix.todense()
