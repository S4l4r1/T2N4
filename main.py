#import telebot
#import random
#token = '5888557677:AAHAKUYyRHLm0ml0bbaXY-vtIUoMo_Uy0W0'
#bot = telebot.TeleBot(token)
#@bot.message_handler(commands = ['start', 'help'])

#def send_welcome(message):
    #welcome_text = "2"
    #bot.send_message(message.chat.id,welcome_text)

#@bot.message_handler(commands=['poem'])

#def send_poem(message):
    #poem_text = "1"
    #bot.send_message(message.chat.id, poem_text)

#@bot.message_handler(commands = ['cat'])

#def send_cat(message):
    #cat_number = str(random.randint(1,9))
    #cat_img = open('img/' + cat_number + '/jpg', 'rb')
    #bot.send_photo(message.chat.id,cat_img)

#bot.polling()












#import speech_recognition as sr
#rec = sr.Recognizer()
#with sr.Microphone(device_indes=1) as source:
    #rec.adjust_for_ambient_noise(source, duration=3)
    #print('Скажите что-нибудь...')
    #audio = rec.listen(source)
    #print(audio)
#text = rec.recognize_google(audio, language = 'ru_RU')












#from tkinter import *
#import requests
#from bs4 import BeautifulSoup
#from datetime import datetime
#window = Tk()
#window.title('Окно')
#window.geometry('600x600')

#url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='

#def getCourse(id):
    #response = requests.get(url)
    #xml = BeautifulSoup(response.content, 'html.parser')
    #valute = xml.find('valute', {'id': id})
    #return valute.value.text

#title = Label(window, text='Курс валют\nayo shut tf up', fg='black',bg='orange',font = '22')
#title.place(y=25,x=150)

#today = datetime.today()
#today = today.strftime('%d.%m.%Y')
#dateinfo= Label(window, text='today' + today, font='20')
#dateinfo.place(y=150,x=90)

#usd_course= Label(window, text='$' + getCourse('R01235'), font='20')
#usd_course.place(y=190,x=100)

#print(getCourse('R01235'))

#window.mainloop()











#res = []
#val = 15
#res = val or res
#print(res)

#div_5_list = []
#for i in range(100):
    #if i % 5 == 0:
        #div_5_list.append(i)
#print(div_5_list)

#div_5_list = [x for x in range(100) if x%5 == 0]
#print(div_5_list)

#div_5_list = [x**3 if x >50 else x for x in range(100) if x%5 == 0]
#print(div_5_list)

#list_30_31 = [x for x in range (251) if x % 30 == 0 or x % 31 == 0]
#print(list_30_31)




#dict = {x: len(x) for x in ['orange','red','blue','green']}
#print(dict)

#a = {x: x**2+1 for x in range(100)}
#print(a)




#cartage = (1,2,[3,7,9],5)
#cartage[2].append(5)
#print(cartage)




#def func(a,b,*args):
    #print(a)
    #print(b)
    #print(args)
#func(2,5,8,7,6,1)


#def func(*args, **kwargs):
    #print(args)
    #print(kwargs)
#func(5, 7, 9, one = 1, two = 2, three = 3)

#list_ch_and_nch = []
#list_ch = []
#list_nch = []
#for i in range(10):
    #a = int(input('Введите число: '))
    #list_ch_and_nch.append(a)
    #if a % 2 == 0:
        #list_ch.append(a)
    #elif a % 2 != 0:
        #list_nch.append(a)
#print(list_ch)
#print(list_nch)



#a = (5, 3, 2, 1, 4)
#print(tuple(sorted(a)))



# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#
#
# response = requests.get(url)
#
# xml = BeautifulSoup(response.content,'html.parser')
#
# nValute = xml.find_all('valute')
#
# for i in nValute:
#     a = ({i.charcode.text:i.value.text})
#     #print(a)
#     b = a.get('EUR')
#     print(b)
#     if b != None:












# from tkinter import *
# import requests
# from bs4 import BeautifulSoup
#
# window = Tk()
#
# window['background'] = '#000'
#
# url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#
# window.geometry('500x500')
#
# window.title('Курсы валют')
#
# window.resizable(width=False,height=False)
#
# title = Label(text = 'Курсы валют:',bg = 'orange',font = 'Arial 22')
# title.place(x = 40, y = 50)
#
# def getCourse(id):
#     response = requests.get(url)
#     xml = BeautifulSoup(response.content, 'html.parser')
#     valute = xml.find('valute',{'id':id})
#     a = (valute.value.text)
#     return a
#
# print(getCourse('R01375'))
# print(getCourse('R01235'))
#
# course1 = Label(text ='Юань = ' + getCourse('R01375') + ' рублей.',bg = 'cyan', fg = 'black', font = 'Arial 22')
# course1.place(x = 40, y = 200)
#
# course2 = Label(text ='Доллар США = ' + getCourse('R01235') + ' рублей.',bg = 'cyan', fg = 'black', font = 'Arial 22')
# course2.place(x = 40, y = 300)

# window.mainloop()





# import random

# class Tank:
#
#     def __init__(self, model, dfns, min_dmg, max_dmg, hp):
#
#         self.model = model
#         self.dfns = dfns
#         self.hp = hp
#         self.dmg = random.randint(min_dmg, max_dmg)
#
#     def print_info(self):
#         print(self.model,'броня:' ,self.dfns,'урон: ',self.dmg, 'здоровье: ',self.hp)
#
#     def hp_down(self, enemy_dmg):
#         self.hp -= enemy_dmg
#         print('\n', self.model)
#         print('Попадание по ', self.model, 'Нанесено ', enemy_dmg, 'урона')
#
#     def shot(self, enemy):
#         if enemy.hp <= 0 or self.dmg >= enemy.hp:
#             enemy.hp = 0
#             print(enemy.model, 'уничтожен')
#         else:
#             enemy.hp_down(self.dmg)
#             print('Попадание. У ', enemy.model, 'отсалось', enemy.hp, 'здоровья.')
#
#
# rank1 = Tank('A', 100, 100, 120, 100)
# rank2 = Tank('B', 120, 120, 130, 110)
# rank3 = Tank('C', 140, 130, 140, 125)
#
# rank1.print_info()
# rank2.print_info()
# rank3.print_info()
#
# rank1.hp_down(50)
#
# class SuperTank(Tank):
#     def __init__(self, model, dfns, min_dmg, max_dmg, hp):
#         super().__init__(self, model, dfns, min_dmg, max_dmg, hp)
#         self.forceDefense = True
#
#     def hp_down(self, enemy_dmg):
#         super().hp_down(enemy_dmg/2)
#
# sRank4 = SuperTank('D', 300, 200, 250, 300)
# sRank4.print_info()
# sRank4.shot(rank3)
#
#
#
#
#
#
# class A:
#     def one(self):
#         print(1)
#     def two(self):
#         print(2)
#
# class B(A):
#     def three(self):
#         print(3)
#     def two(self):
#         print('22')
#
# a = A()
# a.two()
# b = B()
# b.two()





