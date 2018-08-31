from django.db import models
from django.utils.text import slugify
# Create your models here.


class BlogEntries(models.Model):

    title = models.CharField(max_length=20)
    body = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title