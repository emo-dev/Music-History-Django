from django.db import models


# Create your models here.
class Artist(models.Model):
    """Setting up our Questions database"""
    ArtistName = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')    

    def __str__(self):
        """Allows you to print out artist name on referral"""
        return self.ArtistName


class Song(models.Model):
    """Setting up our Choices Database"""
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    SongTitle = models.CharField(max_length=200)

    def __str__(self):
        """Allows you to print out SongTitle on referral"""
        return self.SongTitle


