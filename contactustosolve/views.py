from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import Customer, Provider, Solutions
from .forms import CustomerForm, ProviderForm
from _datetime import datetime

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html", {})

def new_customer(request):
    template = "new_customer.html"
    context = {}
    if request.method == "POST":
        form = CustomerForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            customer = form.save(commit=False)
            customer.office = request.user.profile.office
            customer.save()
            context = {'customer': customer}
            template = "new_customer_success.html"
    else:
        form = CustomerForm()
        context = {'form': form}
    
    return render(request, template, context)

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
    context = {}
    if request.method == "POST":
        form = ProviderForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            provider = form.save(commit=False)
            provider.office = request.user.profile.office
            provider.save()
            context = {'provider': provider}
            template = "new_provider_success.html"
    else:
        form = ProviderForm()
        context = {'form': form}
    
    return render(request, template, context)

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

def new_solution_customer(request):
    currOffice = request.user.profile.office
    query = request.POST.get('q', '')
    if query:
        # query example
        results = Customer.objects.filter(customerName__icontains=query, office=currOffice).order_by('customerName')
    else:
        results = None
    
    context = {'customers': results}
    return render(request, "solution_search_customer.html", context)

def new_solution_provider(request):
    currOffice = request.user.profile.office
    pk = request.POST.get('customer_id')
    customer = get_object_or_404(Customer, pk=pk)
    query = request.POST.get('q', '')
    if query:
        # query example
        results = Provider.objects.filter(activity__icontains=query, office=currOffice).order_by('providerName')
    else:
        results = None
    
    context = {'providers': results, 'customer': customer}
    return render(request, "solution_search_provider.html", context)

def new_solution(request):
    template = "new_solution.html"
    c_id = request.POST['customer_id']
    customer = get_object_or_404(Customer, pk=c_id)
    p_id = request.POST['provider_id']
    provider = get_object_or_404(Provider, pk=p_id)
    context = {'customer': customer, 'provider': provider}

    if request.POST.get("solution_save", ""):
        solution = Solutions()
        solution.office = request.user.profile.office
        solution.customer = customer
        solution.provider = provider
        solution.save()
        context = {'solution': solution}
        template = "new_solution_success.html"

    return render(request, template, context)

def solution_search(request):
    currOffice = request.user.profile.office
    results = ""
    template = "solution_search.html"
    if request.POST.get('q', ''):
        # query example
        query = request.POST.get('q', '')
        results = Solutions.objects.filter(pk=query, office=currOffice)
    
    if request.POST.get('p', ''):
        # query example
        query = request.POST.get('p', '')
        providers = Provider.objects.filter(providerName__icontains=query, office=currOffice)
        for p in providers:
            results = Solutions.objects.filter(provider=p, office=currOffice)
        
    context = {'solutions': results}
    
    if request.POST.get("selected_solution", ""):
        pk = request.POST['solution_id']
        solution = get_object_or_404(Solutions, pk=pk)
        context = {'solution': solution }
        template = "solution_detail.html"
        
    return render(request, template, context)

def solution_close(request):
    pk = request.POST['solution_id']
    solution = get_object_or_404(Solutions, pk=pk)
    solution.status = True
    solution.closingDateTime = datetime.now()
    solution.save()
    context = {'solution': solution }
    template = "solution_close.html"
        
    return render(request, template, context)

def solution_email(request):
    pk = request.POST['solution_id']
    solution = get_object_or_404(Solutions, pk=pk)
    context = {'solution': solution }
    html_content = render_to_string('email.html', context)
    cimzett = solution.provider.email
    msg = EmailMultiAlternatives('Ügyfél érkezik', html_content, 'noreply@contactustosolve.hu', [cimzett])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    solution.sendToProvider = True
    solution.save()
            
    return render(request, 'solution_email.html', context)