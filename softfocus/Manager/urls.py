from django.urls import path
from .views import  home,create_comunication,list_comunication, update_comunication,delete_comunication,verifica_distancia,map
urlpatterns = [
    path('', home,name="home" ),
    path('verification/list_comunication/',verifica_distancia ,name="verifica_distancia" ),
    path('create_comunication/',create_comunication ,name="create_comunication" ),
    path('list_comunication/',list_comunication ,name="list_comunication" ),
    path('update_comunication/<int:id_update>/',update_comunication ,name="update_comunication" ),
    path('delete_comunication/<int:id_delete>/',delete_comunication ,name="delete_comunication" ),
    path('map/', map,name="map" ),
    

    

]