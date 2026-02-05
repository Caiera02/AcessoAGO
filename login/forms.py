from django import forms
from django.core.exceptions import ValidationError
from login.models import MatriculaAutorizada,Acesso

class AcessoForm(forms.Form):
    nome = forms.CharField(label='Nome Completo', max_length=100)
    matricula = forms.CharField(label='Matrícula', max_length=5)

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if len(matricula) != 4:
            raise ValidationError("A matrícula deve ter exatamente 4 dígitos.")
        
        if not matricula.isdigit():
            raise ValidationError("A matrícula deve conter apenas números.")
    
        if Acesso.objects.filter(matricula=matricula).exists():
            raise ValidationError("Você já preencheu a lista")
    
        return matricula
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        return nome.upper()
    
# class AcessoForm(forms.Form):
#     nome = forms.CharField(max_length=100)
#     matricula = forms.CharField(max_length=5)

#     def clean_matricula(self):
#         matricula = self.cleaned_data.get('matricula')
        
#         # 1. Validação de tamanho (conforme sua regra de 5 dígitos)
#         if len(matricula) != 5:
#             raise ValidationError("A matrícula deve ter exatamente 5 dígitos.")
        
#         # 2. Verificação na lista de autorizados
#         if not MatriculaAutorizada.objects.filter(numero=matricula).exists():
#             raise ValidationError("Esta matrícula não está autorizada a acessar.")
            
#         return matricula