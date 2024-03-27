import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abc import ABC, abstractmethod
from Entity.Product import User, Product
from datetime import date

class IOrderManagementRepository(ABC):
    @abstractmethod
    def createOrder(self, user: User,order_id, product_id: int, quantity: int, order_date: date) -> None:
       pass
    
    @abstractmethod
    def cancelOrder(self, userId: int, orderId: int) -> None:
        pass
    
    @abstractmethod
    def createProduct(self, user: User, product: Product) -> None:
        pass
    
    @abstractmethod
    def createUser(self, user: User) -> None:
       pass
    
    @abstractmethod
    def getAllProducts(self) -> list[Product]:
       pass
    
    @abstractmethod
    def getOrderByUser(self, user: User) -> list[Product]:
        pass

    @abstractmethod
    def getUserByUsernameAndPassword(self, username, password):
       pass