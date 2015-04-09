import django_filters

from .models import Owner, Service, Facility, FacilityGPS


class OwnerFilter(django_filters.FilterSet):
    class Meta:
        model = Owner


class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service


class FacilityGPSFilter(django_filters.FilterSet):
    class Meta:
        model = FacilityGPS


class FacilityFilter(django_filters.FilterSet):
    beds = django_filters.NumberFilter(name='number_of_beds')
    cots = django_filters.NumberFilter(name='number_of_cots')
    open_whole_day = django_filters.BooleanFilter(name='open_whole_day')
    open_whole_week = django_filters.BooleanFilter(name='open_whole_week')
    county = django_filters.CharFilter(name='sub_county__county')

    class Meta:
        model = Facility
        fields = [
            'beds', 'cots', 'open_whole_week', 'open_whole_day', 'sub_county',
            'county', 'facility_type', 'owner', 'status', 'name', 'services'
        ]
