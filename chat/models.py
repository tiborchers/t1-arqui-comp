from django.db import models

class Message(models.Model):
    timestamp= 	models.DateTimeField()
    author_ip= models.GenericIPAddressField()
    content= models.TextField()

    def __str__(self):
        return self.author_ip +" - " + self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
