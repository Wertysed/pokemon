import requests
from collections.abc import Iterator

url = 'https://pokeapi.co/api/v2/pokemon/132'


class BasePokemon:
    def __init__(self, abobus):
        self._name = abobus['name']

    def __str__(self):
        return f'name {self._name}'

    def __repr__(self):
        return f'name {self._name}'


class Pokemon(BasePokemon):
    def __init__(self, abobus):
        BasePokemon.__init__(self, abobus)
        self.__id = abobus['id']
        # self.__name = abobus['name']
        self.__height = abobus['height']
        self.__weight = abobus['weight']

    def __gt__(self, other):
        return self.__weight > other.__weight


    def __str__(self):
        return f'id {self.__id} ' \
               f'name {self._name} ' \
               f'height {self.__height} ' \
               f'weight {self.__weight} '

    def __repr__(self):
        return f'id {self.__id} ' \
               f'name {self._name} ' \
               f'height {self.__height} ' \
               f'weight {self.__weight} '

    def get_stats(self, stats: str):
        if stats == 'id':
            return self.__id
        elif stats == 'name':
            return self._name
        elif stats == 'height':
            return self.__height
        elif stats == 'weight':
            return self.__weight
        elif stats == 'all':
            return f'id {self.__id} ' \
                   f'name {self._name} ' \
                   f'height {self.__height} ' \
                   f'weight {self.__weight} '
        raise ValueError


class PokemonAPI:
    @staticmethod
    def get_pokemon(argument):
        url_1 = f'https://pokeapi.co/api/v2/pokemon/{argument}'
        bibus = requests.get(url_1).json()
        return Pokemon(bibus)

    @staticmethod
    def get_all(get_full: bool = False) -> Iterator:
        number = 1
        if not get_full:
            number = 1
            while number < 51:
                print(number)
                url_2 = f'https://pokeapi.co/api/v2/pokemon/{number}'
                bibus_1 = requests.get(url_2).json()
                yield BasePokemon(bibus_1)
                number += 1

        else:
            while number < 50:
                #print('все должно работать', number)
                yield PokemonAPI.get_pokemon(number)
                number += 1


abobus = requests.get(url).json()
ditto = Pokemon(abobus)
print(ditto)
c = PokemonAPI.get_pokemon(1)
for i in range(51):
    p = PokemonAPI.get_pokemon(i + 2)
    if c > p:
        c = c
    else:
        c = p
print('самый большой', c)

