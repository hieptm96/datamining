from django.shortcuts import render
from django.http import HttpResponse
from app.models import Question, Choice


# Create your views here.

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
  return HttpResponse(Question.objects.all()[0].id)
  # return render(request, "index.html", {
  #   'a': Question.objects.all()
  # });
