from django import forms
from .models import Aluno, Contrato, Treino, Plano, FormaDePagamento

class CadastroCompletoForm(forms.Form):
    # Campos do Aluno
    nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    peso = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    altura = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))

    # Campos do Contrato
    plano = forms.ModelChoiceField(queryset=Plano.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    forma_pagamento = forms.ModelChoiceField(queryset=FormaDePagamento.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    # Campos do Treino
    tipo_treino = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'peso', 'altura']