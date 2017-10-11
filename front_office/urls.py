from django.conf.urls import url, include
from. import views
from django.contrib.auth.views import login,logout


urlpatterns = [
        url(r'^$',views.frontof,name='frontof'),
        url(r'^report/$',views.report,name='report'),
        url(r'^medicallab/$',views.medicallab,name='medicallab'),
        url(r'^medicalprovider/$',views.medicalp,name='medicalp'),
        url(r'^medicaldecision/(?P<patient_id>\d+)/$',views.medicaldecision ,name="medicaldecision"),
        url(r'^login/$',login, {'template_name':'login.html'}),
        url(r'^logout/$',views.logout_view,name='logout'),

        url(r'^home/',views.home),
        # url(r'^search/$',views.search,name='search')
]