from django.shortcuts import render,redirect
from .models import Loss_comunication
from .forms import FormLossComunication
from haversine import haversine
import folium

# Create your views here.
def home(request):
    return render(request,'index.html')

def form_comunication(request):
    return render(request,'formComunication.html')


#  CRUD COMUNICAÇÕ DE PERDA

def list_comunication(request):
    comunication= Loss_comunication.objects.all()
    busca = request.GET.get('search')
    if busca:
        comunication = Loss_comunication.objects.filter(cpf_produtor__icontains=busca)
    return render(request,'listComunication.html',{'chave_list_comunication':comunication})

def create_comunication(request):
    form = FormLossComunication(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'formComunication.html',{'chave_form_comunication':form})    

def update_comunication(request,id_update):
    #RESGATAR DADOS DA COMUNICAÇÃO DE PERDA DE ACORDO COM O CPF VINCULADO
    comunication = Loss_comunication.objects.get(cpf_produtor=id_update)
    form = FormLossComunication(request.POST or None, instance=comunication)

    if form.is_valid():
        form.save()
        return redirect('list_comunication')
    return render(request,'updateComunication.html',{'chave_update_comunication':form}) 

def delete_comunication(request, id_delete):
    comunication = Loss_comunication.objects.get(cpf_produtor=id_delete)
    comunication.delete()
    return redirect('list_comunication')

def verifica_distancia(request):
    date = False
    form = FormLossComunication(request.POST or None)
    comunication= Loss_comunication.objects.all()
    busca = request.GET.get('search')
    if busca:
        comunication = Loss_comunication.objects.filter(cpf_produtor__icontains=busca)
        return render(request,'listComunication.html',{'chave_list_comunication':comunication})
    if form.is_valid():
        form.save()   
    if request.method == 'POST':
        latitude = request.POST.get('latitude_produtor')
        longitude = request.POST.get('longitude_produtor')
        ocorrencia = request.POST.get('evento_ocorrido_produtor')
        data = request.POST.get('data_colheita_produtor')
        latitude_float = float(latitude)
        longitude_float = float(longitude)
        cidade_post = (latitude_float , longitude_float)
        for i in comunication:
            data_banco = i.data_colheita_produtor
            ocorrencia_banco = i.evento_ocorrido_produtor
            latitude_banco= i.latitude_produtor
            longitude_banco= i.longitude_produtor
            latitude_banco_float = float(latitude_banco)
            longitude_banco_float = float(longitude_banco)
            cidade_banco = (latitude_banco_float, longitude_banco_float)
            distancia = haversine(cidade_post, cidade_banco)
            if (distancia <= 10 )and (ocorrencia != ocorrencia_banco) and (data == data_banco):
                #messages.warning(request,'erro')
                date = True  
               
                 
    return render(request,'listComunication.html',{'date':date,'chave_list_comunication':comunication})
    
def map(request):
    comunication= Loss_comunication.objects.all()
   
    figure = folium.Figure()
    m = folium.Map(
        location=[-14.239424, -53.186502],
        zoom_start=3.5,
        tiles='Stamen Terrain'
    )
    m.add_to(figure)
    for i in comunication:
        lat = i.latitude_produtor
        long = i.longitude_produtor
        lat_float = float(lat)
        long_float = float(long)

        folium.Marker(
            location=[lat_float, long_float],
            popup='Produtor',
            icon=folium.Icon(icon='cloud')
        ).add_to(m)

    figure.render()
    return render(request,"map.html",{"map": figure})

