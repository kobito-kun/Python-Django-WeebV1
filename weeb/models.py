from django.db import models
from django.utils import timezone

now = timezone.now()

# Create your models here.

class Post(models.Model):
    TYPE = (
        ('Manga', 'Manga'),
        ('Manhwa', 'Manhwa'),
        ('Manhua', 'Manhua'),
        ('Webtoon', 'Webtoon'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True)
    type = models.CharField(max_length=7, choices=TYPE, null=True)
    date = models.DateField(default=now)

    def __str__(self):
        return str(self.title)