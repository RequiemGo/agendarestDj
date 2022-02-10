from django.shortcuts import render
from django.views.generic import ListView, TemplateView
# Vistas para el API rest framework
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,

)
from .serializers import (PersonSerializers,
                          PersonaSerializer,
                          PersonSerializers2,
                          ReunionSerializer,
                          PersonaSerializer3,
                          ReunionSerializer2,
                          ReunionSerializerLink,
                          PersonPagination,
                          CountReunionSerializer,
                          )
from .models import Person, Reunion
from applications.persona import serializers


class ListaPersonas(ListView):
    template_name = 'persona/personas.html'
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializers

    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = 'persona/lista.html'


class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializers

    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializers


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()


class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


class PersonApiLista(ListAPIView):
    '''vista apara intereacturar con los serializadores'''
    #serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionApiListaLink(ListAPIView):
    '''link para ver detalles de persona'''

    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()


class PersonPaginationLits(ListAPIView):
    """
        lista personas con paginacion
    """

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJob(ListAPIView):

    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
