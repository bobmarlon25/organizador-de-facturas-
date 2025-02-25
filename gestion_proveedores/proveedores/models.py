from django.db import models

class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    logo = models.ImageField(upload_to='supplier', null=True, blank=True)  # For images

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=10, unique=True)  # Unique ID for customers
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Invoice(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    invoice_number = models.CharField(max_length=50, unique=True)  # Unique invoice number
    invoice_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='invoice_images/', null=True, blank=True)  # For images

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.supplier.first_name} ({self.invoice_date})"