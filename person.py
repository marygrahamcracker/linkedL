class person():
    def __init__(self, name: str = '') -> None:
        self._name:str = name
        self._needstopee: bool = True

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
            self._name = value

    @property
    def needstopee(self) -> bool:
        return self._needstopee
    def gotobatheroom(self):
        self._needstopee = False

class woman(person):
    @property
    def gender(self) -> str:
        return 'female'
    
class man(person):
    @property
    def gender(self) -> str:
        return 'male'

battery = person() #<--- instanciated
#object - instance of a class
#string is alpha numeric
#funcion = behavior
#we store data in variables
#if anything is going under with indentation use :
#properties = expose data
#variable = store data
#constructor = initilizes data
#getters and setters are part of a construct called properties
#in a property, getters store data
#setters

mypeople = (person('mike'), person('mary'), person('felicity'))
firstperson = mypeople[0]
secondperson = mypeople [1]
thirdperson = mypeople[2]
