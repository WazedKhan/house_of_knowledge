from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    num_employees = models.PositiveIntegerField(blank=True)
    num_chairs = models.PositiveIntegerField(blank=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="employees"
    )
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Service(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="services"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