#import random
#
# class user:
#     def __init__(self, hp, fireball_min, fireball_max, cut_min, cut_max, shoot_min, shoot_max):
#         self.hp = hp
#
# class mage(user):
#     def __init__(self, hp, fireball_min, fireball_max):
#         print(hp, '- Здоровье; ', fireball_min, '- Маг.урон(мин); ', fireball_max, '- Маг.урон(макс.)')
#
# class ranger(user):
#     def __init__(self, hp, shoot_min, shoot_max):
#         print(hp, '- Здоровье; ', shoot_min, '- Стр.урон(мин); ', shoot_max, '- Стр.урон(макс.)')
#
# class warrior(user):
#     def __init__(self, hp, cut_min, cut_max):
#         print(hp, '- Здоровье; ', cut_min, '- Ближн.урон(мин); ', cut_max, '- Ближн.урон(макс.)')
#
# user1 = mage(50, 200, 250)
# user2 = ranger(75, 150, 175)
# user3 = warrior(200, 50, 75)





#user1 = user(50, 200, 250, 0, 0, 0, 0,)
#user1.self_info()






# import requests
# from bs4 import BeautifulSoup
# # def ccourse(valute_from,valute_to,amount):
# valute_from = input('Введите 3 буквы изначальной валюты: ')
# valute_to = input('Введите 3 буквы конечной валюты: ')
# amount = int(input('Введите кол-во изначальной валюты: '))
# def ccourse(valute_from,valute_to,amount):
#     global d
#     url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#     response = requests.get(url)
#     xml = BeautifulSoup(response.content, 'html.parser')
#     nValute = xml.find_all('valute')
#
#     for i in nValute:
#         a = ({i.charcode.text: i.value.text})
#         b = a.get(valute_from)
#         c = a.get(valute_to)
#         print(b, c)
# ccourse(valute_from, valute_to, amount)













# from tkinter import *
# import time
#
# class Ball:
#     def __init__(self, canvas, color, platform):
#         self.canvas = canvas
#         self.oval = canvas.create_oval(200, 200, 215, 215, fill = color)
#         self.x = 1
#         self.y = -1
#         self.platform = platform
#         self.touch_bottom = False
#
#     def draw(self):
#         pos = self.canvas.coords(platform.rect)
#         print(pos)
#         if self.touch_platform(pos) == True:
#             self.y = -1
#
#         self.canvas.move(self.oval,self.x,self.y)
#         pos = self.canvas.coords(self.oval)
#         if pos[1] <= 0:
#             self.y = 1
#         if pos[3] >= 400:
#             self.touch_bottom = True
#         if pos[2] >= 500:
#             self.x = -1
#         if pos[0] <= 0:
#             self.x = 1
#
#
# class Platform:
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
#         self.x = 0
#         self.canvas.bind_all('<KeyPress-Left>', self.left)
#         self.canvas.bind_all('<KeyPress-Right>', self.right)
#
#     def left(self, event):
#         self.x = -2
#
#     def right(self, event):
#         self.x = 2
#
#     def touch_platform(self, ball_pos):
#         platform_pos = self.canvas.coords(platform.rect)
#         if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
#             if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
#                 return True
#         return False
#
#     def draw(self):
#         self.canvas.move(self.rect, self.x, 0)
#
#
#
#         pos = self.canvas.coords(self.rect)
#
#         if pos[0] <= 0:
#             self.x = 0
#         if pos[2] >= 500:
#             self.x = 0
# window = Tk()
# window.title('Аркада')
# window.resizable(0,0)
# window.wm_attributes('-topmost', 1)
#
# canvas = Canvas(window, width=500, height=400)
# canvas.pack()
#
# ball = Ball(canvas, 'red', Platform)
# platform = Platform(canvas, 'green')
#
# while True:
#     if ball.touch_bottom == False:
#         ball.draw()
#         platform.draw()
#     else:
#         break
#     window.update()
#     time.sleep(0.01)










# salary = 20000
# name = 'Davis'
#
# print('У', name, 'зарплата: ', salary)
# print(f'У {name} зарплата в месяц {salary} рублей')




# employee = {
#     'name': 'Davis',
#     'salary': 200000
# }
#
# print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} рублей\n')







# employee_list = [{
#     'name': 'Davis',
#     'salary': 200000
# },{
#     'name':'Ryan',
#     'salary':2000
# },{
#     'name':'Blaze',
#     'salary':3000000
# }]
# print(employee_list[1])
# print(employee_list[1]['salary'])
#
#
# new_employee = {}
# new_employee['name'] = input('Имя:')
# new_employee['salary'] = int(input('Зп: '))
# employee_list.append(new_employee)
#
# for employee in employee_list and new_employee:
#     print(f'У {employee["name"]} зарплата в месяц {employee["salary"]} рублей\n')
#
# print(employee_list)
# name = input('Кого уволить?')
# for employee in employee_list:
#     if employee['name'] == name:
#         employee_list.remove(employee)
#         print(employee_list)
#         break





# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.on_vacation = False
#
#     def get_info(self):
#         return f'У {self.name} зарплата в месяц {self.salary} рублей. В отпуске? {self.on_vacation}\n'
#
# employees = [Employee('EEE', 2000000), Employee('GGG', 3000000), Employee('SSS', 4000000000)]
#
# employees[1].on_vacation = True
#
# for employee in employees:
#     print(employee.get_info())









