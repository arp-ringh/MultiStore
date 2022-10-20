from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Vendor

# Create your views here.

def vendor_apply(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('store:frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/vendor-apply.html', {'form':form})


