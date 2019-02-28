from django.db import models

# Create your models here.


class Filme(models.Model):
    genero_acao='ac'
    genero_ficcao='fc'
    genero_terror='tr'
    genero_aventura='av'
    genero_comedia='cm'
    genero_romance='ro'
    genero_drama='dr'
    genero_opcoes= [
        (genero_acao,'ação'),
        (genero_aventura,'aventura'),
        (genero_ficcao,'ficção'),
        (genero_terror, 'Terror'),
        (genero_comedia, 'comedia'),
        (genero_drama, 'Drama'),
        (genero_romance, 'Romance'),
    ]

    nome = models.CharField(max_length=120)
    genero = models.CharField(max_length=2, choices=genero_opcoes, default=None)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    cartaz = models.ImageField(upload_to='media')

    def __strf__(self):
        return self.nome