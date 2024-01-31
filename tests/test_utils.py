import pytest

from src.utils import conversion_date, sorting_operations_by_date, get_only_executed, get_output_date


def test_conversion_date():
    assert conversion_date("2018-06-30T02:08:58.425572") == "30.06.2018"


def test_sorting_operations_by_date():
    date = [
        {
            "id": 142264268,
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "date": "2019-03-23T01:09:46.296404"
        },
        {
            "id": 214024827,
            "date": "2018-12-20T16:43:26.929246"
        },
        {
            "id": 522357576,
            "date": "2019-07-12T20:41:47.882230"
        }
    ]
    sorting_date = [
        {
            "id": 522357576,
            "date": "2019-07-12T20:41:47.882230"
        },
        {
            "id": 142264268,
            "date": "2019-04-04T23:20:05.206878"
        },
        {
            "id": 873106923,
            "date": "2019-03-23T01:09:46.296404"
        },
        {
            "id": 214024827,
            "date": "2018-12-20T16:43:26.929246"
        }
    ]
    assert sorting_operations_by_date(date) == sorting_date


def test_get_only_executed():
    date = [
        {
            "id": 863064926,
            "state": "EXECUTED"
        },
        {
            "id": 594226727,
            "state": "CANCELED"
        },
        {
            "id": 147815167,
            "state": "EXECUTED"
        }
    ]
    executed_date = [
        {
            "id": 863064926,
            "state": "EXECUTED"
        },
        {
            "id": 147815167,
            "state": "EXECUTED"
        }
    ]
    assert get_only_executed(date) == executed_date


@pytest.mark.parametrize('array, type_in_array, expected', [
    ({
         "id": 147815167,
         "state": "EXECUTED",
         "date": "2018-01-26T15:40:13.413061",
         "operationAmount": {
             "amount": "50870.71",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод с карты на счет",
         "from": "Maestro 4598300720424501",
         "to": "Счет 43597928997568165086"
     }, dict, f'26.01.2018 Перевод с карты на счет\n' f'Maestro 4598 30** **** 4501 -> Счет **5086\n' f'50870.71 руб.'),
    ({
         "id": 172864002,
         "state": "EXECUTED",
         "date": "2018-12-28T23:10:35.459698",
         "operationAmount": {
             "amount": "49192.52",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Открытие вклада",
         "to": "Счет 96231448929365202391"
     }, dict, f'28.12.2018 Открытие вклада\n' f' -> Счет **2391\n' f'49192.52 USD')
])
def test_get_output_date(array, type_in_array, expected):
    assert get_output_date(array, ) == expected








