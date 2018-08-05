from django.db import models

# Create your models here.

class Produto(models.Model):
	CHOICE_CATEGORIA = (
		('TECNOLOGIA', 'tecnologia'),
		('ROUPAS', 'roupas'),
		('CALCADOS', 'calçados'),
		('ESPORTES', 'esportes'),
		)

	nome = models.CharField(max_length=45)
	valor = models.FloatField()
	descricao = models.CharField(max_length=140)
	categoria = models.CharField(max_length=30, choices=CHOICE_CATEGORIA)
	data_criacao = models.DateTimeField(auto_now=True)
	fabrica = models.ForeignKey('Fabrica', related_name='produtos_fornecidos', on_delete=models.CASCADE)

	def __str__(self):
		return self.nome


class Fabrica(models.Model):
	nome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome