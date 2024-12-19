from django.urls import path
from . import views  # Importe suas views aqui
from django.http import HttpResponse

# Adicione uma view básica para teste


urlpatterns = [
    path('', views.home, name='home'),
    path('alunos/', views.lista_alunos, name='lista_alunos'),
    path('editar_aluno/<int:pk>/', views.editar_aluno, name='editar_aluno'),
    path('alunos/deletar/<int:pk>/', views.deletar_aluno, name='deletar_aluno'),
    path('treinos/', views.tabela_treinos, name='tabela_treinos'),
    path('contratos/', views.contratos, name='contratos'),
    path('cadastrar-completo/', views.cadastrar_completo, name='cadastrar_completo'),

]

