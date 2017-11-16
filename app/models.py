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
  time = models.DateTimeField(blank=True, null=True)

class Cluster(models.Model):
  cluster_core = models.IntegerField()
  numOfDocuments = models.IntegerField()

class DocumentRepresentation(models.Model):
  representation = models.TextField()
  cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