# import vk_api
#
# token = 'vk1.a.mEfgIlwCjjLGtBL002w11IrQDAjIdgxDvz0q5DZT6WqFefWwojm84EoAjKis0hSA7v-CjdLhWdd-jciq_SPaJpEhkRkksYaopYaKpf-4PmHFy-irrRhhgMB5o3pn0RPsyuMLHbeQeH2QoYpmDu5IUm9S43S5mDUFc0q7eh-XhDe6pVRoe_h98wHv_QTKrqkXcvESUdo0yA52hs382_Jv1Q'
# vk = vk_api.VkApi(token = token)
#
# messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
# user_id = (messages['items'][1]['last_message']['from_id'])
# message_id = (messages['items'][1]['last_message']['id'])
#print(messages['items'][2]['last_message']['text'])
#print(messages['items'])

#vk.method('messages.send', {'peer_id': user_id ,'random_id': message_id , 'message': 'lelelelele'})











# class Employee:
#     def __init__(self, name, salary, vacation_status, is_good_employee):
#         self.name = name
#         self.salary = salary
#         self.vacation_status = vacation_status
#         self.is_good_employee = is_good_employee
#
#     def get_info(self):
#         return f'У {self.name} зарплата в месяц: {self.salary} рублей. В отпуске? - {self.vacation_status}. Хороший? - {self.is_good_employee}'
#
# employees = [Employee('E1', 200000, True, True), Employee('E2', 300000, False, True), Employee('E3', 4000000, False, True), Employee('E4', 5000000, False, True), Employee('E5', 4000000, False, False)]
# for employee in employees:
#     if employee.is_good_employee == False:
#         employees.remove(employee)
#         print(employees)
























#a = [x for x in range(1,10000)]
#print(a)

# def my_lazy_gen():
#     for x in range(100):
#         print(f'до {x} ')
#         yield x
#         print(f'после {x} ')
# print(my_lazy_gen())
# for i in my_lazy_gen():
#     print(i)








# list = []
# for i in range(10000):
#     file = open('file.txt', 'w')
#     list.append(file)
#     file.close()

# with open('file.txt', 'w') as file:
#     file.write('sup!!!')
#     print(file.closed)
# print(file.closed)





# import requests
#
# url = 'https://swapi.dev/api/'
# response = requests.get(url)
# respJson = response.json()
# starships_api = respJson.get('starships')
#
# def MSWS(url):
#     a = []
#     b = {}
#     for i in range(1,37):
#         resp = requests.get(url + '/' + str(i)).json()
#         mas = resp.get('length')
#         name = resp.get('name')
#         if mas == 'n/a' or mas == 'unknown' or mas == None:
#             mas = 0
#         if mas == float:
#
#         a.append(int(mas))
#         b[mas] = name
#     m_mas = max(a)
#     m_mas_name = b.get(str(m_mas))
#     return str(m_mas) + m_mas_name
# msws = MSWS(starships_api)
#
#
# import vk_api
#
# token = 'vk1.a.mEfgIlwCjjLGtBL002w11IrQDAjIdgxDvz0q5DZT6WqFefWwojm84EoAjKis0hSA7v-CjdLhWdd-jciq_SPaJpEhkRkksYaopYaKpf-4PmHFy-irrRhhgMB5o3pn0RPsyuMLHbeQeH2QoYpmDu5IUm9S43S5mDUFc0q7eh-XhDe6pVRoe_h98wHv_QTKrqkXcvESUdo0yA52hs382_Jv1Q'
# vk = vk_api.VkApi(token = token)
#
# while True:
#     messages = vk.method('messages.getConversations',{'count' : 20, 'filter': 'unanswered'})
#     if messages['count'] >= 1:
#         user_id = messages['items'][1]['last_message']['from_id']
#         vk.method('messages.send', {'peer_id': user_id, 'random_id': 41,'message':msws })




#з.4, н.3

# numb = [1,5,7,-8,55,-54,88,100,0]
# total_elems = len(numb) - 1
# print(total_elems)
# for z in range(total_elems):
#     for i in range(total_elems):
#         if numb[i] > numb[i+1]:
#             numb[i], numb[i+1] = numb[i+1], numb[i]
# print(numb)




#з.5, н.3

# goods = {
#     'Лампа':'12345',
#     'Стол':'23456',
#     'Диван':'34567',
#     'Стул':'45678',
# }
# store = {
#     '12345':[
#         {'quanity':27, 'price': 42}
#     ],
#     '23456':[
#     {'quanity':22,'price':510},
#     {'quanity':32,'price':520},
#     ],
#     '34567':[
#     {'quanity':2,'price':1200},
#     {'quanity':1,'price':1150},
#     ],
#     '45678':[
#     {'quanity':50,'price':100},
#     {'quanity':12,'price':95},
#     {'quanity':43,'price':97},
#     ]
# }
# for name in goods:
#     q_ity = 0
#     sum = 0
#     for item in store[goods[name]]:
#         pr_ce = item['price']
#         q_ity = item['quanity']
#         sum += pr_ce * q_ity
#         print(f'{name}:{q_ity} за {pr_ce} руб, общая стоимость товара : {sum} руб.')

#з.7, н.3

# from tkinter import *
# import random
# p1 = 0
# p2 = 0
# window = Tk()
# window.geometry('650x450')
# def check1():
#     global p2
#     global p1
#     b.place(x=random.randint(1,550),y=random.randint(1,350))
#     p1+= 1
#     if p1 == 10:
#         b1['text'] = 'Ну пожалуйста'
#     if check2 == True:
#         p1 == 0
# def check2():
#     global p2
#     global p1
#     b1.place(x=random.randint(1,550), y=random.randint(1,350))
#     p2 += 1
#     if check1 == True:
#         p2 == 0
#     if p2 == 10:
#         b['text'] = 'Ну пожалуйста'
# b = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check1)
# b.place(x=200,y=130)
# b1 = Button(text='нажми меня', font=('Arial', 20), fg='black', command=check2)
# b1.place(x=300,y=200)
# window.mainloop()

#З.9 Н.1

# from bs4 import BeautifulSoup as BS
# import requests as req
#
# request = req.get('http://www.columbia.edu/~fdc/sample.html')
# request = request.content
# html = BS(request, 'html.parser')
# result = html.find_all('h3')
# emp_list = []
# for h3 in result:
#     tex = h3.text
#     emp_list.append(tex)
# print(emp_list)

