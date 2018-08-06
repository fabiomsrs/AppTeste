"""teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import CreateProdutoView, UpdateProdutoView, ProdutoListView, DeleteProdutoView

app_name = 'core'

urlpatterns = [
    path('criar_produtos/', CreateProdutoView.as_view(), name='criar_produto'),
    path('atulizar_produtos/<int:id>', UpdateProdutoView.as_view(), name='atualizar_produto'),
    path('deletar_produtos/<int:id>', DeleteProdutoView.as_view(), name='deletar_produto'),
    path('', ProdutoListView.as_view(), name='listar_produtos'),
]
