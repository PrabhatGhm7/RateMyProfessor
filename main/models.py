from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from profanity.validators import validate_is_profane


# Create your models here.
    
class Professor(models.Model):
    name = models.CharField(max_length = 255)
    course = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name

class Rating(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    comments = models.TextField(validators=[validate_is_profane])
    datecreated = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.professor} - {self.rating}'
