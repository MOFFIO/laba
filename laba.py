#coding:utf-8

from lxml import etree
import json

class Car(object):

    def __init__(self, id, brand, price, attributes):
        self.id = id
        self.brand = brand
        self.price = price
        self.attributes = attributes

    def __repr__(self):
        return '<Car_id=%s_brand=%s>' % (self.id, self.brand)

    def car_as_dict(self):
        car = {
                'id' : self.id,
                'brand' : self.brand,
                'price' : self.price,
                'paint' : self.attributes.paint,
                'tires' : self.attributes.tires,
                'trim' : self.attributes.trim
                }
        return car

class CarAttributes(object):

    def __init__(self, paint, tires, trim):
        self.paint = paint
        self.tires = tires
        self.trim = trim


class Dealership(object):

    def __init__(self, car_list, name):
        self.car_list = car_list
        self.name = name

    def add_cars(self, cars):
        for item in cars:
            car_attr = CarAttributes(item[3], item[4], item[5])
            carr = Car(item[0], item[1], item[2], car_attr)
            self.car_list.append(carr)

    def __repr__(self):
        return 'Dealer_name=%s' % (self.name)

    def get_car(self, id):
        for item in self.car_list:
            if item.id == id:
                return item

    def update_car(self, id, new_value):
        car = self.get_car(id)
        if car:
            if new_value[0] in ('brand', 'price'):
                setattr(car, new_value[0], new_value[1])
            elif new_value[0] in ('paint', 'tires', 'trim'):
                setattr(car.attributes, new_value[0], new_value[1])
            return 'Car Updated'
        return 'Car not found'

    def sell_car(self, id):
        car = self.get_car(id)
        if car:
            self.car_list.remove(car)
            return 'Car Sold'
        return 'Car not found'

    def set_discount(self, id, discount_value):
        car = self.get_car(id)
        if car:
            car.price = int(car.price * discount_value / 100)
            return 'The Discount is set'
        return 'Car not found'

    def car_filter(self, values):
        car_filter_list = []
        car_list = self.car_list
        for value in values:
            for carr in car_list:
                if value[0] in ('brand', 'price') and value[1] == getattr(carr, value[0]):
                    car_filter_list.append(carr)
                if value[0] in ('paint', 'tires', 'trim') and value[1] == getattr(carr.attributes, value[0]):
                    car_filter_list.append(carr)
            car_list = car_filter_list[:]
            car_filter_list = []
        return car_list


    def car_amount(self):
        return len(self.car_list)

    def sync_xml_cars(self, file_adress='/home/moffio/my_python/cars.xml'):
        tree = etree.parse(file_adress)
        rawss = tree.findall('vehicle')
        all_cars = []
        for idd, raw in enumerate(rawss, start=1):
            car = [
                idd,
                raw.get('make'),
                int(raw.xpath('price')[0].text),
                raw.xpath('color')[0].text,
                raw.xpath('tires')[0].text,
                'Regular'
            ]
            all_cars.append(car)
        self.add_cars(all_cars)

    def car_list_to_json(self):
        json_cars = []
        for car in self.car_list:
            json_cars.append(car.car_as_dict())
        return json.dumps(json_cars, indent = 4, ensure_ascii=False)






car1 = Car(1, 'Ford', 23000, CarAttributes('Red', 'Rain', 'Level-1'))
car2 = Car(2, 'BMW', 46000, CarAttributes('Blue', 'Regular', 'Regular'))
car3 = Car(3, 'Ferrari', 150000, CarAttributes('Violet', 'Regular', 'Level-2'))
car4 = Car(4, 'Toyota', 26000, CarAttributes('Black', 'Snow', 'Regular'))
car5 = Car(5, 'BMW', 50000, CarAttributes('Red', 'Sport', 'Level-3'))
car6 = Car(6, 'Lotus', 50000, CarAttributes('Grey', 'Sport', 'Regular'))
car7 = Car(7, 'Audi', 40000, CarAttributes('Blue', 'Regular', 'Level-2'))
car8 = Car(8, 'Audi', 45000, CarAttributes('Blue', 'Rain', 'Regular'))
car9 = Car(9, 'Ford', 30000, CarAttributes('Violet', 'Sport', 'Level-1'))
car10 = Car(10, 'Toyota', 32000, CarAttributes('Green', 'Show', 'Level-2'))
car11 = Car(11, 'Ferrari', 200000, CarAttributes('Green', 'Sport', 'Level-1'))
car12 = Car(12, 'VAZ', 15000, CarAttributes('Blue', 'Rain', 'Level-2'))

dealership1 = Dealership([car1, car2, car3, car10], 'KMac')
dealership2 = Dealership([car4, car5, car6, car7], 'JRM')
dealership3 = Dealership([car8, car9], 'YPeng')


p1List = [
    [11, 'Mercedes', 40000, 'Grey', 'Snow', 'Regular'],
    [12, 'Ford', 20000, 'Red', 'Rain', 'Level-1'],
]


p2List = []


p3List = [
    [13, 'Mercedes', 40000, 'Grey', 'Snow', 'Regular'],
    [14, 'Mercedes', 40000, 'Blue', 'Snow', 'Regular'],
    [15, 'Mercedes', 40000, 'Orange', 'Snow', 'Regular'],
]



