import pytest
from faker import Faker
from django.urls import reverse
from offers.models import Offer
from users.models import User, RegularUser, Company


pytestmark = pytest.mark.django_db
fake = Faker()


class TestOfferEndpoints:
    def create_offer(self):
        regular_user = RegularUser.objects.create(
            username = "test_username_1",
            password = "test_password_name",
            name = fake.first_name(), surname = fake.last_name()
        )
        company = Company.objects.create(
            username = "another_test_user",
            password = "test_password_name",
            name = "Exadel"
        )

        offer = {
            "user": regular_user.id,
            "company": company.id
        }

        return offer


    def test_list(self, api_client):
        url = reverse("offers")
        response = api_client.get(url)

        assert response.status_code == 200

    
    def test_create(self, api_client):
        offer = self.create_offer()
        url = reverse("offers")
        response = api_client.post(url, data = offer)

        assert response.status_code == 201
        assert Offer.objects.count() == 1

    
    def test_detail(self, api_client):
        offer = self.create_offer()
        offer_obj = Offer.objects.create(
            user = RegularUser.objects.get(pk = offer["user"]),
            company = Company.objects.get(pk = offer["company"])
        )

        url = reverse("offer", args=[offer_obj.id])
        response = api_client.get(url)

        assert response.status_code == 200
        assert response.data["user"] == offer_obj.user.id
        assert response.data["company"] == offer_obj.company.id
    

    def test_update(self, api_client):
        offer = self.create_offer()
        offer_obj = Offer.objects.create(
            user = RegularUser.objects.get(pk = offer["user"]),
            company = Company.objects.get(pk = offer["company"])
        )
        new_user = User.objects.create_user(username = "another_test_user_new", password = "test_password_name")
        new_company = Company.objects.create(user = new_user, name = "Epam")

        url = reverse("offer", args=[offer_obj.id])
        response_old = api_client.get(url)

        put_data = {
            "user": offer_obj.user.id,
            "company": new_company.id,
        }

        response_new = api_client.put(url, data = put_data)

        assert response_new.status_code == 200
        assert response_new.data["user"] == response_old.data["user"]
        assert response_old.data["company"] != response_new.data["company"]
    

    def test_delete(self, api_client):
        offer = self.create_offer()
        offer_obj = Offer.objects.create(
            user = RegularUser.objects.get(pk = offer["user"]),
            company = Company.objects.get(pk = offer["company"])
        )

        url = reverse("offer", args=[offer_obj.id])
        response = api_client.delete(url)

        assert response.status_code == 204
        with pytest.raises(Offer.DoesNotExist):
            Offer.objects.get(id = offer_obj.id)
