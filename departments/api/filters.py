from django_filters import rest_framework as filters


class DepartmentFilterSet(filters.FilterSet):
    with_parent = filters.CharFilter(method='filter_by_with_parent')

    def filter_by_with_parent(self, queryset, name, value):
        param = True
        if value.lower() == 'true':
            param = False
        return queryset.filter(parent__isnull=param)

    class Meta:
        fields = ['with_parent']
