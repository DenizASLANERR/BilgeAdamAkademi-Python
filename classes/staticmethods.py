##### STATIC METHODS #####
# Static method, sınıfa ya da örneklere ait olmayan, genel amaçlı fonksiyonlardır.
# Bunlar, sınıfın veya örneklerin durumuna erişim gerektirmez ve genelde yardımcı
# fonksiyonlar olarak kullanılır.

class Mathematics:
    @staticmethod
    def add5(number):
        return number + 5

    @staticmethod
    def sub5(number):
        return number - 5

    @staticmethod
    def mul5(number):
        return number * 5

    @staticmethod
    def div5(number):
        return number / 5

    @staticmethod
    def print_sth():
        print("This is a static method")


x = 10

Mathematics.print_sth()
Mathematics.add5(x)
Mathematics.sub5(x)
Mathematics.mul5(x)
Mathematics.div5(x)

m1 = Mathematics()
m1.div5(x)

# math modülü
import math

math.sqrt(x)


