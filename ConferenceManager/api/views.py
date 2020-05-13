from rest_framework import viewsets

from .serializers import PaperSerializer
from ..models import Paper


class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all().order_by('name')
    serializer_class = PaperSerializer
