from django.db import models


# Create your models here.

class FakeCardGame(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/')
    answer = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.description + ' ' + str(self.answer)


class FakeNews(models.Model):
    description = models.TextField()
    answer = models.BooleanField(blank=True, null=True)
    correct = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.description + ' ' + str(self.answer) + ' ' + str(self.correct)
