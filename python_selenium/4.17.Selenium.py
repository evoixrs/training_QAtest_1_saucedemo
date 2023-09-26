from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\surgu\\PycharmProjects\\pythonLessons\\python_selenium\\chromedriver.exe')
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
"""Инициализация браузера Chrome, прописываем тестовый сайт"""

login_standart_user = "standard_user"
password_all = "secret_sauce"
"""Создаем переменные Логина и Пароля"""

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standart_user)
print("Input login")
"""Запускаем ввод логина в поле Username"""

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input password")
"""Запускаем ввод пароля в поле Password"""

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login button")
"""Запускаем клик на кнопку 'LOGIN' для авторизации в системе"""


"""INFO товар 1/товар 2"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)
"""Создаем локатор товара 1"""

product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_product_2 = product_2.text
print(value_product_2)
"""Создаем локатор товара 2"""

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)
"""Создаем локатор цены товара 1"""

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)
"""Создаем локатор цены товара 2"""

select_product_1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Select Product 1")
"""Создаем локатор кнопки 'add to card' товара 1 и запускаем клик"""

select_product_2 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
select_product_2.click()
print("Select Product 2")
"""Создаем локатор кнопки 'add to card' товара 2 и запускаем клик"""

cart = driver.find_element(By.XPATH, "//span[@class= 'shopping_cart_badge']")
cart.click()
print("Enter Cart")
"""Создаем локатор Корзины и запускаем клик """

"""INFO Cart Product 1"""
cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1")
"""Сохраняем название товара 1 в переменную и запускаем сравнение названия товара 1 на главной странице и корзине"""

cart_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("INFO Cart Product 2")
"""Сохраняем название товара 2 в переменную и запускаем сравнение названия товара 2 на главной странице и корзине"""

price_cart_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product 1")
"""Сохраняем стоимость товара 1 в переменную и запускаем сравнение стоимости товара 1 на главной странице и корзине"""

price_cart_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print("INFO Cart Price Product 2")
"""Сохраняем стоимость товара 2 в переменную и запускаем сравнение стоимости товара 2 на главной странице и корзине"""

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Click Checkout")
"""Создаем в Your Cart локатор кнопки 'checkout' и запускаем клик на кнопку"""

"""Select User INFO"""
first_name = driver.find_element(By.XPATH, "//input[@id= 'first-name']")
first_name.send_keys("Roma")
print("Input first_name")
"""Создаем локатор поля 'First Name' и запускаем ввод данных в поле"""

last_name = driver.find_element(By.XPATH, "//input[@id= 'last-name']")
last_name.send_keys("Rod")
print("Input last_name")
"""Создаем локатор поля 'Last Name' и запускаем ввод данных в поле"""

zip = driver.find_element(By.XPATH, "//input[@id= 'postal-code']")
zip.send_keys("628415")
print("Input zip")
"""Создаем локатор поля 'Zip/Postal Code' и запускаем ввод данных в поле"""

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print("Click continue")
"""Создаем в Checkout локатор кнопки 'continue' и запускаем клик на кнопку"""

"""INFO Finish Product 1/ Product 2"""
finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finish Product 1")
"""Сохраняем название товара 1 из 'Checkout: Overview' в переменную и 
запускаем сравнение названия товара 1 на главной странице и Checkout: Overview"""

finish_product_2 = driver.find_element(By.XPATH, "//*[@id='item_5_title_link']/div")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("INFO finish Product 2")
"""Сохраняем название товара 2 из 'Checkout: Overview' в переменную и 
запускаем сравнение названия товара 2 на главной странице и Checkout: Overview"""

price_finish_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO finish Price Product 1")
"""Сохраняем стоимость товара 1 из 'Checkout: Overview' в переменную и 
запускаем сравнение названия товара 1 на главной странице и Checkout: Overview"""

price_finish_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2
print("INFO finish Price Product 2")
"""Сохраняем стоимость товара 2 из 'Checkout: Overview' в переменную и 
запускаем сравнение названия товара 2 на главной странице и Checkout: Overview"""

"""INFO Price total"""
summ_product = float(value_finish_price_product_1[1:]) + float(value_finish_price_product_2[1:])
print("Summ poduct:", summ_product)
"""Получаем сумму из стоимости Товара 1 и Товара 2 в 'Checkout: Overview' без символа $"""

summery_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summery_price = summery_price.text
item_total = float(value_summery_price[13:])
print("Item total: ", item_total)
assert summ_product == item_total
print("Total summary price GOOD")
"""Создаем локатор и получаем сумму из 'Item total' в 'Checkout: Overview Price Total' без символа $. 
Сравниеваем на соответствие сумму из 'Item total' и сумму за все товары"""

"""FINISH"""
select_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
select_finish.click()
print("Select FINISH")
"""Создаем локатор кнопки 'Finish' в 'Checkout: Overview' и запускаем клик"""





