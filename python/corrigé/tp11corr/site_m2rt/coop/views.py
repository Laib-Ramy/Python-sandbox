from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddToolForm
from .models import Tool


def home(request):
    addform = AddToolForm()
    context = {'addform': addform}
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
