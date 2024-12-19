from django.shortcuts import render
from .models import Aluno, Treino, Contrato
from django.shortcuts import render, redirect
from .forms import CadastroCompletoForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/home.html', {'alunos': alunos})

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'core/lista_alunos.html', {'alunos': alunos})

def tabela_treinos(request):
    treinos = Treino.objects.all()
    return render(request, 'core/tabela_treinos.html', {'treinos': treinos})

def contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'core/contratos.html', {'contratos': contratos})

def cadastrar_completo(request):
    if request.method == 'POST':
        form = CadastroCompletoForm(request.POST)
        if form.is_valid():
            # Criando o Aluno
            aluno = Aluno.objects.create(
                nome=form.cleaned_data['nome'],
                peso=form.cleaned_data['peso'],
                altura=form.cleaned_data['altura']
            )

            # Criando o Contrato
            contrato = Contrato.objects.create(
                aluno=aluno,
                plano=form.cleaned_data['plano'],
                forma_pagamento=form.cleaned_data['forma_pagamento'],
                data_inicio=form.cleaned_data['data_inicio'],
                data_fim=form.cleaned_data['data_fim'],
                descricao=form.cleaned_data['descricao']
            )

            # Criando o Treino
            Treino.objects.create(
                aluno=aluno,
                tipo_treino=form.cleaned_data['tipo_treino']
            )

            return redirect('home')  # Redireciona para uma página, por exemplo, lista de alunos
    else:
        form = CadastroCompletoForm()

    return render(request, 'core/cadastrar_completo.html', {'form': form})
#mudanças aqui abaixo

def editar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    contrato = get_object_or_404(Contrato, aluno=aluno)
    treino = get_object_or_404(Treino, aluno=aluno)

    if request.method == 'POST':
        form = CadastroCompletoForm(request.POST)
        if form.is_valid():
            # Atualiza os dados do aluno
            aluno.nome = form.cleaned_data['nome']
            aluno.peso = form.cleaned_data['peso']
            aluno.altura = form.cleaned_data['altura']
            aluno.save()

            # Atualiza os dados do contrato
            contrato.plano = form.cleaned_data['plano']
            contrato.forma_pagamento = form.cleaned_data['forma_pagamento']
            contrato.data_inicio = form.cleaned_data['data_inicio']
            contrato.data_fim = form.cleaned_data['data_fim']
            contrato.descricao = form.cleaned_data['descricao']
            contrato.save()

            # Atualiza os dados do treino
            treino.tipo_treino = form.cleaned_data['tipo_treino']
            treino.save()

            return redirect('lista_alunos')  # Redireciona para a lista de alunos
    else:
        # Pré-popula o formulário com os dados existentes
        form = CadastroCompletoForm(initial={
            'nome': aluno.nome,
            'peso': aluno.peso,
            'altura': aluno.altura,
            'plano': contrato.plano,
            'forma_pagamento': contrato.forma_pagamento,
            'data_inicio': contrato.data_inicio,
            'data_fim': contrato.data_fim,
            'descricao': contrato.descricao,
            'tipo_treino': treino.tipo_treino,
        })

    return render(request, 'core/editar_aluno.html', {'form': form, 'aluno': aluno})

# View para deletar um aluno
def deletar_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'deletar_aluno.html', {'aluno': aluno})