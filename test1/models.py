from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50,unique=True)
    descriptions = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

