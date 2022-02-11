from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) # Заголовок. Ограничиваем его длину в 100 символов.
    description = models.CharField(max_length=250) # Короткое описание проекта. 
    image = models.ImageField(upload_to = 'portfolio/images/') # Картинка для описания. upload_to - определяет, в какой папке будут храниться изображения.  
    url = models.URLField(blank=True) # Ссылка на страницу. blank = true - открытие ссылки в новом окне. 

    def __str__(self): # Будет возвращать имя по умолчанию при наведении курсора на один из объектов
        return f'{self.title}'