from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import UserFilterSet
from .serializers import (
    UserSerializer,
)


User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    filterset_class = UserFilterSet
