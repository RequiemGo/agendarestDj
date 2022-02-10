from unicodedata import name
from django.urls import path, re_path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path('personas/', views.ListaPersonas.as_view(), name='personas'),
    path('api/persona/lista/', views.PersonListApiView.as_view(), ),
    path('lista/', views.PersonListView.as_view(), name='lista'),
    path('api/persona/search/<kword>/',
         views.PersonSearchApiView.as_view(), name='search'),
    path('api/persona/create/', views.PersonCreateView.as_view(), ),
    path('api/persona/detail/<pk>/',
         views.PersonDetailView.as_view(), name='detail'),
    path('api/persona/delete/<pk>/',
         views.PersonDeleteView.as_view(), name='delete'),
    path('api/persona/update/<pk>/',
         views.PersonRetrieveUpdateView.as_view(), name='update'),
    path('api/reuniones/', views.ReunionApiLista.as_view(), name='reunion'),
    path('api/persona/', views.PersonApiLista.as_view(), ),
    path('api/reuniones-link/', views.ReunionApiListaLink.as_view()),
    path('api/personas/paginacion/',
         views.PersonPaginationLits.as_view(), name='pagination'),
    path('api/reunion/por-job', views.ReunionByPersonJob.as_view()),
]
