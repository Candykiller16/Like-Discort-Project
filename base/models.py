from django.db import models
from django.contrib.auth .models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # автор комнаты
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) # тема комнаты
    name = models.CharField(max_length=200)  # имя комнаты
    description = models.TextField(null=True, blank=True)  # описание о комнате, может быть пустое
    # participants = # хранит данные о юзерах, которые находятся в данный момент в комнате
    update = models.DateField(auto_now=True)  # auto_now срабатывает каждый раз, когда мы изменяем запись в таблице
    created = models.DateField(auto_now_add=True)  # auto_now_add - работает 1 раз при создании записи в таблице

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    update = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] # в админке будет видеть с 0 по 49 символы поля body

