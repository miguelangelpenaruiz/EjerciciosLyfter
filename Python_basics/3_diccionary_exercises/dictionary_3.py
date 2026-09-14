# Cree un programa que use una lista para eliminar keys de un diccionario.

list_key_to_eliminate = ['password', 'id_government']

personal_information = {
    'name':'Miguel',
    'last_name':'Peña',
    'email': 'mmiigguel@live.com',
    'password': 'Chachoman_22',
    'id_government': 'MAPR010321'
}

for index in range(len(list_key_to_eliminate)):
    personal_information.pop(list_key_to_eliminate[index])

print(personal_information)
#