import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        r = os.path.splitext(self.photo_file_name)
        return r[1]


class Car(CarBase):

    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):

    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        if body_whl == '' or body_whl.count('x') != 2:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)
        else:
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):

    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if row[0] == 'car' and row[2] != 0:
                car_list.append(Car(brand=row[1], photo_file_name=row[3], carrying=row[5], passenger_seats_count=row[2]))
            elif row[0] == 'truck' and row[4] != 0:
                car_list.append(Truck(brand=row[1], photo_file_name=row[3], carrying=row[5], body_whl=row[4]))
            elif row[0] == 'spec_machine' and row[6] != 0:
                car_list.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6]))
            else:
                break


    return car_list


# cars = get_car_list('C:\Python\Example\\cars.csv')
# len(cars)
# for car in cars:
#     print(type(car))