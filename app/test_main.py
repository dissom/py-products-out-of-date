import datetime
from unittest import mock
from pytest import mark

from app.main import outdated_products


@mark.parametrize(
    "products, expected_result",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600,
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120,
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160,
                },
            ], ["duck"]
        ),
        (
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 1, 10),
                    "price": 50,
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2021, 12, 15),
                    "price": 100,
                },
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2022, 1, 5),
                    "price": 30,
                },
            ], ["milk", "cheese", "yogurt"]
        ),
        (
            [
                {
                    "name": "soda",
                    "expiration_date": datetime.date(2021, 10, 20),
                    "price": 20,
                },
                {
                    "name": "cookies",
                    "expiration_date": datetime.date(2023, 1, 1),
                    "price": 15,
                },
                {
                    "name": "chips",
                    "expiration_date": datetime.date(2021, 6, 30),
                    "price": 40,
                },
            ], ["soda", "chips"]
        )
    ],
)
@mock.patch("app.main.datetime")
def test_outdated_product(
    mocked_date_today: mock.Mock,
    products: list[dict],
    expected_result: list[str],
) -> None:
    mocked_date_today.date.today.return_value = datetime.date(2022, 2, 2)
    assert outdated_products(products) == expected_result
