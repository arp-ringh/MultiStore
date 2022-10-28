"""
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

"""


from django.shortcuts import render

from apps.store.models import CustomUser
from apps.vendor.models import Vendor
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View

from django.contrib.auth import login, logout
from django.contrib import messages, auth

from apps.vendor.decorators import vendor_required
from django.contrib.auth.decorators import login_required

from .forms import VendorSignUpForm
# Create your views here.

class vendorSignUpView(CreateView):
    model = CustomUser
    form_class = VendorSignUpForm
    template_name = 'registration/vendor_register.html'


    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        vendor = Vendor.objects.create(name=user.username,created_by=user)
        return redirect('vendor:vendordash')


@login_required
@vendor_required
def vendorDash(request):
    views = {}

    return render(request, 'vendor/vendor-dash.html', views )