#З.9 Н.2

# from bs4 import BeautifulSoup as BS
# import requests as req
#
# request = req.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
# request = request.content
# html = BS(request, 'html.parser')
# result = html.find(class_ = 'ecomerce-items')
# items = result.get('data-items')
# print(items)

#З.9 Н.3

# from bs4 import BeautifulSoup as BS
# import requests as req
#
# user_wish = int(input('Введите цифру для выбора жанра (Гонки - 1; Аркады - 2; Файтинги - 3; Квестовые - 4; Головоломки - 5; Приключения - 6; Симуляторы - 7; Спортивные - 8; Стратегии - 9; Хорроры - 10; Шутеры - 11; Экшен-игры - 12): '))
#
# if user_wish == 1:
#     request = req.get('https://thelastgame.ru/category/racing/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     racing_ = html.find_all(class_ = 'post-title entry-title')
#     for h in racing_:
#         print(h.text)
#
# elif user_wish == 2:
#     request = req.get('https://thelastgame.ru/category/arcade/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     arcade_ = html.find_all(class_ = 'post-title entry-title')
#     for h in arcade_:
#         print(h.text)
#
# elif user_wish == 3:
#     request = req.get('https://thelastgame.ru/category/fight/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     fighting_ = html.find_all(class_ = 'post-title entry-title')
#     for h in fighting_:
#         print(h.text)
#
# elif user_wish == 4:
#     request = req.get('https://thelastgame.ru/category/quest/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     quests_ = html.find_all(class_ = 'post-title entry-title')
#     for h in quests_:
#         print(h.text)
#
# elif user_wish == 5:
#     request = req.get('https://thelastgame.ru/category/logic/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     logic_ = html.find_all(class_ = 'post-title entry-title')
#     for h in logic_:
#         print(h.text)
#
# elif user_wish == 6:
#     request = req.get('https://thelastgame.ru/category/adventure/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     adventure_ = html.find_all(class_ = 'post-title entry-title')
#     for h in adventure_:
#         print(h.text)
#
# elif user_wish == 7:
#     request = req.get('https://thelastgame.ru/category/simulator/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     simulator_ = html.find_all(class_ = 'post-title entry-title')
#     for h in simulator_:
#         print(h.text)
#
# elif user_wish == 8:
#     request = req.get('https://thelastgame.ru/category/sport/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     sport_ = html.find_all(class_ = 'post-title entry-title')
#     for h in sport_:
#         print(h.text)
#
# elif user_wish == 9:
#     request = req.get('https://thelastgame.ru/category/strategy/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     strategy_ = html.find_all(class_ = 'post-title entry-title')
#     for h in strategy_:
#         print(h.text)
#
# elif user_wish == 10:
#     request = req.get('https://thelastgame.ru/category/horror/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     horror_ = html.find_all(class_ = 'post-title entry-title')
#     for h in horror_:
#         print(h.text)
#
# elif user_wish == 11:
#     request = req.get('https://thelastgame.ru/category/shooter/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     shooter_ = html.find_all(class_ = 'post-title entry-title')
#     for h in shooter_:
#         print(h.text)
#
# elif user_wish == 12:
#     request = req.get('https://thelastgame.ru/category/action/')
#     request = request.content
#     html = BS(request, 'html.parser')
#     action_ = html.find_all(class_ = 'post-title entry-title')
#     for h in action_:
#         print(h.text)



#З.10 Н.1

# number = int(input('Введите число:'))
# summ = 0
# while number != 0:
#     summ += number
#     print(summ)
#     number = int(input('Введите число:'))

#З.10 Н.2

# password = input('Введите пароль: ')
# while password != '235':
#     print('Неверный пароль. Повторите попытку. ')
#     password = input('Введите пароль: ')
# if password == '235':
#     print('Добро пожаловать, <username>.')

#З.10 Н.3

# import openpyxl
#
# wb = openpyxl.load_workbook(filename = r"C:\Users\МАКС\Desktop\Книга3.xlsx")
# sheet = wb['Лист1']
# val = sheet['A1'].value
# print(val)
# vals = [v[0].value for v in sheet['A1:A2']]
# print(vals)
# sheet['B1'] = val
# i = 1
#
# for rec in vals:
#     sheet.cell(row = i, column = 2).value = rec
#     i =+1
#
# wb.save(r'C:\Users\МАКС\Desktop\Книга3.xlsx')

#TASK 1 NUMBER 2

# a = int(input('Введите значение "a" (b^2 - 4ac) '))
# b = int(input('Введите значение "b" (b^2 - 4ac) '))
# c = int(input('Введите значение "c" (b^2 - 4ac) '))
#
# def Disc_():
#     global a,b,c
#     D = b**2 - 4 * a * c
#     print(D)
# Disc_()

#TASK 2 NUMBER 1

# import telebot
# from bs4 import BeautifulSoup as BS
# import requests as req
#
# token = '6621968740:AAELIGGjv7tKJouuUcBEoVvviBOQRU5I78Y'
#
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(content_types = ['text'])
# def rec_(message):
#     if message.text == 'Рек/Гонки':
#         request = req.get('https://thelastgame.ru/category/racing/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         racing_ = html.find_all(class_ = 'post-title entry-title')
#         for h in racing_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)
#     elif message.text == 'Рек/Шутеры':
#         request = req.get('https://thelastgame.ru/category/shooter/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         shooter_ = html.find_all(class_ = 'post-title entry-title')
#         for h in shooter_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)
#     elif message.text == 'Рек/Стратегии':
#         request = req.get('https://thelastgame.ru/category/strategy/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         strategy_ = html.find_all(class_ = 'post-title entry-title')
#         for h in strategy_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)

# bot.polling()

#TASK 2 NUMBER 2

