from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class ContactInfo(models.Model):
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class ShippingAddress(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    # TODO Will need more info from possible API for shipping details.
    # TODO will also need to figure out what Facebook marketplace will need to post things to their API.
    title = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    depth = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    description = models.TextField()
    image = models.ImageField()
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




