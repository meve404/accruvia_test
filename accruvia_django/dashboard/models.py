from django.db import models

class Tweets(models.Model):
    fullName = models.CharField(max_length=20)
    tweetText = models.CharField(max_length=50)
    
    created = models.DateTimeField(auto_now_add=True) #takes a snapshot when the instance is created

    def __str__(self):
        return self.fullName