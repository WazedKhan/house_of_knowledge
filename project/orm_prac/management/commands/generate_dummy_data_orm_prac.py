import random
from django.core.management.base import BaseCommand
from faker import Faker
from orm_prac.models import Company, Employee, Product, Service

fake = Faker()


class Command(BaseCommand):
    help = "Generate thousands of dummy data records for the models."

    def handle(self, *args, **kwargs):
        num_companies = 1000  # Adjust the number of companies you want to create

        for _ in range(num_companies):
            # Create a Company
            company = Company.objects.create(
                name=fake.company(),
                num_employees=random.randint(1, 1000),
                num_chairs=random.randint(1, 1000),
                ticker=fake.unique.lexify(text="????"),
            )

            # Create Employees for the Company
            num_employees = random.randint(1, 50)
            for _ in range(num_employees):
                Employee.objects.create(
                    company=company,
                    name=fake.name(),
                    salary=random.uniform(30000, 150000),
                )

            # Create Products for the Company
            num_products = random.randint(1, 10)
            for _ in range(num_products):
                Product.objects.create(company=company, name=fake.unique.word())

            # Create Services for the Company
            num_services = random.randint(1, 10)
            for _ in range(num_services):
                Service.objects.create(company=company, name=fake.unique.word())

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully generated dummy data for {num_companies} companies."
            )
        )