# import telebot
# from bs4 import BeautifulSoup as BS
# import requests as req
#
# token = '6621968740:AAELIGGjv7tKJouuUcBEoVvviBOQRU5I78Y'
#
# bot = telebot.TeleBot(token)
# @bot.message_handler(commands = ['start', 'help'])
# def send_welcome(message):
#     welcome_text = 'Привет! Какой жанр вам порекомендовать в этот раз?(1 - Гонки; 2 - Шутеры; 3 - Стратегии.)'
#     bot.send_message(message.chat.id, welcome_text)
# @bot.message_handler(content_types = ['text'])
# def genre_(message):
#     if message.text =='1':
#         request = req.get('https://thelastgame.ru/category/racing/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         racing_ = html.find_all(class_ = 'post-title entry-title')
#         for h in racing_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)
#     elif message.text == '2':
#         request = req.get('https://thelastgame.ru/category/shooter/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         shooter_ = html.find_all(class_ = 'post-title entry-title')
#         for h in shooter_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)
#     elif message.text == '3':
#         request = req.get('https://thelastgame.ru/category/strategy/')
#         request = request.content
#         html = BS(request, 'html.parser')
#         strategy_ = html.find_all(class_ = 'post-title entry-title')
#         for h in strategy_:
#             result = h.text
#         bot.send_message(message.from_user.id, result)
#
#
#
# bot.polling()

#TASK 3 NUMBER 1

# from tkinter import *
#
# window = Tk()
# window.geometry('800x600')
#
# canvas = Canvas(window,width = 800, height = 600, bg = 'black')
# canvas.pack()
#
# canvas.create_rectangle(300, 200, 500, 400, fill = 'cyan')
# canvas.create_polygon(200, 305, 300, 400, 300, 199, fill = 'yellow')
# canvas.create_polygon(300, 200, 400, 125, 500, 200, fill = 'yellow')
# canvas.create_polygon(500, 200, 600, 300, 500, 400, fill = 'yellow')
# canvas.create_polygon(500, 400, 400, 500, 300, 400, fill = 'yellow')
#
# class object:
#     def __init__(self,x1, y1, x2, y2, x3, y3, color):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.x3 = x3
#         self.y3 = y3
#         self.color = color
# rectangle_ = object(300,200,500,400,'','','cyan')
# poly_1 = object(200, 305, 300, 400, 300, 199, 'yellow')
# poly_2 = object(300,200,400,125,500,200, 'yellow')
# poly_3 = object(500,200,600,300,500,400, 'yellow')
# poly_4 = object(500,400,400,500,300,400, 'yellow')
#
# canvas.create_rectangle(rectangle_.x1, rectangle_.y1, rectangle_.x2, rectangle_.y2, fill = rectangle_.color)
# canvas.create_polygon(poly_1.x1, poly_1.y1, poly_1.x2, poly_1.y2, poly_1.x3, poly_1.y3, fill = poly_1.color)
# canvas.create_polygon(poly_2.x1, poly_2.y1, poly_2.x2, poly_2.y2, poly_2.x3, poly_2.y3, fill = poly_2.color)
# canvas.create_polygon(poly_3.x1, poly_3.y1, poly_3.x2, poly_3.y2, poly_3.x3, poly_3.y3, fill = poly_3.color)
# canvas.create_polygon(poly_4.x1, poly_4.y1, poly_4.x2, poly_4.y2, poly_4.x3, poly_4.y3, fill = poly_4.color)
#
# window.mainloop()


#TASK 3 NUMBER 2

# import random
# class warrior:
#     def __init__(self, name, health):
#         self.health = health
#         self.name = name
#     def hit(self, other):
#         other.health = other.health - 20
#         print(self.name + ' Наносит удар! У ' + other.name + ' Осталось',other.health,'очков здоровья.')
#         if other.health == 0:
#             print(self.name + ' одержал победу!')
#             exit()
# warrior_1 = warrior('Воин 1',100)
# warrior_2 = warrior('Воин 2',100)
# while True:
#     a = random.randint(1,2)
#     if a == 1:
#         warrior_1.hit(warrior_2) == True
#     elif a == 2:
#         warrior_2.hit(warrior_1) == True

#TASK 4 NUMBER 1

# from tkinter import *
#
# w = 600
# h = 600
#
# window = Tk()
# window.geometry(str(w) + 'x' + str(h))
#
# canvas = Canvas(window, width = w, height = h)
# canvas.place(in_ = window, x = 0, y = 0)
# bg_photo = PhotoImage(file = 'plain.png')
# knight_photo = PhotoImage(file = 'knight.png')
#
# class Knight:
#     def __init__(self):
#         self.x = 120
#         self.y = h//2
#         self.v = 0
#         self.photo = PhotoImage(file = 'knight.png')
#
#     def up(self, event):
#         self.v = -3
#
#     def down(self, event):
#         self.v = 3
#
#     def stop(self, event):
#         self.v = 0
#
#
# knight = Knight()
#
# def game():
#     canvas.delete('all')
#     canvas.create_image(300,300, image = bg_photo)
#     canvas.create_image(knight.x, knight.y, image = knight_photo)
#     knight.y += knight.v
#     if knight.y >= 600:
#         knight.y = 599
#     elif knight.y <= 0:
#         knight.y = 1
#     window.after(10, game)
#
#
# game()
#
# window.bind('<Key-Up>', knight.up)
# window.bind('<Key-Down>', knight.down)
# window.bind('<KeyRelease>', knight.stop)
# window.mainloop()

#TASK 4 NUMBER 2

# from tkinter import *
#
# w = 600
# h = 600
#
# window = Tk()
# window.geometry(str(w) + 'x' + str(h))
#
# canvas = Canvas(window, width = w, height = h)
# canvas.place(in_ = window, x = 0, y = 0)
# bg_photo = PhotoImage(file = 'plain.png')
# knight_photo = PhotoImage(file = 'knight.png')
#
# class Knight:
#     def __init__(self):
#         self.x = 120
#         self.y = h//2
#         self.v = 0
#         self.s = 0
#         self.photo = PhotoImage(file = 'knight.png')
#
#     def up(self, event):
#         self.v = -3
#
#     def down(self, event):
#         self.v = 3
#
#     def stop_v2(self, event):
#         self.s = 0
#         self.v = 0
#
#     def right(self, event):
#         self.s = 2
#
#     def left(self, event):
#         self.s = -2
#
#
#
# knight = Knight()
#
# def game():
#     canvas.delete('all')
#     canvas.create_image(300,300, image = bg_photo)
#     canvas.create_image(knight.x, knight.y, image = knight_photo)
#     knight.y += knight.v
#     knight.x += knight.s
#     if knight.y >= 600:
#         knight.y = 599
#     elif knight.y <= 0:
#         knight.y = 1
#     if knight.x <= 0:
#         knight.x = 1
#     elif knight.x >= 600:
#         knight.x = 599
#     window.after(10, game)
#
#
# game()
#
# u = window.bind('<Key-Up>', knight.up)
# d = window.bind('<Key-Down>', knight.down)
# l = window.bind('<Key-Left>', knight.left)
# r = window.bind('<Key-Right>', knight.right)
# s_2 = window.bind('<KeyRelease>', knight.stop_v2)
# window.mainloop()

