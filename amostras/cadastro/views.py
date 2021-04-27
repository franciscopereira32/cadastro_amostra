# Create your views here.
from .models import Inscricao
from django.views.generic.edit import CreateView

class CampoCreate(CreateView):
        model = Inscricao
        fields = ['model', 'number', 'hardware', 'supplier', 'location', 'created']
        #template_name = 'cadastro/lista.html'
        #success_url = reversed('cadastro/index.html')