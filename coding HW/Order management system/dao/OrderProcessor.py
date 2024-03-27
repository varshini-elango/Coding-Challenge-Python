import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.IOrderManagementRepository import IOrderManagementRepository
from Util.DBConnUtil import DBUtil
from Entity.Product import *
from exception.OrderManagementException import OrderNotFound,UnauthorizedAccess
from exception.OrderManagementException import UserNotFound


class OrderProcessor(IOrderManagementRepository):

    
    def createOrder(self, user, order_id, product_id, quantity, order_date):
        
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
            
            sql_query = f"INSERT INTO orders (orderId,userId, productId, quantity, orderDate) VALUES ({order_id},'{user.getUserId()}', {product_id}, {quantity}, '{order_date}')"
            cursor.execute(sql_query)
            conn.commit()
            
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    def cancelOrder(self, userId, orderId):
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
           
            cursor.execute("SELECT * FROM orders WHERE userId = ? AND orderId = ?", (userId, orderId))
            order_exists = cursor.fetchone()
            if order_exists:
                
                cursor.execute("DELETE FROM orders WHERE userId = ? AND orderId = ?", (userId, orderId))
                conn.commit()
            else:
                raise OrderNotFound("Order not found")
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.close()
            conn.close()

    def createProduct(self, user, product):
        
        conn = DBUtil.getDBConn()
        
        cursor = conn.cursor()
        try:
           
            if user.getRole() == "Admin":
                
                cursor.execute("INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                            (product.getProductId(), product.getProductName(), product.getDescription(), product.getPrice(), product.getQuantityInStock(), product.getType()))

               
                if isinstance(product, Electronics):
                   
                    cursor.execute("INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)",
                                (product.getProductId(), product.getBrand(), product.getWarrantyPeriod()))
                elif isinstance(product, Clothing):
                    
                    cursor.execute("INSERT INTO Clothing (productId, color, size) VALUES (?, ?, ?)",
                                (product.getProductId(), product.getColor(), product.getSize()))

               
                conn.commit()
                print("Product Created Successfully!!")
            else:
                
                raise UnauthorizedAccess("User is not authorized to create products")
        except Exception as e:
            # Rollback the transaction in case of any error
            conn.rollback()
            # Raise an exception or handle it as appropriate
            raise e
        finally:
            # Close the cursor and database connection
            cursor.close()
            conn.close()


    def createUser(self, user):
        
        conn = DBUtil.getDBConn()
        
        cursor = conn.cursor()
        try:
            
            cursor.execute("INSERT INTO users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                        (user.getUserId(), user.getUsername(), user.getPassword(), user.getRole()))
            
            conn.commit()
            print("User Created Successfully")
        except Exception as e:
            
            conn.rollback()
            
            print(str(e))
        finally:
            
            cursor.close()
            conn.close()


    def getAllProducts(self):
        
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
            
            cursor.execute("SELECT * FROM Product")
            products = []
            for row in cursor.fetchall():
                product = Product(row[0], row[1], row[2], row[3], row[4], row[5])
                products.append(product)
            return products
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

    def getOrderByUser(self, user):
         
        
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
          
            cursor.execute("SELECT * FROM orders WHERE userId = ?", (user.getUserId(),))
            orders = cursor.fetchall()
            return orders
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

    def getUserByUsernameAndPassword(self, username, password):
        
        conn = DBUtil.getDBConn()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user_data = cursor.fetchone()
            if user_data:
               
                userId, username, password, role = user_data
                user = User(userId, username, password, role)
                return user
            else:
                return None
        except Exception as e:
            
            print(str(e))
        finally:
            cursor.close()
            conn.close()

