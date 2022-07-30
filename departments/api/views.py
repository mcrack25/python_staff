from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from ..models import Department
from .filters import DepartmentFilterSet

from .serializers import (
    DepartmentSerializer,
)


class DepartmentViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilterSet
