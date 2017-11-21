from django.http import HttpResponse
from .tokenizer.scripts import vn_tokenizer
from .tfidf import tfidf
from .cluster import cluster
from .tfpdf import tfpdf
from .result import result_controller
from .lda import test_LDA

import numpy
import time

import nltk
import string

# used for looping through folders/files
from os import listdir
from os.path import isfile, join

#Calc tfidf and cosine similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django.shortcuts import render

def index(request):
    return render(request, "index.html", {});

def test(request):
    fromDate = request.POST.get("from_date")
    toDate = request.POST.get("to_date")
    print (fromDate)
    data = result_controller.show_result(fromDate, toDate)
    # data = [
    #   {
    #     'name': 'a',
    #     'ranking': 1,
    #     'news': [
    #       {
    #         'title': 'Bai bao 1',
    #         'url': '#'
    #       },
    #       {
    #         'title': 'Bai bao 2',
    #         'url': '#'
    #       },
    #       {
    #         'title': 'Bai bao 3',
    #         'url': '#'
    #       }
    #     ]
    #   },
    #   {
    #     'name': 'b',
    #     'ranking': 2,
    #     'news': [
    #       {
    #         'title': 'Bai bao 4',
    #         'url': '#'
    #       },
    #       {
    #         'title': 'Bai bao 5',
    #         'url': '#'
    #       }
    #     ]
    #   },
    # ]
    return render(request, "test.html", {
      "startDate": request.POST.get("from_date"),
      "endDate": request.POST.get("to_date"),
      "data": data
    });
def lda(request):
    result = test_LDA.display_topics()
    return HttpResponse(result)

def clustering(request):
    cluster.clustering('2017-11-10', '2017-11-10')
    return HttpResponse("Done")

def ranking(request):
    tfpdf.ranking_topic('2017-11-10', '2017-11-10')
    return HttpResponse('Done')

def process_raw_data(request):
    start_time = time.time()
    number_of_files = vn_tokenizer.tokenize()
    end_time = time.time()
    return HttpResponse("Proceed " + str(number_of_files) + " file(s) in " + str(end_time-start_time))

def remove(request):
  stopWords = ["nhận", "rằng", "cao", "nhà", "quá", "riêng", "gì", "muốn", "rồi", "số", "thấy", "hay", "lên", "lần",
        "nào", "qua", "bằng", "điều", "biết", "lớn", "khá", "vừa", "nếu", "thời gian", "họ", "từng", "đây", "tháng", "trước", "chính", "cả", "việc", "chưa", "do", "nói", "ra", "nên", "đều", "đi", "tới", "tôi", "có thể", "cùng", "vì", "làm", "lại", "mới", "ngày", "đó", "vẫn", "mình", "chỉ", "thì", "đang", "còn", "bị", "mà", "năm", "nhất", "hơn", "sau", "ông", "rất", "anh", "phải", "như", "trên", "tại", "theo", "khi", "nhưng", "vào", "đến", "nhiều", "người", "từ", "sẽ", "ở", "cũng", "không", "về","để","này","những","một","các","cho","được","với","có","trong","đã","là","và","của","thực_sự","ở trên","tất cả","dưới", "hầu hết","luôn","giữa", "bất","kỳ","hỏi","bạn","cô","tôi","tớ","cậu","bác","chú","dì","thím","cậu","mợ","ông","bà","em", "thường", "ai","cảm ơn"]
  inputWords = ["nhận", "a", "rằng", "cao", "nhà", "b"]
  results = []
  # results.remove(element)
  for word in inputWords:
    if word.lower() not in stopWords:
      results.append(word)

  return HttpResponse(results)
