from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import ProdutoForm
from .models import Produto

class CreateProdutoView(CreateView):
    template_name = 'criar_produto.html'
    form_class = ProdutoForm
    success_url = reverse_lazy('core:listar_produtos')


class UpdateProdutoView(UpdateView):
	template_name = 'criar_produto.html'
	form_class = ProdutoForm
	success_url = reverse_lazy('core:listar_produtos')

	def get_object(self, queryset=None):
		id = self.kwargs['id']
		return Produto.objects.get(pk=id)


class DeleteProdutoView(DeleteView):
	template_name = 'criar_produto.html'
	model = Produto	

	def get_success_url(self):
		return reverse_lazy('core:listar_produtos')


	def get_object(self, queryset=None):
		id = self.kwargs['id']
		return Produto.objects.get(pk=id)

	def get(self, request, *args, **kwargs):
		produto = self.get_object()

		produto.delete()
		# livro.minha_transacao.delete()


		return redirect('core:listar_produtos')


class ProdutoListView(ListView):
	model = Produto
	template_name = 'index.html'
	paginate_by = 5
