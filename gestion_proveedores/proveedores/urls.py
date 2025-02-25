
from django.urls import path
from . import views 

app_name='proveedores'



urlpatterns = [
    path('',views.index,name='index'),
    path('proveedores',views.supplier_list,name='proveedores'),
    path('proveedores/<int:supplier_id>',views.supplier_info,name='proveedores'),
    path('invoice/<int:invoice_id>',views.invoice_detail,name='invoice')


]