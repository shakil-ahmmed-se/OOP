from menu import Burger, Pizza, Drinks, Menu
from restaurant import Restaurant
from users import Chef,Customer,Manager,Server
from Order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('sutki pizza', 600, 'large',['sutki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Alu Vorta pizza' , 400, 'medium',['patato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('Dal pizza', 500, 'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)

    #add burger to the menu
    burger_1 = Burger('Naga burger', 1000,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',1200,'beef',['goru','haddi'])
    menu.add_menu_item('burger',burger_2)

    #add drinks to the menu
    drink_1 = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks',drink_1)
    drink_2 = Drinks('Coffee',250, False)
    menu.add_menu_item('drinks',drink_2)

    menu.show_menu()

    sai_baba = Restaurant('Sai Baba Resturant',2000, menu)

    manager = Manager('Kala Chan Manager',21321,'kala@gmail.com','kaliapur',1500,'january 1 2020','Core')
    sai_baba.add_employee('manager',manager)
    chef = Chef('Rustom Baburchi',2312,'rustom@gmail.com','rustom nagar',3000,'Feb 3 2020','Chef','Everything')
    sai_baba.add_employee('chef',chef)

    server = Server('Chotu Server',3234,'nai@gmail.com','choto goli',200,'jan 2 2020','server')
    sai_baba.add_employee('server',server)

    # sai_baba.show_employees()

    #customer 1 placing order
    customer_1 = Customer('Sakib',3221,'sakib@gmail.com','Magura',12000)
    order_1 = Order(customer_1,[pizza_2,drink_2,pizza_3,drink_2,burger_2])
    customer_1.pay_for_oder(order_1)
    sai_baba.add_order(order_1)

    #customer 1 paying
    sai_baba.recive_payment(order_1,10000,customer_1)
    print('Revenure and balance after first customer',sai_baba.revenue,sai_baba.balance)

    #customer 2
    customer_2 = Customer('Rakib',3221,'rakib@gmail.com','Bogura',10000)
    order_2 = Order(customer_2,[pizza_1,drink_2,burger_1,drink_1,pizza_2])
    customer_2.pay_for_oder(order_2)
    sai_baba.add_order(order_2)

    #customer 2 paying
    sai_baba.recive_payment(order_2,10000,customer_2)
    print('Revenure and balance after second customer',sai_baba.revenue,sai_baba.balance)

    #pay retn
    sai_baba.pay_expense(sai_baba.rent ,'Rent')
    print('After rent', sai_baba.revenue, sai_baba.balance, sai_baba.expense)

    #pay salary
    sai_baba.pay_salary(manager)
    print('After Pay Salary', sai_baba.revenue, sai_baba.balance, sai_baba.expense)


#call the main method
if __name__ == '__main__':
    main()