from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

#Create a table for projects and to-dos
#class Project(models.Model):
# 	name = models.CharField(max_length=50)
# 	owner = models.CharField(max_length=50)
# 
# class Todo(models.Model):
# 	project_name = models.ForeignKey(Project)
# 	title = models.CharField(max_length=100)
# 	due_date = models.DateField()
# 	order = models.IntegerField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)