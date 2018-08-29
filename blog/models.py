from django.db import models

# Create your models here.


class BlogEntries(models.Model):

    title = models.CharField(max_lenght=20)
    body = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    tags = models.CharField(max_lenght=20)

    def __str__(self):
        return self.title