import random
from tqdm import tqdm

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from faker import Faker
from core.models import UserGender, UserStatus, UserKind, UserType, UserTheme

User = get_user_model()


def fake_lite_info():
    first_name = Faker().first_name()
    last_name = Faker().last_name()
    random_number = Faker().random_int(min=0, max=15)
    email = f"{first_name.lower()}.{last_name.lower()}.{random_number}@example.com"
    return first_name, last_name, email


class Command(BaseCommand):
    help = "Generate dummy data for User and Address models"

    def handle(self, *args, **options):
        fake = Faker()

        num_users = 1000  # Number of users to create
        created_by = User.objects.last()
        for _ in tqdm(range(num_users)):
            first_name, last_name, email = fake_lite_info()
            phone = "+8801" + fake.msisdn()[:-4]
            try:
                user = User.objects.create(
                    uid=fake.uuid4(),
                    phone=phone,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    country="bd",
                    language=fake.language_code(),
                    slug=fake.slug(),
                    created_by =created_by,
                    gender=random.choice([choice[0] for choice in UserGender.choices]),
                    status=random.choice([choice[0] for choice in UserStatus.choices]),
                    date_of_birth=fake.date_of_birth(),
                    code=fake.random_int(min=100000, max=999999),
                    user_kind=random.choice([choice[0] for choice in UserKind.choices]),
                    user_type=random.choice([choice[0] for choice in UserType.choices]),
                    theme=random.choice([choice[0] for choice in UserTheme.choices]),
                )
                user.set_password("password")
                user.save()
            except IntegrityError:
                pass

        self.stdout.write(self.style.SUCCESS(f"Created dummy users"))
