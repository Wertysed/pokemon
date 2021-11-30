import requests
from collections.abc import Iterator
from typing import Union
from typing import Any
from dataclasses import dataclass
from functools import lru_cache



url = 'https://pokeapi.co/api/v2/pokemon/132'

url_stats = 'https://pokeapi.co/api/v2/stat/132'


class PokeError(Exception):
    pass


@dataclass
class BasePokemon:
    abobus: Any
    name: str

    def __init__(self, abobus: Any):
        self._name = abobus['name']

    def __str__(self):
        return f'name {self._name}'

    def __repr__(self):
        return f'name {self._name}'


@dataclass
class Pokemon(BasePokemon):
    __id: str
    __height: int
    __weight: int

    def __init__(self, abobus: Any):
        BasePokemon.__init__(self, abobus)
        self.__id = abobus['id']
        # self.__name = abobus['name']
        self.__height = abobus['height']
        self.__weight = abobus['weight']

    def __gt__(self, other: Any):
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
        raise PokeError('introduced something incorrect')


class PokemonStats:
    pass


class PokemonAPI:

    @staticmethod
    @lru_cache
    def get_pokemon(argument: Union[int, str]):

        if not isinstance(argument, (int, str)):
            raise PokeError('introduced something incorrect, only str or int')

        elif isinstance(argument, (int, str)):
            url_1 = f'https://pokeapi.co/api/v2/pokemon/{argument}'
            bibus = requests.get(url_1).json()
            return Pokemon(bibus)

    @staticmethod
    def get_all(get_full: bool = False) -> Iterator:
        try:
            number = 1
            if not get_full:
                number = 1
                while number < 50:
                    try:
                        print(number)
                        url_2 = f'https://pokeapi.co/api/v2/pokemon/{number}'
                        bibus_1 = requests.get(url_2).json()
                        yield BasePokemon(bibus_1)
                        number += 1
                    except PokeError:
                        print('Pasta')

            else:
                while number < 50:
                    # print('все должно работать', number)
                    yield PokemonAPI.get_pokemon(number)
                    number += 1
                    print()
        except PokeError:
            print('Some pasta')


#abobus = requests.get(url_stats).json()
abobus = requests.get(url).json()
ditto = Pokemon(abobus)
print('Задание №1')
print(ditto)

c = PokemonAPI.get_pokemon(1)
for i in range(51):
    p = PokemonAPI.get_pokemon(i + 2)
    if c > p:
        c = c
    else:
        c = p
print('самый большой', c)
print('без кеширования', PokemonAPI.get_pokemon.cache_info())
c = PokemonAPI.get_pokemon(1)
for i in range(51):
    p = PokemonAPI.get_pokemon(i + 2)
    if c > p:
        c = c
    else:
        c = p

print('самый большой', c)
print('c кешированием', PokemonAPI.get_pokemon.cache_info())
# g = PokemonAPI.get_all(1231)
# while True:
#    print(next(g))
#
print("реализация исключения")
f = PokemonAPI.get_pokemon(78.33)
