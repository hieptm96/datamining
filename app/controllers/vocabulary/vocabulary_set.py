from ...models import News, Vocabulary

def make_vocabulary_set_in_date(date):
    # get vocabulary
    vocabulary_object = Vocabulary.objects.filter(fromDate=date, toDate=date).first()

    # create if not exist
    if(not vocabulary_object):
        vocabulary_object = Vocabulary.objects.create(fromDate=date, toDate=date)

    # make vocabulary
    vocabulary_set = vocabulary_object.vocabulary_set.split(' ')
    print (len(vocabulary_set))
    news_objects = News.objects.filter(date=date, add_to_vocabulary_set=0)
    for news in news_objects:
        words_list = news.title.split() + news.description.split() + news.content.split()
        # print (vocabulary_set)
        vocabulary_set = list(set(vocabulary_set + words_list))
        news.add_to_vocabulary_set = 1
        news.save()
    vocabulary_object.vocabulary_set = ' '.join(vocabulary_set).strip()
    vocabulary_object.save()
    return


def make_vocabulary_set():
    days=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17']
    for day in days:
        make_vocabulary_set_in_date('2017-11-' + day)
    # make_vocabulary_set_in_date('2017-11-17')
    # news_objects = News.objects.filter(add_to_vocabulary_set=0)
    # for news in news_objects:
    #     print (news.id)
    #     full_document = news.title + ' ' + news.description + ' ' + news.content
    #     for word in full_document.split():
    #         if(not is_in_vocabulary_set(word)):
    #             add_to_vocabulary_set(word, news.id)
    #
    #     news.add_to_vocabulary_set = 1
    #     news.save()
    return

# make_vocabulary_set()
