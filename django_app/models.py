from django.db import models


class Poll (models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Option (models.Model):
    text = models.CharField(max_length=255)
    number_of_voices = models.IntegerField(default=0)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class ConnectedUsers(models.Model):
    first_name = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s connected at %s" % (self.first_name, self.connected)
