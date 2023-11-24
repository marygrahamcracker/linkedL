class soda ():
    def __init__(self, name: str = '', calories: int = 0, Isdiet: bool = False) -> None:
        self._name:str = name
        self._calories:int = calories
        self._Isdiet:bool = Isdiet

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
            self._name = value

    @property
    def calories(self) -> int:
        return self._calories
    @calories.setter
    def calories(self, value:int):
        self._calories = value

    @property
    def Isdiet(self) -> bool:
        return self._Isdiet
    @Isdiet.setter
    def Isdiet(self, value:bool):
        self._Isdiet = value

mysoda = soda('sunkist')
mysoda.calories = 0 
mysoda.Isdiet = True
print(f'the soda im drinking is {mysoda.name}, it has {mysoda.calories} calories, and its {mysoda.Isdiet} that its diet')