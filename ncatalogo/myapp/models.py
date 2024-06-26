from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roupa(models.Model):
    title = models.CharField(max_length=100)
    path = models.ImageField(upload_to="imagens/")
    descript = models.TextField()
    
class Curtida(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    clothe_id = models.ForeignKey(Roupa, on_delete=models.CASCADE)
 

class Comentario(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    clothe_id = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    content = models.IntegerField()
   