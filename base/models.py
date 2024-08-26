from django.db import models

# Create your models here.


class Words(models.Model):
    words = models.TextField()

    def __str__(self):
        return self.words[:50]

    class Meta:
        verbose_name_plural = 'Words'
