from django.db.models.expressions import OuterRef
from .models import Tool, Lease
from django.db.models import Exists


def get_owned_tools(user):
    leased = Lease.objects.filter(thing=OuterRef('pk'), stop__isnull=True)
    return user.tool_set.all().annotate(leased=Exists(leased))


def get_available_tools():
    return Tool.objects.filter(~Exists(
        Lease.objects.filter(thing=OuterRef('pk'),
                             stop__isnull=True)))


def get_borrowed_tools(user):
    return Tool.objects.filter(Exists(
        Lease.objects.filter(thing=OuterRef('pk'),
                             lessee=user, stop__isnull=True)))
