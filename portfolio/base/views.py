from django.http import HttpResponseRedirect
from django.shortcuts import render
from portfolio.base.forms import ContatoForm

def home(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():  # Valida os dados enviados no formulário
            # Salvamento manual dos dados do formulário
            contato = form.save()
            contato.save()  # Salva o objeto no banco de dados
            
            # Você pode adicionar lógica adicional aqui, como redirecionar
            return render(request, 'portfolio/projeto01.html', {'contato': contato})
    else:
        form = ContatoForm()
    return render(request, 'portfolio/projeto01.html', {'form': form})


