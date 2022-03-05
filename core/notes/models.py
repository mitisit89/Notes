from django.db import models

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=150,db_index=True)
    body=models.TextField(blank=True,db_index=True)
    created=models.DateTimeField(auto_now_add=True)
