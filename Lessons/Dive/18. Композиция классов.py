# Композиция классов или наследование?
class Pet:
    pass

class Dog(Pet):
    pass

class ExportJSON(Pet):
    pass

class ExDog(Dog, ExportJSON):
    pass
# Композиция VS наследование
class ExportJSON:
    def to_json(self):
        pass

class ExportXML:
    def to_xml(self):
        pass

class ExDog(Dog, ExportJSON, ExportXML):
      pass

# >>> dog = ExDog("Фокс", "мопс")
# >>> dog.to_xml()
# >>> dog.to_json()
### Композиция классов против наследования, пример буду вводить в онлайн

import json


class Pet:
    def __init__(self, name):
        self,name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportXML(PetExport):
    def export(self, dog):
        return """<xml version="1.0" encoding="utf-8">
<dog>
  <name>{0}</name>
  <breed>{1}</breed>
</dog>""".format(dog.name, dog.breed)


class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed,
        })


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)

        self._exporter = exporter or ExportJSON()

        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad export instance value", exporter)

    def export(self):
        return self._exporter.export(self)


# >>> fox = ExDog("Фокс", "мопс", exporter=ExportXML())
# >>> print(fox.export())
# <xml version="1.0" encoding="utf-8">
# <dog>
#   <name>Фокс</name>
#   <breed>мопс</breed>
# </dog>
# >>>
# >>> muhtar = ExDog("Мухтар", "питбуль")
# >>> print(muhtar.export())
{"name": "\u0414\u0436\u0435\u043a", "breed": "\u043c\u043e\u043f\u0441"}