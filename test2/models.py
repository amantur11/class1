from django.db import models
from test1.models import Post


class Comment(models.Model):
    title = models.CharField(max_length=60,unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comment')

    def __ste__(self) -> str:
        return self.title

