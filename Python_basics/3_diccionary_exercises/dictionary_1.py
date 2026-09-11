# Cree un diccionario que guarde la siguiente información sobre un hotel:
#   nombre
#   numero_de_estrellas
#       habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
#           numero
#           piso
#           precio_por_noche



room_1 = {
            "room_number": 1,
            "floor": 1,
            "night_price": 1000.50
}
room_2 = {
            "room_number": 2,
            "floor": 2,
            "night_price": 1000.50
}

my_hotel = {
    "name" : "WOW ROOMS DELUXE",
    "stars" : 4.7,
    "rooms" : [room_1,room_2],
}
# OR ------------------------------------------------------------ INLINE
# my_hotel = {
#     "name": "WOW ROOMS DELUXE",
#     "stars": 4.7,
#     "rooms": [
#         {"room_number": 1, "floor": 1, "night_price": 1000.50},
#         {"room_number": 2, "floor": 2, "night_price": 1000.50}
#     ]
# }