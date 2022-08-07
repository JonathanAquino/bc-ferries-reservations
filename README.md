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

For the 3-letter terminal codes, see below.

```
python3 -u reservations.py <departure terminal> <arrival terminal> <start date> <end date>
```

Example:

```
python3 -u reservations.py HSB LNG 2022-08-01 2022-08-03
```

### Terminal codes

| Terminal | Terminal Code |
| --- | --- |
| Bella Bella (McLoughlin Bay) | PBB |
| Bella Coola | BEC |
| Bowen Island (Snug Cove) | BOW |
| Brentwood Bay | BTW |
| Buckley Bay | BKY |
| Campbell River | CAM |
| Chemainus | CHM |
| Comox (Little River) | CMX |
| Cormorant Island (Alert Bay) | ALR |
| Cortes Island (Whaletown) | COR |
| Crofton | CFT |
| Denman Island East (Gravelly Bay) | DNE |
| Denman Island West | DNM |
| Gabriola Island (Descanso Bay) | GAB |
| Galiano Island (Sturdies Bay) | PSB |
| Graham Island (Skidegate) | PSK |
| Hornby Island (Shingle Spit) | HRN |
| Klemtu | KLE |
| Malcolm Island (Sointula) | SOI |
| Mayne Island (Village Bay) | PVB |
| Mill Bay | MIL |
| Moresby Island (Alliford Bay) | ALF |
| Nanaimo (Departure Bay) | NAN |
| Nanaimo (Duke Point) | DUK |
| Nanaimo (Nanaimo Harbour) | NAH |
| Ocean Falls | POF |
| Pender Island (Otter Bay) | POB |
| Penelakut Island (Telegraph Harbour) | PEN |
| Port Hardy (Bear Cove) | PPH |
| Port McNeill | MCN |
| Powell River (Saltery Bay) | SLT |
| Powell River (Westview) | PWR |
| Prince Rupert | PPR |
| Quadra Island (Heriot Bay) | HRB |
| Quadra Island (Quathiaski Cove) | QDR |
| Salt Spring Island (Fulford Harbour) | FUL |
| Salt Spring Island (Long Harbour) | PLH |
| Salt Spring Island (Vesuvius Bay) | VES |
| Saturna Island (Lyall Harbour) | PST |
| Shearwater | SHW |
| Sunshine Coast (Earls Cove) | ERL |
| Sunshine Coast (Langdale) | LNG |
| Texada Island (Blubber Bay) | TEX |
| Thetis Island (Preedy Harbour) | THT |
| Vancouver (Horseshoe Bay) | HSB |
| Vancouver (Tsawwassen) | TSA |
| Victoria (Swartz Bay) | SWB |
