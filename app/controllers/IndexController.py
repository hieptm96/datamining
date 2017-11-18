from django.http import HttpResponse
from .tokenizer.scripts import vn_tokenizer
from .vocabulary import vocabulary_set
from .tf_idf import tfidf

import numpy

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
  vn_tokenizer.tokenize()
  result = tfidf.execute_tfidf('2017-11-01', '2017-11-02')
  f = open('test.txt', 'w')
  f.write(str(result))

  matrixValue = []
  for i in range(len(result)):
    row = []
    for j in range(len(result)):
      numValue = cosine_similarity(result[i], result[j])[0][0]
      row.append(numValue)
    matrixValue.append(row)

  # print (len(result[0]))
  # return HttpResponse(result)

  # return HttpResponse(cosine_distance(result[0], result[0]))
  return render(request, "index.html", {
    'matrixValue': matrixValue
  });

def make_vocabulary_set(request):
    vocabulary_set.make_vocabulary_set()
    return HttpResponse("Make vocabulary set succeed")

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
