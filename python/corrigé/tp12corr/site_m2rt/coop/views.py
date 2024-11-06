from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models.functions import Now
from .forms import AddToolForm
from .models import Tool, Lease
from .utility import get_available_tools, get_borrowed_tools, get_owned_tools


def home(request):
    addform = AddToolForm()
    context = {'addform': addform}
    context['available'] = get_available_tools()
    if request.user.is_authenticated:
        context['owned'] = get_owned_tools(request.user)
        context['borrowed'] = get_borrowed_tools(request.user)
    return render(request, "coop/home.html", context)


def add_tool(request):
    form = AddToolForm(request.POST)
    if form.is_valid():
        description = form.cleaned_data['description']
        price = form.cleaned_data['price']
        tool = Tool(owner=request.user, description=description, price=price)
        tool.save()
    return redirect('home')


def delete_tools(request):
    to_delete = [int(s) for s in request.POST.getlist('to_delete')]
    Tool.objects.filter(id__in=to_delete).delete()
    return redirect('home')

def borrow_tools(request):
    to_borrow=[int(s) for s in request.POST.getlist('to_borrow')]
    for tid in to_borrow:
        l=Lease(lessee=request.user, thing=Tool.objects.get(pk=tid))
        l.save()
    return redirect('home')

def restitute_tools(request):
    to_restitute=[int(s) for s in request.POST.getlist('to_resitute')]
    Lease.objects.filter(thing__in=to_restitute).update(stop=Now())
    return redirect('home')