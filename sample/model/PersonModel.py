from .Model import Model


class Person():
    def __init__(self, **kw):
        self.name = kw.get('name', None)
        self.age = kw.get('age', 0)
        self.birth = kw.get('birth', None)
        self.death = kw.get('death', None)
        self.father = kw.get('father', 0)
        self.mother = kw.get('mother', 0)
        self.childrens = kw.get('childrens', [])

    def
