global store
codes = ('1', '2', '3', '4', '5')
store = {
    '1': {'name': 'Papel', 'required': 'Tabaco, Cerillas, Filtros y Green', 'flag': False, 'request': None},
    '2': {'name': 'Tabaco', 'required': 'Papel, Cerillas, Filtros y Green', 'flag': False, 'request': None},
    '3': {'name': 'Cerillas', 'required': 'Papel, Tabaco, Filtros y Green', 'flag': False, 'request': None},
    '4': {'name': 'Filtros', 'required': 'Papel, Tabaco, Cerillas y Green', 'flag': False, 'request': None},
    '5': {'name': 'Green', 'required': 'Papel, Tabaco, Cerillas y Filtros', 'flag': False, 'request': None},
}

time_smoke = 5
time_sleep = 1
packet_size = 1024
