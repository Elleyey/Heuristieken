GROUND_LENGTH = 180 # meter
GROUND_WIDTH = 160 # meter
WATER_SURF = 0.2 * GROUND_WIDTH * GROUND_LENGTH # square meter;
                                                # hoogte-breedteverhouding
                                                # tussen 1 en de 4
model # 20, 40 of 60 woningen

class Eengezinswoning:
    house_length = 8 # meter
    house_width = 8 # meter
    price = 285 # thousand euro
    vrijstand = 2 # meter
    xtra_vrijstand # meter
    xtra_vrijstand_value = 0.03 # added value to price per extra meter vrijstand
    value = xtra_vrijstand * xtra_vrijstand_value + price
    aantal = 0.6 * model

class Bungalow:
    house_length = 10 # meter
    house_width = 7.5 # meter
    price = 399 # thousand euro
    vrijstand = 3 # meter
    xtra_vrijstand # meter
    xtra_vrijstand_value = 0.04 # added value to price per extra meter vrijstand
    value = xtra_vrijstand * xtra_vrijstand_value + price
    aantal = 0.25 * model

class Maison:
    house_length = 11 # meter
    house_width = 10.5 # meter
    price = 610 # thousand euro
    vrijstand = 6 # meter
    xtra_vrijstand # meter
    xtra_vrijstand_value = 0.06 # added value to price per exta meter vrijstand
    value = xtra_vrijstand * xtra_vrijstand_value + price
    aantal = 0.15 * model
