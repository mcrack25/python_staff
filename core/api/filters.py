from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.expressions import Value
from django.db.models.functions import Concat
from django_filters import rest_framework as filters


class UserFilterSet(filters.FilterSet):
    fullname = filters.CharFilter(method='filter_by_fullname')

    def filter_by_fullname(self, queryset, name, value):
        return queryset \
                .annotate(fullname=Concat('last_name', Value(' '), 'first_name')) \
                .annotate(similarity=TrigramSimilarity('fullname', value)) \
                .filter(similarity__gt=0.1).order_by('-similarity')

    class Meta:
        fields = ['fullname']
