from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello,e at the polls index.")
