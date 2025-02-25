from django.shortcuts import render, get_object_or_404
from .models import Customer,Supplier,Invoice


#supplier= provedores
def index(request):
    
    
    return render(request, 'inicio.html')


def supplier_list(request):
    
    suppliers = Supplier.objects.all()
    context = {
        'suppliers': suppliers,
    }
    return render(request, 'proveedores.html', context)


def supplier_info(request, supplier_id):
    # Intentar obtener el proveedor
    supplier = Supplier.objects.get(id=supplier_id)

    if not supplier:
        # Si el proveedor no existe, renderizar una página de error personalizada
        return render(request, 'error.html', {'message': 'El proveedor no existe.'}, status=404)

    # Obtener todas las facturas asociadas a ese proveedor
    invoices = Invoice.objects.filter(supplier=supplier)

    # Pasar los datos al template
    context = {
        'supplier': supplier,
        'invoices': invoices,
    }

    return render(request, 'Invoice.html', context)





def invoice_detail(request, invoice_id):
    # Obtener la factura con el ID proporcionado o mostrar error 404 si no existe
    invoice = get_object_or_404(Invoice, id=invoice_id)

    # Obtener el proveedor (vendedor) de la factura
    supplier = invoice.supplier

    # Obtener el cliente de la factura (asumiendo que hay un campo 'client' en Invoice)
    client = invoice.customer

    # Pasar los datos al template
    context = {
        'invoice': invoice,
        'supplier': supplier,
        'client': client,
    }

    return render(request, 'invoice-detail.html', context)