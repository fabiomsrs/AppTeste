from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import ProdutoForm
from .models import Produto

class CriarProdutoView(CreateView):
    template_name = 'criar_produto.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('core:criar_produtos')


class ProdutoListView(ListView):
	model = Produto
	template_name = 'index.html'
	paginate_by = 5
	
