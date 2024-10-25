from abc import ABC,abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_riders(self,rider):
        self.riders.append(rider)
    
    def add_drivers(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders {len(self.riders)} and drivers{len(self.drivers)}'

class Users(ABC):
    def __init__(self, name , email,nid) -> None:
        self.name = name
        self.email = email
        self.current_ride = None
        # To do set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(Users): #customer
    def __init__(self, name, email, nid,current_location,initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Rider: with name  {self.name} and email {self.email}')

    def load_cash(self,amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self,ride_sharing, destination):
        if not self.current_ride:
            
            ride_request = Ride_request(self, destination)
            ride_matcher = Ride_matching(ride_sharing.drivers)
            ride  = ride_matcher.find_driver(ride_request)
            print('got the ride',ride)
            self.current_ride = ride
    
    def show_current_ride(self):
        print(self.current_ride)


class Driver(Users):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f'Driver : With name {self.name} and email {self.email}')

    def accept_ride(self,ride):
        ride.set_driver(self)
    
class Ride:
    def __init__(self,start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,rider,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride details: {self.start_location} to {self.end_location}'

class Ride_request:
    def __init__(self,rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self,drivers) -> None:
        self.avaiable_drivers = drivers

    def find_driver(self,ride_request):
        if len(self.avaiable_drivers) > 0:
            #to do: find the closet driver of the rider
            print('Looking for a driver')
            driver = self.avaiable_drivers[0]
            ride = Ride(ride_request.rider.current_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride


class Vehicle(ABC):

    speed = {
        'car' : 50,
        'bike': 60,
        'cng' : 30

    }

    def __init__(self, vehicle_type, licens_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.licens_plate = licens_plate
        self.rate = rate
        self.status = 'available'

        super().__init__()
    @abstractmethod
    def start_driving(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, licens_plate, rate) -> None:
        super().__init__(vehicle_type, licens_plate, rate)
    
    def start_driving(self):
        self.status = 'unavailable'


class Bike(Vehicle):
    def __init__(self, vehicle_type, licens_plate, rate) -> None:
        super().__init__(vehicle_type, licens_plate, rate)
    
    def start_driving(self):
        self.status = 'unavailable'


# check the class integration
        
pathaw = Ride_sharing('PATHAW')
sakib = Rider('Sakib','sakib@gmail.com',12123,'Mirpur',1200)
pathaw.add_riders(sakib)

rohim = Driver('Rohim','rohim@gmail.com',1231231,'Mohamadpur')

pathaw.add_drivers(rohim)
print(pathaw)

sakib.request_ride(pathaw,'Uttara')
sakib.show_current_ride()