#TASK 5 NUMBER 1

# import requests
#
# url = 'https://swapi.dev/api/'
#
# response = requests.get(url)
#
# response_j = response.json()
#
# starships_url = response_j.get('starships')
#
# def max_starships_speed(url):
#     for i in range(1,12):
#         response = requests.get(url + '/' + str(i)).json()
#         max_speed = response.get('max_atmosphering_speed')
#         print(max_speed)
# max_starships_speed(starships_url)

# TASK 5 NUMBER 2

# import requests
#
# url = 'https://swapi.dev/api/'
#
# response = requests.get(url)
#
# response_j = response.json()
#
# starships_url = response_j.get('starships')
#
# emp_dict = {}
# emp_list = []
#
# def max_starships_speed(url):
#     for i in range(1,12):
#         global emp_dict
#         global ship_name
#         response = requests.get(url + '/' + str(i)).json()
#         max_speed = response.get('max_atmosphering_speed')
#         ship_name = response.get('name')
#         if max_speed == None or max_speed == 'n/a':
#             max_speed = 0
#         elif max_speed == '1000km':
#             max_speed = 1000
#         emp_dict[max_speed] = ship_name
#         emp_list.append(int(max_speed))
# max_starships_speed(starships_url)
#
# max_speed_str = str(max(emp_list))
# print(max_speed_str)
# print(emp_dict[max_speed_str])

# TASK 6 NUMBER 2

# import requests
# from bs4 import BeautifulSoup as BS
# emp_dict = {}
# for_value = []
# for_valute = []
# def converter(valute_from, valute_to, amount):
#     url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req='
#     date = input('Введите данные вида "день(__)/месяц(__)/год(____)". ')
#     url_v2 = url + date
#     response = requests.get(url_v2)
#     xml = BS(response.content, 'html.parser')
#     valute = xml.find_all('charcode')
#     value = xml.find_all('value')
#     for h in valute:
#         valute_tex = h.text
#         for_valute.append(valute_tex)
#     for i in value:
#         value_tex = i.text
#         for_value.append(value_tex)
#     for v in range(1,34):
#         new_value = float(for_value[v].replace(',', '.'))
#         emp_dict[for_valute[v]] = new_value
#     a = emp_dict.get(valute_from)
#     b = emp_dict.get(valute_to)
#     result = a * amount / b
#     print(result)
# converter('AMD', 'USD', 12)

# TASK 2 NUMBER 2

# import vk_api as v_a
# import requests
# url = 'https://swapi.dev/api/'
# response = requests.get(url)
# response_j = response.json()
# starships_url = response_j.get('starships')
# emp_list = []
# emp_dict = {}
# speed_list = []
# def max_starships_speed(url):
#     global max_speed
#     global name
#     for i in range(1,80):
#         response = requests.get(url + '/' + str(i)).json()
#         max_speed = str(response.get('max_atmosphering_speed'))
#         name = response.get('name')
#         if max_speed == 'n/a' or max_speed == 'unknown':
#             max_speed = '0'
#         for delete in ['k','m']:
#             if delete in max_speed:
#                 max_speed = max_speed.replace(delete, '')
#         emp_list.append(max_speed)
#         emp_dict[max_speed] = name
#     try:
#         while True:
#             emp_list.remove('None')
#     except ValueError:
#         pass
#     for x in emp_list:
#         speed_list.append(int(x))
#     true_max_speed = str(max(speed_list))
#     result = emp_dict.get(true_max_speed)
#     return result + ' ' +  true_max_speed
# token = 'vk1.a.mEfgIlwCjjLGtBL002w11IrQDAjIdgxDvz0q5DZT6WqFefWwojm84EoAjKis0hSA7v-CjdLhWdd-jciq_SPaJpEhkRkksYaopYaKpf-4PmHFy-irrRhhgMB5o3pn0RPsyuMLHbeQeH2QoYpmDu5IUm9S43S5mDUFc0q7eh-XhDe6pVRoe_h98wHv_QTKrqkXcvESUdo0yA52hs382_Jv1Q'
# vk = v_a.VkApi(token = token)
# while True:
#     messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
#     if messages['count']>= 1:
#         user_id = messages["items"][0]["last_message"]["from_id"]
#         message_id = messages["items"][0]["last_message"]["id"]
#         message_text = messages["items"][0]["last_message"]["text"]
#         if message_text.lower() == "корабли":
#             vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":max_starships_speed(starships_url)})
#         else:
#             vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message": "неизвестная команда"})

#TASK 3 NAMBER 1

