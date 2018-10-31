import django_filters
from django_filters import rest_framework as filters


#from django_filters.widgets import CSVWidget
from jobs.models import Job, Category


class TagsFilter(filters.CharFilter):
    """
    Return all objects which match any of the provided tags, ||
    """

    def filter(self, queryset, value):
        if value:
            tags = [tag.strip() for tag in value.split(',')]
            queryset = queryset.filter(tags__name__in=tags).distinct()

        return queryset

class JobFilter(django_filters.FilterSet):
    """
    create filter for class job
    """
    title = django_filters.CharFilter(field_name = 'title', lookup_expr = 'icontains')
    location = django_filters.CharFilter(field_name = 'location', lookup_expr = 'icontains')
    tag = TagsFilter(field_name = "tags",lookup_expr = 'icontains')
    category = django_filters.CharFilter(field_name = 'category__cate_name')
    s_date = django_filters.DateFromToRangeFilter(field_name = "start_date")
    e_date = django_filters.DateFromToRangeFilter(field_name = "due_date")



    class Meta:
        model = Job
        fields = ['title','location','category','tag','s_date','e_date']


