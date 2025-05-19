from coffee import Coffee
from customer import Customer

coffee1 = Coffee("Latte")
coffee2 = Coffee("Robusta")
coffee3 = Coffee("Cappucchino")
coffee4 = Coffee("Arabica")
coffee5 = Coffee("Expresso")    

customer1 = Customer("Eunice")
customer2 = Customer("Joram")
customer3 = Customer("George")
customer4 = Customer("Austin")
customer5 = Customer("Nadia")


customer1.create_order(coffee1, 5.0)
customer1.create_order(coffee2, 7.3)
customer3.create_order(coffee3, 6.8)
customer4.create_order(coffee4, 4.6)
customer5.create_order(coffee5, 7.9)



for order in customer5.orders():
    print(f"Customer: {order.customer.name}, Coffee: {order.coffee.name}, Price: {order.price}")