# import vk_api as v_a
#
# import requests
# from bs4 import BeautifulSoup as BS
# from datetime import date
# from vk_api.longpoll import VkLongPoll, VkEventType
# emp_dict = {}
# for_value = []
# for_valute = []
# today = date.today()
# day = str(today.day)
# month = str(today.month)
# year = str(today.year)
# def converter(valute_wanted):
#     global today, day, month, year
#     if int(day)< 10:
#         day = '0' + day
#     if int(month)< 10:
#         month = '0' + month
#     url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + day + '/' + month + '/' + year
#     response = requests.get(url)
#     xml = BS(response.content, 'html.parser')
#     valute = xml.find_all('charcode')
#     value = xml.find_all('value')
#     for h in valute:
#         valute_tex = h.text
#         for_valute.append(valute_tex)
#     for i in value:
#         value_tex = i.text
#         for_value.append(value_tex)
#     for v in range(1,34):
#         new_value = float(for_value[v].replace(',', '.'))
#         emp_dict[for_valute[v]] = new_value
#     wanted = emp_dict.get(valute_wanted)
#     return wanted
#
# token = 'vk1.a.mEfgIlwCjjLGtBL002w11IrQDAjIdgxDvz0q5DZT6WqFefWwojm84EoAjKis0hSA7v-CjdLhWdd-jciq_SPaJpEhkRkksYaopYaKpf-4PmHFy-irrRhhgMB5o3pn0RPsyuMLHbeQeH2QoYpmDu5IUm9S43S5mDUFc0q7eh-XhDe6pVRoe_h98wHv_QTKrqkXcvESUdo0yA52hs382_Jv1Q'
# vk_session = v_a.VkApi(token = token)
# vk = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)
# for event in longpoll.listen():
#     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#         message = event.text
#         user_id = event.user_id
#         message_id = event.message_id
#         if event.text == '-к USD':
#             response = f'{converter("USD")} рублей за 1 доллар США.'
#             vk.messages.send(user_id = user_id, random_id = message_id, message = response)
#         elif event.text == '-к EUR':
#             response = f'{converter("EUR")} рублей за 1 евро.'
#             vk.messages.send(user_id=user_id, random_id=message_id, message=response)
#         elif event.text == '-к AMD':
#             response = f'{converter("AMD")} рублей за 1 драм.'
#             vk.messages.send(user_id=user_id, random_id=message_id, message=response)

#TASK 4 NUMBER 1
# #1.
# def my_gen():
#     for x in range(1_000_000):
#         yield x**2
# for v in my_gen():
#     print(v)
#
# #2.
# b = (x**2 for x in range(100_000_0))
# for i in b:
#     print(i)

#TASK 4 NUMBER 2

# import contextlib as cl
# import requests
# from bs4 import BeautifulSoup as BS
# from datetime import date
# today = date.today()
# day = str(today.day)
# month = str(today.month)
# year = str(today.year)
# @cl.contextmanager
# def converter(valute_id):
#     global today, day, month, year
#     if int(day)< 10:
#         day = '0' + day
#     if int(month)< 10:
#         month = '0' + month
#     url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + day + '/' + month + '/' + year
#     response = requests.get(url)
#     xml = BS(response.content, 'html.parser')
#     try:
#         id = xml.find('valute', {'id': valute_id})
#         name = id.find('name').text
#         value = id.value.text
#         print ('(1 шт.) ',name,' стоит(-ят): ',value,' рублей.')
#         yield True
#     except AttributeError:
#         print('Вы ввели неверное значение.')
#         exit()
#
# with converter('R01235'):
#     my_l = [1,2]
#     print(my_l[1])

#TASK 5 NUMBER 1

# class Myfile:
#     def __init__(self,f_name,w_or_r,coding_type = 'utf-8'):
#         self.coding_type = coding_type
#         if self.coding_type != 'utf-8' and w_or_r == 'w':
#             with open(f_name, 'w', encoding = coding_type) as e:
#                 text_encode_v1 = input('Введите текст, который хотите увидеть в файле: ')
#                 e.write(text_encode_v1)
#         if w_or_r == 'w' and coding_type == 'utf-8':
#             with open(f_name,'w') as w:
#                 text = input('Введите текст, который хотите увидеть в файле: ')
#                 w.write(text)
#         elif w_or_r == 'r':
#             with open(f_name,w_or_r) as r:
#                 print(r.read())
# Myfile('www.txt', 'r','cp1251')

#TASK 5 NUMBER 2

# import random
# class Endless:
#     def __init__(self):
#         something = 1
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return random.randint(1,5)
# rand_iter = Endless()
# for rand_int in rand_iter:
#     print(rand_int)

#TASK 6 NUMBER 1

# class Year:
#     def __init__(self, days, season):
#         self.days = days
#         self.season = season
#     @property
#     def days(self):
#         return self.__days
#
#     @days.setter
#     def days(self, days):
#         if days == 365 or days == 366:
#             self.__days = days
#         else:
#             raise Exception('Введено неверное значение.')
# year = Year(365, 'may')
# year.days = 3

#TASK 6 NUMBER 2

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,age):
#         if age<0:
#             raise Exception('Вы ещё не родились.')
#         else:
#             self.__age = age
#     @age.deleter
#     def age(self):
#         del self.__age
#
# person = Person('Виктор',19)
# print(person.age,person.name)
# person.age = 3
# print(person.age)
# person.name = 'Александр'
# print(person.name)
# del person.age
# del person.name

#TASK 7 NUMBER 1

# class Solution:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self,other):
#         total = self.number + other.number
#         return total
#     def __sub__(self, other):
#         result = self.number - other.number
#         return result
#     def __mul__(self, other):
#         final = self.number * other.number
#         return final
#     def __truediv__(self, other):
#         answer = self.number / other.number
#         return answer
# N1 = Solution(25)
# N2 = Solution(5)

#TASK 7 NUMBER 2

# from tkinter import *
# from random import randint
#
# window = Tk()
# window.geometry('600x600')
#
# class Fire:
#     image = PhotoImage(file = 'fire.png').subsample(4, 4)
#     def __add__(self,other):
#         if isinstance(other, Ground):
#             return Clay
#         elif isinstance(other, Water):
#             return Steam
# class Water:
#     image = PhotoImage(file = 'water.png').subsample(2,2)
#     def __add__(self,other):
#         if isinstance(other, Wind):
#             return Rain
#         elif isinstance(other, Fire):
#             return Steam
# class Wind:
#     image = PhotoImage(file = 'wind.png').subsample(2,2)
# class Ground:
#     image = PhotoImage(file = 'ground.png').subsample(2, 1)
# class Clay:
#     image = PhotoImage(file = 'pottery.png').subsample(2,2)
# class Steam:
#     image = PhotoImage(file = 'steam.png').subsample(2,2)
# class Rain:
#     image = PhotoImage(file = 'rain.png').subsample(2,2)
# canvas = Canvas(window, width = 600, height = 600)
# canvas.pack()
#
# elements = [Fire(), Water(), Wind(), Ground()]
# for element in elements:
#     img = canvas.create_image(randint(50,500),randint(50,500), image = element.image)
#
# def move(event):
#     images_coords = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
#     if len(images_coords) == 2:
#         element_1 = elements[images_coords[0] - 1]
#         element_2 = elements[images_coords[1] - 1]
#         new_element = element_1 + element_2
#         if new_element not in elements:
#             canvas.create_image(event.x, event.y, image=new_element.image)
#     canvas.coords(images_coords, event.x, event.y)
# window.bind('<B1-Motion>', move)
#
# window.mainloop()

