from django.db import models

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

class News(models.Model):
  title = models.TextField()
  description = models.TextField()
  url = models.TextField()
  content = models.TextField()
  date = models.DateField(blank=True, null=True)
  file_name = models.TextField()
  website_id = models.IntegerField()

class Time_Period(models.Model):
  total_news = models.IntegerField()
  fromDate = models.DateField()
  toDate = models.DateField()

class Cluster(models.Model):
  cluster_core = models.IntegerField()
  number_of_news = models.IntegerField()

class Cluster_Time_Period(models.Model):
  cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
  time_period = models.ForeignKey(Time_Period, on_delete=models.CASCADE)

class Cluster_News(models.Model):
  cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
  news = models.ForeignKey(News, on_delete=models.CASCADE)

class Website(models.Model):
  name = models.TextField()
  weight = models.FloatField()

class DocumentRepresentation(models.Model):
  representation = models.TextField()
  cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)

class Vocabulary(models.Model):
  fromDate = models.DateField()
  toDate = models.DateField()
  vocabulary_set = models.TextField()
