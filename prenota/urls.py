from django.urls import path
from . import views



urlpatterns = [
    path('',views.index , name='index'),
    path('logout',views.logout , name='logout'),
    path('signup/', views.signup, name='signup'),
    path('prenota/', views.prenota, name='prenota'),
    #path('prenotazione/', views.prenotazione, name='prenotazione'),
    path('ordine/<int:id>', views.ordine, name='ordine'),
    path('piatti/', views.piatti_ordinati, name='piatti_ordinati'),
    path('tutti/', views.tutti_prenotazione, name='tutti_prenotazione'),
    path('details/<int:id>', views.details, name='details'),
    path('ordine_details/<int:pd>/<int:id>', views.ordine_details, name='ordine_details'),

]