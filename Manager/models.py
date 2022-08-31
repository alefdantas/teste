from django.db import models

# Create your models here.
class Loss_comunication(models.Model):
    EVENTO_CHOICES = (
        ("CHUVA EXCESSIVA","CHUVA EXCESSIVA"),
        ("GEADA","GEADA"),
        ("GRANIZO","GRANIZO"),
        ("SECA","SECA"),
        ("VENDAVAL","VENDAVAL"),
        ("RAIO","RAIO")
    )
    nome_produtor = models.CharField(max_length=75)
    email_produtor = models.EmailField()
    cpf_produtor = models.CharField(max_length=11,primary_key=True)
    latitude_produtor = models.CharField(max_length=200)
    longitude_produtor = models.CharField(max_length=200)
    tipo_lavoura_produtor = models.CharField(max_length=75)
    data_colheita_produtor = models.CharField(max_length=11)
    evento_ocorrido_produtor = models.CharField(max_length=75,choices=EVENTO_CHOICES,default=None)
   