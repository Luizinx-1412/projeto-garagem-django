from rest_framework.viewsets import ModelViewSet

from ..models import Cor
from ..serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

