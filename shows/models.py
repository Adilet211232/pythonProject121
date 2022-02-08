from django.db import models


class TVShow(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama')

    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICE,max_length=100)
    data_filmed = models.DateField()
