from django.contrib import admin
from .models import Company, Employee, Product, Service


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "num_employees", "num_chairs", "ticker")
    list_filter = ("num_employees", "num_chairs")
    search_fields = ("name", "ticker")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "salary")
    list_filter = ("company", "salary")
    search_fields = ("name", "company__name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    list_filter = ("company",)
    search_fields = ("name", "company__name")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
    list_filter = ("company",)
    search_fields = ("name", "company__name")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
