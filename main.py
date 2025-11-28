class Base:
    def show(self):
        print("Base")

class Mixin:
    def show(self):
        print("Mixin")

class Child(Mixin, Base):
    pass

c = Child()
c.show()