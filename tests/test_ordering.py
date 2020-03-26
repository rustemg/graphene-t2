import graphene

from graphene_metafora import DjangoObjectType, Queries

from tests.data.models import Organization


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization
        fields = ("id", "full_name", "registration_date")

    class Metafora:
        can_order_by = "id", "registration_date"
        default_ordering = "-registration_date"


class Query(Queries):
    class Metafora:
        enable_ordering_for = "__auto__"

    organizations = graphene.List(OrganizationType)

    def resolve_organizations(self, info):
        return Organization.objects.all()


def test_ordering_kwarg_exist():
    assert "sort_by" in Query.organizations.kwargs
