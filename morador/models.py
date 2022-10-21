from django.db import models


sexo_psr = {
    ('F', 'FEMININO' ),
    ('M', 'MASCULINO')

}
tempoManau = {
    ('-1', 'Menos de 1 ano'),
    ('1a5', 'Entre 1 a 5 anos'),
    ('6a10', 'Entre 6 a 10 anos'),
    ('11a15', 'Entre 11 a 15 anos'),
    ('16+', 'Mais de 16 anos')
}

cor = {
    ('Branca', 'Branca'),
    ('Negra', 'Negro/Preta'),
    ('Parda', 'Parda'),
    ('Amarelo', 'Amarela'),
    ('indigena', 'Indigena')
}
class Morador(models.Model):

    ruaAbordagem = models.CharField(max_length=50, null=True, verbose_name='Rua Abordagem')
    bairroAbordagem = models.CharField(max_length=50, null=True, verbose_name='Bairro Abordagem')
    nome = models.CharField(max_length=50, null=True, verbose_name='Nome')
    apelido = models.CharField(max_length=30, null=True, verbose_name='Apelido')
    nomeMAe = models.CharField(max_length=50, null=True, verbose_name='Nome da Mãe')
    nomePai = models.CharField(max_length=50, null=True, verbose_name='Nome do Pai')
    idade = models.IntegerField(blank=True, null=True, verbose_name='Idade')
    sexo = models.CharField(max_length=10, choices=sexo_psr, null=True)
    cor = models.CharField(max_length=10, choices=cor, null=True)
    naturalidade = models.CharField(max_length=25, null=True, verbose_name='Naturalidade')
    tempoManaus = models.CharField(max_length=20, choices=tempoManau, null=True, verbose_name='Tempo em Manaus')
    rg = models.CharField(max_length=30, null=True, verbose_name='RG')
    cpf = models.CharField(max_length=11, null=True, verbose_name='CPF')
    cartaoSus = models.CharField(max_length=30, null=True, verbose_name='Cartão SUS')
    cadUnico = models.CharField(max_length=30, null=True, verbose_name='Cad. Único')
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True, verbose_name='Última alteração')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, verbose_name='Data de Cadastro')


    def _str_(self):
        return self.nome