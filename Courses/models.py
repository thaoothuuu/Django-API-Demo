from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=255)


    def __int__(self):
        return self.price

    def to_json(self):
        return {
            'title': self.title,
            'price': self.price,
            'content': self.content,
        }


