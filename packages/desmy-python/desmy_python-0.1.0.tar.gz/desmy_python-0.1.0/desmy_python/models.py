from django.db import models
from django.core.paginator import Paginator
from django.db.models import Q

class DesmyManager(models.Manager):
    def createOrUpdate(self, defaults=None, **kwargs):
        obj, created = self.update_or_create(defaults=defaults, **kwargs)
        return obj, created
    
    def delete(self, **kwargs):
        return super().filter(**kwargs).delete()

    def read(self, **kwargs):
        return super().filter(**kwargs)

    def readWithPaginated(self, page=1, per_page=10, search_query=None, sort_by=None, **kwargs):
        queryset = super().filter(**kwargs)
        
        if search_query:
            search_filters = Q()
            for field in self.model._meta.get_fields():
                if isinstance(field, models.CharField) or isinstance(field, models.TextField):
                    search_filters |= Q(**{f"{field.name}__icontains": search_query})
            queryset = queryset.filter(search_filters)
        
        if sort_by:
            queryset = queryset.order_by(sort_by)
        
        paginator = Paginator(queryset, per_page)
        return paginator.get_page(page)

    def update(self, pk, **kwargs):
        return super().filter(pk=pk).update(**kwargs)

    def create(self, **kwargs):
        return super().create(**kwargs)
