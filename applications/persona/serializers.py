from curses import meta
from rest_framework import serializers, pagination
from . models import Person, Reunion, Hobby


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # agregando un atributo que no está en el modelo
    activo = serializers.BooleanField(required=False)


class PersonSerializers2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')


class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializers()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbySerializer(serializers.ModelSerializer):
    '''serializador que nos permite traer los valores de hobby'''
    class Meta:
        model = Hobby
        fields = ('__all__')


class PersonaSerializer3(serializers.ModelSerializer):
    '''many=True para que tenga en cuenta que vendra un array '''
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )


class ReunionSerializer2(serializers.ModelSerializer):
    '''concatenamos fecha y hora en fecha_hora'''
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora',
        )

    def get_fecha_hora(self, obj):
        '''función encargada de concatenar fecha + hora '''
        return str(obj.fecha) + ' - ' + str(obj.hora)


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    '''estructura para poder generar el link para ver el detail de persona'''
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:detail', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    # paginas en bloques de 5
    page_size = 5
    # cantidad máxima que trae en memoria
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()