#TASK 8 NUMBER 1(NOT SURE OF)

# class Item:
#     def __init__(self,price,brand):
#         self.price = price
#         self.brand = brand
#
#     def __repr__(self):
#         return f'{self.brand} {self.price}'
#
# items_list = [
#     Item(1000, 'Apple'),
#     Item(1200, 'Apple'),
#     Item(900, 'Samsung'),
#     Item(700, 'Samsung'),
#     Item(660, 'Xiaomi')
# ]
#
# filtered = filter(lambda item:item.brand == 'Apple', items_list)
# print(list(filtered))

#TASK 8 NUMBER 2

# names_list = ['данил', 'артём', 'никита', 'влад']
#
# names_list = map(lambda item: item.capitalize(), names_list)
# print(list(names_list))

#TASK 11 NUMBER 1

# import sqlite3
# import logging
#
# logging.basicConfig(level = logging.INFO)
# def create_table_user(cursor):
#     query = ("""
#     CREATE TABLE IF NOT EXISTS User(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(70) NOT NULL,
#     surname VARCHAR(70) NOT NULL,
#     gender VARCHAR(1) DEFAULT 'M')
#     ;""")
#     cursor.execute(query)
#     logging.info("Таблица создана.")
# def drop_table_user(cursor):
#     query = ("""
#     DROP TABLE IF EXISTS User;""")
#     cursor.execute(query)
#     logging.info("Таблица удалена.")
# def add_user(cursor,User):
#     query = (
#         """INSERT INTO User(name, surname, gender) VALUES (?, ?, ?)"""
#     )
#     cursor.execute(query, (User.name, User.surname, User.gender))
#     logging.info("Данные таблицы обновлены.")
# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
# def get_user_list(cursor):
#     query = """
#     SELECT * FROM User;"""
#     logging.info("Данные о пользователях выведены.")
#     return cursor.execute(query).fetchall()
# def get_user_by_id(cursor, id):
#     query = """
#     SELECT * FROM User WHERE id = ?
#     """
#     logging.info("Данные о пользователе с данным id были выведены.")
#     return cursor.execute(query, (id,)).fetchone()
# def del_data(cursor):
#     query = """
#     DELETE FROM User
#     """
#     cursor.execute(query)
#     logging.info("Данные были удалены.")
# def update_username(cursor, name):
#     query = """
#     UPDATE User SET name = ?;"""
#     logging.info("Имя было изменено.")
#     cursor.execute(query, (name,))
# def del_user_by_id(cursor, id):
#     query = """
#     DELETE FROM User WHERE id = ?;"""
#     logging.info('Удаление по id завершено.')
#     cursor.execute(query, (id,))
# with sqlite3.connect('data.db') as cursor:
#     logging.info("Подключение установлено.")
#     drop_table_user(cursor)
#     create_table_user(cursor)
#     add_user(cursor, User('SAL', 'ARI',  'M'))
#     add_user(cursor, User('Le', 'Le', 'M'))
#     del_user_by_id(cursor, 1)
#     data = get_user_list(cursor)
#     print(data)
#     one_data = get_user_by_id(cursor, 1)
#     print(one_data)
#     logging.info("Данные таблицы были выведены.")

#TASK 11 NUMBER 2

# import sqlite3
# import logging
#
# logging.basicConfig(level = logging.INFO)
# def create_table_user(cursor):
#     query = ("""
#     CREATE TABLE IF NOT EXISTS User(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(70) NOT NULL,
#     surname VARCHAR(70) NOT NULL,
#     gender VARCHAR(1) DEFAULT 'M')
#     ;""")
#     cursor.execute(query)
#     logging.info("Таблица создана.")
# def drop_table_user(cursor):
#     query = ("""
#     DROP TABLE IF EXISTS User;""")
#     cursor.execute(query)
#     logging.info("Таблица удалена.")
# def add_user(cursor,User):
#     query = (
#         """INSERT INTO User(name, surname, gender) VALUES (?, ?, ?)"""
#     )
#     cursor.execute(query, (User.name, User.surname, User.gender))
#     logging.info("Данные таблицы обновлены.")
# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
# def get_user_list(cursor):
#     query = """
#     SELECT * FROM User;
#     """
#     logging.info("Данные о пользователях выведены.")
#     return cursor.execute(query).fetchall()
# def get_user_by_id(cursor, id):
#     query = """
#     SELECT * FROM User WHERE id = ?
#     """
#     logging.info("Данные о пользователе с данным id были выведены.")
#     return cursor.execute(query, (id,)).fetchone()
# def del_data(cursor):
#     query = """
#     DELETE FROM User
#     """
#     cursor.execute(query)
#     logging.info("Данные были удалены.")
# def update_username(cursor, name):
#     query = """
#     UPDATE User SET name = ?;
#     """
#     logging.info("Имя было изменено.")
#     cursor.execute(query, (name,))
# def del_user_by_id(cursor, id):
#     query = """
#     DELETE FROM User WHERE id = ?;
#     """
#     logging.info('Удаление по id завершено.')
#     cursor.execute(query, (id,))
# def certain_gender_only(cursor, gender):
#     query = """
#     SELECT * FROM User WHERE gender = ?
#     """
#     logging.info('Вывод по полу завершён.')
#     return list(cursor.execute(query, (gender,)))
# with sqlite3.connect('data.db') as cursor:
#     logging.info("Подключение установлено.")
#     drop_table_user(cursor)
#     create_table_user(cursor)
#     add_user(cursor, User('SAL', 'ARI',  'M'))
#     add_user(cursor, User('Le', 'Le', 'F'))
#     certain_gender_only(cursor, 'F')
#     data = get_user_list(cursor)
#     print(data)
#     print(certain_gender_only(cursor, 'F'))
#     one_data = get_user_by_id(cursor, 1)
#     print(one_data)
#     logging.info("Данные таблицы были выведены.")