# bc-ferries-reservations
A simple script to scrape all available BC Ferries reservations in a date range

Sample output:

```
HSB -> LNG: Mon 2022-08-01 7:30 AM Sold Out
HSB -> LNG: Mon 2022-08-01 9:50 AM Sold Out
HSB -> LNG: Mon 2022-08-01 12:10 PM Sold Out
HSB -> LNG: Mon 2022-08-01 12:55 PM Sold Out
HSB -> LNG: Mon 2022-08-01 2:25 PM Sold Out
HSB -> LNG: Mon 2022-08-01 3:15 PM Sold Out
HSB -> LNG: Mon 2022-08-01 4:45 PM Sold Out
HSB -> LNG: Mon 2022-08-01 5:30 PM Sold Out
HSB -> LNG: Mon 2022-08-01 7:05 PM AVAILABLE
HSB -> LNG: Mon 2022-08-01 9:25 PM AVAILABLE
HSB -> LNG: Mon 2022-08-01 11:30 PM AVAILABLE

HSB -> LNG: Tue 2022-08-02 7:30 AM Sold Out
HSB -> LNG: Tue 2022-08-02 9:50 AM Sold Out
HSB -> LNG: Tue 2022-08-02 12:10 PM Sold Out
HSB -> LNG: Tue 2022-08-02 2:25 PM Sold Out
HSB -> LNG: Tue 2022-08-02 4:45 PM AVAILABLE
HSB -> LNG: Tue 2022-08-02 7:05 PM AVAILABLE
HSB -> LNG: Tue 2022-08-02 9:25 PM AVAILABLE
HSB -> LNG: Tue 2022-08-02 11:30 PM AVAILABLE

HSB -> LNG: Wed 2022-08-03 7:30 AM Sold Out
HSB -> LNG: Wed 2022-08-03 9:50 AM Sold Out
HSB -> LNG: Wed 2022-08-03 12:10 PM Sold Out
HSB -> LNG: Wed 2022-08-03 2:25 PM Sold Out
HSB -> LNG: Wed 2022-08-03 4:45 PM Sold Out
HSB -> LNG: Wed 2022-08-03 7:05 PM AVAILABLE
HSB -> LNG: Wed 2022-08-03 9:25 PM AVAILABLE
HSB -> LNG: Wed 2022-08-03 11:30 PM AVAILABLE
```

## Installation

We use pyenv to isolate the environment. You don't have to if you don't want to.

```
pyenv install 3.10.4
pyenv virtualenv 3.10.4 bc-ferries-reservations
pyenv activate bc-ferries-reservations
pip install -r requirements.txt
```

## Usage

You can get the 3-letter terminal codes by inspecting the dropdowns in bcferries.com.

```
python3 reservations.py <departure terminal> <arrival terminal> <start date> <end date>
```

Example:

```
python3 reservations.py HSB LNG 2022-08-01 2022-08-03
```
