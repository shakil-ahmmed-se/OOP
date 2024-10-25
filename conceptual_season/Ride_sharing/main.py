from abc import ABC, abstractmethod
class Ride_sharing:
    def __init__(self,company_name,) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []

    def add_driver(self,driver):
        self.drivers.append(driver)
    
    def add_rider(self,rider):
        self.riders.append(rider)
    
    def __repr__(self) -> str:
        return f'{self.company_name} has {len(self.riders)} Riders and {len(self.drivers)} Drivers'
    
class User(ABC):
    def __init__(self,name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def disply_profile(self):
        raise NotImplementedError
    
class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location = current_location
        super().__init__(name, email, nid)
    
    def disply_profile(self):
        print(f'Driver name is {self.name} and email is {self.email}')


class Rider(User):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_location = current_location
        self.current_ride = None
        super().__init__(name, email, nid)

        
    def disply_profile(self):
        print(f'Rider name is {self.name} and email is {self.email}')

    def ride_request(self,uber, destination):
        if not self.current_ride:
            ob = Ride_matching(uber.drivers)
            res = ob.available_driver(self,destination)
            print('Your result is',res)
            return res


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location

    def start_ride(self):
        pass
    def end_ride(self):
        pass
    def __repr__(self) -> str:
        return f'Start from {self.start_location} to {self.end_location}'
    
class Ride_matching:
    def __init__(self,drivers) -> None:
        self.drivers = drivers

    def available_driver(self,rider,destination):
        if len(self.drivers) > 0:
            ride = Ride(rider.current_location,destination)
            return ride
        else:
            print('Sorry, Driver not Available')
    

uber = Ride_sharing('Uber')
driver = Driver('Alice','alice@gmail.com', 1231,'Mirpur')
sakib = Rider('Sakib','sakib@gmail.com',123123,'Uttara')

uber.add_driver(driver)
uber.add_rider(sakib)

sakib.ride_request(uber,'Dhaka')