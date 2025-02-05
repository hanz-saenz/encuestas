from django.db import models
from django.contrib.auth.models import User
# Create your models here.

url_static = 'static/assets/imagenes'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=f'{url_static}/avatars', null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

class TokensUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.TextField()

    def __str__(self):
    
        return self.user.username