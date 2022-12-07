from django.db import models


class Task(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    time=models.TimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)


class CompletedTask(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField()
    time=models.TimeField(auto_now_add=True)
    date=models.DateField(auto_now_add=True)    
    
