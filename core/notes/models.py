from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=100, db_index=True)
    user_emai = models.CharField(max_length=100, db_index=True)
    user_password = models.CharField(max_length=140)


class Note(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
