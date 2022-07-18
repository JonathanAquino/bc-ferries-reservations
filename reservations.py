# A simple script to scrape all available BC Ferries reservations in a date range.
#
# Usage:
# python3 reservations.py <departure terminal> <arrival terminal> <start date> <end date>
#
# You can get the 3-letter terminal codes by inspecting the dropdowns in bcferries.com.
#
# Example:
# python3 reservations.py HSB LNG 2022-08-01 2022-08-03

import sys
from datetime import datetime, timedelta
from collections import namedtuple
import requests
from bs4 import BeautifulSoup

departure_terminal = sys.argv[1]
arrival_terminal = sys.argv[2]
start_date = sys.argv[3]
end_date = sys.argv[4]

Reservation = namedtuple("Reservation", "dt, departure_time, sold_out")

def fetch_reservations(departure_terminal, arrival_terminal, dt):
    """
    Fetch the reservations for a given date.
    """
    session = requests.Session()

    print('Loading BC Ferries homepage for %s' % dt.strftime('%a %Y-%m-%d'))
    response = session.get('https://www.bcferries.com/')
    soup = BeautifulSoup(response.text, 'html.parser')
    print('Loaded: %s' % soup.title.string.strip())
    csrf_token = soup.find('input', {'name': 'CSRFToken'})['value']

    print('Submitting terminals and date')
    response = session.post('https://www.bcferries.com/view/FareFinderComponentController/PassengerInfo', {
        'routeInfoForm.tripType': 'SINGLE',
        'routeInfoForm.departureLocation': departure_terminal,
        'routeInfoForm.arrivalLocation': arrival_terminal,
        'routeInfoForm.departingDateTime': dt.strftime('%m/%d/%Y'),
        'CSRFToken': csrf_token,
    })
    soup = BeautifulSoup(response.text, 'html.parser')
    print('Loaded: %s' % soup.title.string.strip())
    csrf_token = soup.find('input', {'name': 'CSRFToken'})['value']

    print('Submitting passenger info')
    response = session.post('https://www.bcferries.com/view/FareFinderComponentController/next-step', {
        'passengerInfoForm.passengerTypeQuantityList[0].quantity': '1',
        'CSRFToken': csrf_token,
    })
    soup = BeautifulSoup(response.text, 'html.parser')
    print('Loaded: %s' % soup.title.string.strip())
    csrf_token = soup.find('input', {'name': 'CSRFToken'})['value']

    print('Submitting vehicle details')
    response = session.post('https://www.bcferries.com/view/FareFinderComponentController/search', {
        'vehicleInfoForm.vehicleInfo[0].vehicleType.code': 'UH_standard',
        'vehicleInfoForm.vehicleInfo[0].qty': '1',
        'CSRFToken': csrf_token,
    })
    soup = BeautifulSoup(response.text, 'html.parser')
    print('Loaded: %s' % soup.title.string.strip())

    reservations = []
    table = soup.find('div', {'class': 'table-responsive'})
    rows = table.find_all('div', {'class': 'p-card'})
    for row in rows:
        departure_time = row.find('div', {'class': 'fnt-24 ferrytime'}).find('b').string.strip()
        sold_out = True if row.find('p', {'class': 'sold-out-red-text'}) else False
        reservations.append(Reservation(dt, departure_time, sold_out))

    print()
    return reservations

def dates_between(start_dt, end_dt):
    """
    Generate a list of dates between two dates.
    """
    delta = end_dt - start_dt
    return [start_dt + timedelta(days=i) for i in range(delta.days + 1)]

all_reservations = []
start_dt = datetime.strptime(start_date, '%Y-%m-%d')
end_dt = datetime.strptime(end_date, '%Y-%m-%d')
for dt in dates_between(start_dt, end_dt):
    reservations = fetch_reservations(departure_terminal, arrival_terminal, dt)
    all_reservations.extend(reservations)

previous_dt = None
for reservation in all_reservations:
    if previous_dt != reservation.dt:
        print()
    date = reservation.dt.strftime('%a %Y-%m-%d')
    print('%s -> %s: %s %s %s' % (departure_terminal, arrival_terminal, date, reservation.departure_time, 'Sold Out' if reservation.sold_out else 'AVAILABLE'))
    previous_dt = reservation.dt
