from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new_customer/$', views.new_customer, name='new_customer'),
    url(r'^modify_customer/$', views.customer_list, name='customer_list'),
    url(r'^modify_customer/(?P<pk>[0-9]+)/$', views.customer_update, name='customer_update'),
    url(r'^new_provider/$', views.new_provider, name='new_provider'),
    url(r'^modify_provider/$', views.provider_list, name='provider_list'),
    url(r'^modify_provider/(?P<pk>[0-9]+)/$', views.provider_update, name='provider_update'),
    url(r'^new_solution/$', views.new_solution, name='new_solution'),
    url(r'^new_solution/customer_search/$', views.new_solution_customer, name='new_solution_customer'),
    url(r'^new_solution/provider_search/$', views.new_solution_provider, name='new_solution_provider'),
    url(r'^solution_search/$', views.solution_search, name='solution_search'),
    url(r'^solution_close/$', views.solution_close, name='solution_close'),
    url(r'^solution_email/$', views.solution_email, name='solution_email'),
]