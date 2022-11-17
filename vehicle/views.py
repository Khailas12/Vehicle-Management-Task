from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from . import models, forms


def create(request):
    context = {}
    form = forms.VehicleForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Vehicle Details Created Successfully')
        return redirect('super_admin_page')
    
    context['form'] = form
    return render(request, "CRUD/create.html", context)



# def read(request):
#     context = {}
#     context['dataset'] = models.VehicleModel.objects.all()
#     return render(request, 'CRUD/read.html', context)


# def user_read(request, id):
#     context = {}
#     obj = get_object_or_404(models.VehicleModel, id=id)
    
#     context['data'] = obj
#     return render(request, 'CRUD/user_read.html', context)


def update(request, id):
    context = {}
    
    obj = get_object_or_404(models.VehicleModel, id=id)
    form = forms.VehicleForm(request.POST or None, instance=obj)
    
    if form.is_valid():
        msg = messages.success(request, 'Vehicle Details Updated Successfully')
        form.save()
    
    
    context['form'] = form
    return render(request, "CRUD/update.html", context)


def delete(request, id):
    context = {}
    obj = get_object_or_404(models.VehicleModel, id=id)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('super_admin_page')
    
    return render(request, 'CRUD/delete.html', context)