from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    urll = models.URLField()
    title = models.TextField()
    info = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.safe()

    def __str__(self):
        return self.title