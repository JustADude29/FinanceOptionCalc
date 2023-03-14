from django.urls import include, re_path

from django.contrib import admin
from calc.views import blackScholes, index
from calc.BinomialModel_views import binomialIndex, Binomial
admin.autodiscover()


urlpatterns = [
    #Black-Scholes
    re_path(r'^$', index, name='index'),
    re_path(r'^catalog', index, name='index'),
    re_path(r'^blackScholes_index', index, name='index'),
    re_path(r'^blackScholes/S(.+)sigma(.+)r(.+)T(.+)K(.+)call_put(.+)/$', blackScholes, name='blackScholes'),

    #Binomial model
    re_path(r'^binomial_index', binomialIndex, name='binomial'),
    re_path(r'^binomial/S(.+)K(.+)n(.+)d(.+)u(.+)r(.+)/$', Binomial, name='n-step Binomial'),
    re_path(r'^binomial/S(.+)K(.+)T(.+)r(.+)sigma(.+)N(.+)call_put(.+)/$', Binomial, name='n-step Binomial'),
]
