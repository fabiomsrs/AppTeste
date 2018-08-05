from django import forms
from core.models import Produto, Fabrica


class ProdutoForm(forms.ModelForm):
	CHOICE_CATEGORIA = (
		('TECNOLOGIA', 'tecnologia'),
		('ROUPAS', 'roupas'),
		('CALCADOS', 'calçados'),
		('ESPORTES', 'esportes'),
		)

	nome_fabrica = forms.CharField(max_length=45)
	categoria = forms.CharField(
        max_length=124,
        widget=forms.Select(
            choices=CHOICE_CATEGORIA,
            attrs={'class': 'browser-default'}),
        
    )	

	class Meta:
		model = Produto
		exclude = ('data_criacao','fabrica')

	def save(self, commit=True):
		produto = super(ProdutoForm, self).save(commit=False)
		produto.nome = self.cleaned_data['nome']
		produto.valor = self.cleaned_data['valor']       
		produto.descricao = self.cleaned_data['descricao']
		produto.categoria = self.cleaned_data['categoria']
		nome_fabrica = self.cleaned_data['nome_fabrica']       
		
		if Fabrica.objects.filter(nome=nome_fabrica):
			fabrica = Fabrica.objects.get(nome=fabrica)			
			produto.fabrica = fabrica			
		else:
			fabrica = Fabrica.objects.create(nome=nome_fabrica)			
			produto.fabrica = fabrica		

		produto.save()
		return produto