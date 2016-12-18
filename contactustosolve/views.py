from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Customer, Provider
from .forms import CustomerForm, ProviderForm

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html", {})

def new_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.office = request.user.profile.office
            customer.save()
    else:
        form = CustomerForm()
    
    context = {'form': form}
    return render(request, "new_customer.html", context)

def customer_list(request):
    currOffice = request.user.profile.office
    query = request.GET.get('q', '')
    if query:
        # query example
        results = Customer.objects.filter(customerName__icontains=query, office=currOffice).order_by('customerName')
    else:
        results = None
    
    context = {'customers': results}
    return render(request, "search_customer.html", context)

def customer_update(request, pk):
    instance = get_object_or_404(Customer, pk=pk)
    context = {'instance': instance}
    template = "modify_customer.html"

    if request.POST:
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            customer = form.save(commit=False)
            customer.office = instance.office
            customer.pk = instance.pk
            customer.save()
            template = "success.html"
        
    else:
        return render(request, template, context)
    
    return render(request, template, context)

def new_provider(request):
    template = "new_provider.html"
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.office = request.user.profile.office
            provider.save()
            template = "new_provider_success.html"
    else:
        form = ProviderForm()
        print(request.user.profile.office)
    
    return render(request, template, {'instance': form})

def provider_list(request):
    currOffice = request.user.profile.office
    query = request.GET.get('q', '')
    if query:
        # query example
        results = Provider.objects.filter(providerName__icontains=query, office=currOffice).order_by('providerName')
    else:
        results = None
    
    context = {'providers': results}
    return render(request, "search_provider.html", context)

def provider_update(request, pk):
    instance = get_object_or_404(Provider, pk=pk)
    context = {'instance': instance}
    template = "modify_provider.html"

    if request.POST:
        form = ProviderForm(request.POST)
        
        if form.is_valid():
            provider = form.save(commit=False)
            provider.office = instance.office
            provider.pk = instance.pk
            provider.save()
            template = "modify_provider_success.html"
        
    else:
        return render(request, template, context)
    
    return render(request, template, context)
