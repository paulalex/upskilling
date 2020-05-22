class HotelBooker:
    def find_hotel(self):
        return "Hotel Booker is finding hotels....."

class FlightBooker:
    def find_flight(self):
        return "Flight Booker is finding flights....."


class CarBooker:
    def find_car(self):
        return "Car Booker is finding cars....."

class InsuranceBooker:
    def find_insurance(self):
        return "Insurance Booking is finding insurance deals....."

class BookingCoordinator:
    _hotel_booker = HotelBooker()
    _flight_booker = FlightBooker()
    _car_booker = CarBooker()
    _insurance_booker = InsuranceBooker()

    def find_deals(self):
        print(self._hotel_booker.find_hotel(), end="\n")
        print(self._flight_booker.find_flight(), end="\n")
        print(self._car_booker.find_car(), end="\n")
        print(self._insurance_booker.find_insurance(), end="\n")

if __name__ == "__main__":
    coordinator = BookingCoordinator()

    coordinator.find_deals()
    