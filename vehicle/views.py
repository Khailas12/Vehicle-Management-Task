from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from . import models, forms



@login_required(login_url='login_user')
def create(request):
    context = {}
    form = forms.VehicleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Vehicle Details Created Successfully')
        return redirect('super_admin_page')
    
    context['form'] = form
    return render(request, "CRUD/create.html", context)


@login_required(login_url='login_user')
def update(request, id):
    context = {}
    
    obj = get_object_or_404(models.VehicleModel, id=id)
    form = forms.VehicleForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        messages.success(request, 'Vehicle Details Updated Successfully')
        form.save()
    
    context['form'] = form
    return render(request, "CRUD/update.html", context)


@login_required(login_url='login_user')
def delete(request, id):
    context = {}
    obj = get_object_or_404(models.VehicleModel, id=id)
    
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Vehicle Details Deleted Successfully')
        return redirect('super_admin_page')
    
    return render(request, 'CRUD/delete.html', context)
