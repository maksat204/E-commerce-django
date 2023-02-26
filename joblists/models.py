from django.db import models
class joblists(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)0
    is_published = models.BooleanField(default=True)


