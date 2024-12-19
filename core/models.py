from django.db import models

class Plano(models.Model):
    SEMANAL = 'semanal'
    MENSAL = 'mensal' 
    ANUAL = 'anual'
    PLANO_CHOICES = [
        (SEMANAL, 'Semanal'),
        (MENSAL, 'Mensal'),
        (ANUAL, 'Anual'),
    ]
    tipo = models.CharField(max_length=7, choices=PLANO_CHOICES, default=MENSAL)

    def __str__(self):
        return self.tipo

class FormaDePagamento(models.Model):
    PIX = 'pix'
    CEDULA = 'cedula'
    CARTAO = 'cartao'
    FORMA_CHOICES = [
        (PIX, 'Pix'),
        (CEDULA, 'Cédula'),
        (CARTAO, 'Cartão'),
    ]
    tipo = models.CharField(max_length=6, choices=FORMA_CHOICES, default=PIX)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.tipo} - R${self.valor}'

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    
    def imc(self):
        return self.peso / (self.altura ** 2)

    def tipo_de_treino(self):
        imc = self.imc()
        if imc < 18.5:
            return 'Ganho de Massa'
        elif 18.5 <= imc < 24.9:
            return 'Treino de Manutenção'
        else:
            return 'Perda de Peso'

    def __str__(self):
        return self.nome

class Treino(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    tipo_treino = models.CharField(max_length=100)

    def __str__(self):
        return f'Treino de {self.aluno.nome}'

class Contrato(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE,null=True)
    forma_pagamento = models.ForeignKey(FormaDePagamento, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'Contrato de {self.aluno.nome}'
