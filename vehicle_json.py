# -*- coding: utf-8 -*-
import mimesis
import typing
import datetime
import random
import json
import argparse
import logging

"""
車データJSONサンプルデータ作成
https://lk-geimfari.github.io/mimesis/
"""
parser = argparse.ArgumentParser(prog='vehicle_json', usage='%(prog)s [--lines] [--log]')
parser.add_argument("--lines", help="number of lines", type=int, default=100)
parser.add_argument("--log", help="log level", choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'], type=str,
                    default='WARN')


class Owner(object):
    """所有者"""

    def __init__(self, owner_id: int):
        self.id = owner_id  # type: int
        self.first_name = None  # type: str
        self.last_name = None  # type: str
        self.address = None # type: str


class Vehicle(object):
    """Vehicle"""

    def __init__(self, vehicle_id: int):
        self.id = vehicle_id  # type: int
        self.name = None  # type: str
        self.code = None  # type: str
        self.owner = None  # type: Owner
        self.vehicle_date = None  # type: datetime.date
        self.temparature = None # type: int


def next_owner(data_locale: str) -> typing.Iterator[Owner]:
    personal = mimesis.Person(data_locale)
    address = mimesis.Address(data_locale)
    owner_id = 0

    while True:
        owner_id += 1

        owner = Owner(owner_id)
        owner.first_name = personal.name()
        owner.last_name = personal.surname()
        owner.address = address.address()

        yield owner


def next_vehicle(owners: typing.List[Owner], data_locale: str) -> typing.Iterator[Vehicle]:
    vehicle_id = 0
    transport = mimesis.Transport(data_locale)
    vehicle_date = mimesis.Datetime(data_locale)
    numbers = mimesis.Numbers(data_locale)

    while True:
        vehicle_id += 1

        vehicle = Vehicle(vehicle_id)
        vehicle.name = transport.car().title()
        vehicle.code = transport.vehicle_registration_code(data_locale)
        vehicle.owner = random.choice(owners)
        vehicle.vehicle_date = vehicle_date.date(start=1800, end=2018).isoformat()
        vehicle.temparature = numbers.integer_number(start=-30, end=50)

        yield vehicle


class SimpleJsonEncoder(json.JSONEncoder):
    """JSONエンコーダ、オブジェクトの __dict__ の内容でエンコードする"""

    def default(self, o):
        return o.__dict__


def generate_vehicles(data_locale: str, n_owners: int, n_vehicles: int) -> typing.Iterator[Vehicle]:
    owner_generator = next_owner(data_locale)
    owner = [next(owner_generator) for _ in range(n_owners)]

    car_generator = next_vehicle(owner, data_locale)
    return (next(car_generator) for _ in range(n_vehicles))


def main():
    args = parser.parse_args()

    #data_locale = 'ja'
    data_locale = 'en'
    n_owners = args.lines
    n_vehicles = args.lines
    vehicles = generate_vehicles(data_locale, n_owners=n_owners, n_vehicles=n_vehicles)
    encoder = SimpleJsonEncoder()

    with open(f'vehicles_{data_locale}.json', 'w') as wf:
        for b in vehicles:
            print(encoder.encode(b), file=wf)


if __name__ == '__main__':
    main()
