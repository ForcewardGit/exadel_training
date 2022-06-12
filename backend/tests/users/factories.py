import random
from faker import Faker
from users.models import User, RegularUser, Company, Service, Address
from factory import SubFactory
from factory.django import DjangoModelFactory


fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = "new_user"
    password = "user_new_password_1234"


class RegularUserFactory(DjangoModelFactory):
    class Meta:
        model = RegularUser
    
    user = SubFactory(UserFactory)
    name = fake.first_name()
    surname = fake.last_name()

    
class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service

    name = fake.text(max_nb_chars = 30)
    avg_price = random.randint(1, 10000)


class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Company
    
    user = SubFactory(UserFactory)
    name = fake.text(max_nb_chars = 30)
    rating = round(random.uniform(0.00, 5.00), 2)
    cost_per_hour = random.randint(1, 10000)


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    user_id = SubFactory(RegularUserFactory)
    country = fake.text(max_nb_chars = 30)
    city = fake.text(max_nb_chars = 50)
    street = fake.text(max_nb_chars = 50)
    house_number = random.randint(1, 10000)
    ap_number = random.randint(1, 10000)
