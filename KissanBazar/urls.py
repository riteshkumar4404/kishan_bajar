"""Kissan_Bazar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from KB import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^$',views.home,name='home'),
	url(r'^contact/$',views.contact,name='contact'),
	url(r'^info/$',views.info,name='info'),
	#url(r'^logout/$',auth_views.LogoutView.as_view(),name="logout"),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^login/$',views.login,name='login'),
	#url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
	url(r'^userdetails/$',views.userdetails,name='userdetails'),
	url(r'^navcategory/$',views.navcategory,name='navcategory'),
	#url(r'^navcategory/$',views.navcategory,name='navcategory'),
	url(r'^logout/$',views.logout1,name='logout'),
	url(r'^changepassword/(?P<pk>\d+)/$',views.changepassword,name='changepassword'),
	url(r'^myaccount/(?P<pk>\d+)/$',views.myaccount,name='myaccount'),
	#url(r'^contact/$',views.contact,name='contact'),
	#url(r'^contactiflogin/(?P<pk>\d+)/$',views.contactiflogin,name='contactiflogin'),
	#url(r'^$',views.home,name='home'),
	url(r'^useractivate/(?P<pk>\d+)/$',views.useractivate,name='useractivate'),
	url(r'^userdeactivate/(?P<pk>\d+)/$',views.userdeactivate,name='userdeactivate'),
	url(r'^prodactivate/(?P<pk>\d+)/$',views.prodactivate,name='prodactivate'),
	url(r'^proddeactivate/(?P<pk>\d+)/$',views.proddeactivate,name='proddeactivate'),
	url(r'^cateactivate/(?P<pk>\d+)/$',views.cateactivate,name='cateactivate'),
	url(r'^catedeactivate/(?P<pk>\d+)/$',views.catedeactivate,name='catedeactivate'),
	url(r'^admin1/$',views.admin1,name='admin1'),
	url(r'^admin1/users/$',views.user,name='user'),
	url(r'^admin1/products/$',views.product,name='product'),
	url(r'^admin1/categories/$',views.category,name='categories'),
	url(r'^admin1/purchased/$',views.purchase,name='purchased'),
	url(r'^buynow/$',views.buynow,name='buynow'),
	url(r'^invoice/$',views.invoice,name='invoice'),
	url(r'^particular/$',views.checking,name='checking'),
	url(r'^searchresults/$',views.search,name='search'),]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
