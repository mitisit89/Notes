from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from time import time


def create_slug(s):
    slug = slugify(s, allow_unicode=True)
    return f"{slug}-{str(int(time()))}"


class Note(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = create_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
