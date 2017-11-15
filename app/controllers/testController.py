from django.http import HttpResponse
from .tokenizer.scripts import vn_tokenizer

def index(request):
  vn_tokenizer.tokenize("thuan.txt", "haha.txt")
  return HttpResponse("Hello,e at the polls index.")
