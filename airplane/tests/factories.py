import factory

from airplane.models import Airplane


class AirplaneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Airplane

    airplane_id = factory.Sequence(lambda n: n)
    passengers_count = factory.Faker("pyint", min_value=0, max_value=20)
    user_id = factory.Sequence(lambda n: n)
    created = factory.Faker("date_time")
