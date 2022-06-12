import pytest
from pytest_factoryboy import register
from tests.users.factories import UserFactory, RegularUserFactory, CompanyFactory, ServiceFactory, AddressFactory


register(UserFactory)
register(RegularUserFactory)
register(CompanyFactory)
register(ServiceFactory)
register(AddressFactory)


@pytest.fixture
def user_create(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def regular_user_create(db, regular_user_factory):
    regular_user = regular_user_factory.create()
    return regular_user


@pytest.fixture
def company_create(db, company_factory):
    company = company_factory.create()
    return company


@pytest.fixture
def service_create(db, service_factory):
    service = service_factory.create()
    return service


@pytest.fixture
def address_create(db, address_factory):
    address = address_factory.create()
    return address