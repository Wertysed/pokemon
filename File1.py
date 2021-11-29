import requests

url = 'https://pokeapi.co/api/v2/pokemon/ditto'


class BasePokemon:
    def __init__(self, abobus):
        self._name = abobus['name']

    def __str__(self):
        return f'name {self._name}'


class Pokemon(BasePokemon):
    def __init__(self, abobus):
        BasePokemon.__init__(self, abobus)
        self.__id = abobus['id']
        # self.__name = abobus['name']
        self.__height = abobus['height']
        self.__weight = abobus['weight']

    def __str__(self):
        return f'id {self.__id} ' \
               f'name {self._name} ' \
               f'height {self.__height} ' \
               f'weight {self.__weight} '

    def get_stats(self, stats:str):
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


abobus = requests.get(url).json()
ditto = Pokemon(abobus)
print(ditto.get_stats('id'))
print(ditto)
