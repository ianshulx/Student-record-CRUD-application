from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

admin.site.site_header = "Students Records Management"
admin.site.site_title = "Welcome to admin Dashboard"
admin.site.index_title= "Students Record Management"
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),

    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('home', views.menu, name='home'),
    path('export', views.export, name='export'),
    path('exportfee', views.export_fee, name='exportfee'),
    path('notice', views.notice, name='notice'),
    path('noticefile', views.noticefile, name='noticefile'),
    

    path('list', views.stu_list, name='list'),
    path('add', views.HomeView.as_view(), name='adddata'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
    path('app/<int:pk>', views.application_form, name='application'),
    path('fee', views.fee, name='fee'),
   

 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
