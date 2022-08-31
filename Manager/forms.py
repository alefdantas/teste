
from dataclasses import field
from django import forms
from .models import Loss_comunication


class FormLossComunication(forms.ModelForm):

    
    class Meta:
        model = Loss_comunication
        fields = ['cpf_produtor','nome_produtor','email_produtor','latitude_produtor','longitude_produtor','data_colheita_produtor','tipo_lavoura_produtor','evento_ocorrido_produtor']
        

 
