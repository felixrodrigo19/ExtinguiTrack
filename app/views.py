from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.models import FireExtinguisher
from app.models import Type
from app.models import Capacity
from app.models import Agent
from app.models import Location
from app.models import Supplier
from app.models import Manufacture
from app.serializers import ManufactureSerializer
from app.serializers import TypeSerializer
from app.serializers import CapacitySerializer
from app.serializers import AgentSerializer
from app.serializers import LocationSerializer
from app.serializers import SupplierSerializer
from app.serializers import FireExtinguisherSerializer


class FireExtinguishersViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Extinguishers** registered in the system.
    """
    serializer_class = FireExtinguisherSerializer
    queryset = FireExtinguisher.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TypeViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Extinguishers Types** registered in the system.
    """
    serializer_class = TypeSerializer
    queryset = Type.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CapacityViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Extinguishers Capacity** registered in the system.
    """
    serializer_class = CapacitySerializer
    queryset = Capacity.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class AgentViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Extinguishers Agent Types** registered in the system.
    """
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Extinguishers Location** registered in the system.
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Suppliers** registered in the system.
    """
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ManufactureViewSet(viewsets.ModelViewSet):
    """
    Returns a list of all **Manufactures** registered in the system.
    """
    serializer_class = ManufactureSerializer
    queryset = Manufacture.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):
    """
    Return token and email from a specific user
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'email': user.email
        })
