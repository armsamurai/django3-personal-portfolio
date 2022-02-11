from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    
    def __str__(self): # Будет возвращать имя по умолчанию при наведении курсора на один из объектов
        return f'{self.title} Date: {self.date}'