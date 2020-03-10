class A(object):
    a = "A"

    def __init__(self):
        self.b = "B"

    class Meta:
        c= "C"

    def a_print(self):
        print('a_print')

    @classmethod
    def class_print(cls):
        print(cls.__name__)
        print('class_print')

    @staticmethod
    def static_print():
        print('static_print')

    @property
    def data(self):
        print('data')

    def is_valid(self):
        self.a_print()

    def __str__(self):
        return '__str__'

    def save(self):
        print('a_save')



# print(A.a)
# print(A.b)
# print(A().a)
# print(A().b)
# print(A().Meta.c)
# A.a_print(A())
# A.class_print()
# A.static_print()
# A.data
# A().a_print()
# A().class_print()
# A().static_print()
# A().data
# print(A())


class B(object):
    A=A()


    def save(self):
        print('save')

B.A.a_print()

# BookInfo.objects.get()
B().save()
A().save()