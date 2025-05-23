#abstraction
# from abc import ABC,abstractmethod
# class juicemaker(ABC):  #cant create obj for juicemaker 'ABC' method
#     @abstractmethod
#     def makejuice1(Self):
#         pass
# class orangejuice(juicemaker):
#     def makejuice1(self):
#         print("ornage juice processing")
# class mangojucie(juicemaker):
#     def makejuice(self):
#         print("mango juice processing")
# obj=orangejuice()
# obj.makejuice1()

#online debit upi using abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using UPI.")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using Card.")

class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paid Rs.{amount} using NetBanking.")

def process_payment(method, amount):
    method.pay(amount)

UPI_obj = UPI()
card_obj = Card()
net_obj = NetBanking()

process_payment(UPI_obj, 500)
process_payment(card_obj, 1000)
process_payment(net_obj, 750)
