from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import signal
import time
import random

class Watchdog(Exception):
    def __init__(self, time=5):
        self.time = time
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(self.time)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)
    def handler(self, signum, frame):
        raise self
    def __str__(self):
        return "The code you executed took more than %ds to complete" % self.time


print('Открытие файла твиттер.txt')
twitter_file=open('твиттер.txt','r')
twitter_f=twitter_file.read().split('\n')
twitter=[]
for t in twitter_f:
    if t!="":
        twitter.append(t)
t_login=[]
t_pass=[]
t_mail=[]
t_phone=[]
t_auth_token=[]
for t in twitter:
    a=t.split(':')
    if a[0]=='login':
        t_login.append(a[1].replace(' ',''))
    elif a[0]=='pass':
        t_pass.append(a[1].replace(' ',''))
    elif a[0]=='mail':
        t_mail.append(a[1].replace(' ',''))
    elif a[0]=='phone':
        t_phone.append(a[1].replace(' ',''))
    elif a[0]=='auth_token':
        t_auth_token.append(a[1].replace(' ',''))
#if len(t_login)!=len(t_pass) or len(t_login)!=len(t_mail) or len(t_login)!=len(t_phone) or len(t_login)!=len(t_auth_token):
#    print('Неверная длина файла твиттер.txt')
#    sys.exit(0)
twitter_file.close()

print('Открытие файла хотмаил.txt')
hotmail_file=open('хотмаил.txt','r')
hotmail_f=hotmail_file.read().split('\n')
hotmail=[]
for h in hotmail_f:
    if h!='':
        hotmail.append(h)
h_login=[]
h_pass=[]
for h in hotmail:
    p=h.split(';')
    if p[0]=='login':
        pp=p[1].split(':')
        h_login.append(pp[1].replace(' ',''))
        h_pass.append(pp[2])
hotmail_file.close()

def check_exists_class(class_,name,n):
    try:
        element=driver.find_elements(By.CLASS_NAME,class_)[n]
        assert element.text==name
    except:
        return False
    return True
def click(class_,name_class,i,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            btn = driver.find_elements(By.CLASS_NAME,class_)[i]
            assert btn.text == name_class
            btn.click()
            print(f"Клик по {name_class}")
            flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 3:
                try:
                    btn.click()
                    print(f"Клик по {name_class}")
                except:
                    pass
                flag = False
    time.sleep(time_after)
    if check_exists_class(class_,name_class,i):
        print(f"Класс {name_class} все еще на странице, повторный клик")
        click(class_,name_class,i,5,2)
def click_one_click(class_,name_class,i,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            btn = driver.find_elements(By.CLASS_NAME,class_)[i]
            assert btn.text == name_class
            btn.click()
            print(f"Клик по {name_class}")
            flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 3:
                try:
                    btn.click()
                    print(f"Клик по {name_class}")
                except:
                    pass
                flag = False
    time.sleep(time_after)
def click_tagname(tagname,name_tagname,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            tag = driver.find_elements(By.TAG_NAME,tagname)
            for t in tag:
                if t.text==name_tagname:
                    print(f"Клик по {name_tagname}")
                    t.click()
                    flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 5:
                flag = False
    time.sleep(time_after)
def click_tagname2(tagname,name_tagname1,name_tagname2,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            tag = driver.find_elements(By.TAG_NAME,tagname)
            for t in tag:
                if t.text==name_tagname1 or t.text==name_tagname2:
                    t.click()
                    print(f"Клик по {t.text}")
                    flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 5:
                flag = False
    time.sleep(time_after)
def click_noname(class_,i,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            btn = driver.find_elements(By.CLASS_NAME,class_)[i]
            btn.click()
            print(f"Клик по классу {class_}")
            flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 5:
                try:
                    btn.click()
                    print(f"Клик по классу {class_}")
                except:
                    pass
                flag = False
    time.sleep(time_after)
def click_id(id_,name_id,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            btn = driver.find_element(By.ID,id_)
            assert btn.text == name_id
            btn.click()
            print(f"Клик по {name_id}")
            flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 5:
                try:
                    btn.click()
                    print(f"Клик по {name_id}")
                except:
                    pass
                flag = False
    time.sleep(time_after)
def click_id_noname(id_,time_before,time_after):
    global driver
    time.sleep(time_before)
    flag=True
    iter_error = 0
    while flag:
        try:
            btn = driver.find_element(By.ID,id_)
            btn.click()
            print(f"Клик по id {id_}")
            flag=False
        except:
            time.sleep(1)
            iter_error += 1
            if iter_error >= 5:
                try:
                    btn.click()
                    print(f"Клик по id {id_}")
                except:
                    pass
                flag = False
    time.sleep(time_after)
def input_id(id_,keys,time_before,time_after):
    global driver
    time.sleep(time_before)
    iter_error=0
    while driver.find_element(By.ID,id_).get_attribute('value')!=keys:
        try:
            driver.find_element(By.ID,id_).clear()
            time.sleep(1)
            driver.find_element(By.ID,id_).send_keys(keys)
        except:
            pass
        iter_error+=1
        if iter_error>5:
            break
    time.sleep(time_after)
def input_class(class_,keys,i,time_before,time_after):
    global driver
    time.sleep(time_before)
    iter_error=0
    while driver.find_elements(By.CLASS_NAME,class_)[i].get_attribute('value')!=keys:
        time.sleep(1)
        try:
            driver.find_elements(By.CLASS_NAME,class_)[i].clear()
            time.sleep(1)
            driver.find_elements(By.CLASS_NAME,class_)[i].send_keys(keys)
        except:
            pass
        iter_error+=1
        if iter_error>5:
            break
    time.sleep(time_after)
def random10():
    string='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890'
    str_mass=list(string)
    random.shuffle(str_mass)
    string_out=''
    for i in range(10):
        string_out=string_out+str_mass[i]
    return string_out
def get_input(class_,i,time_before,time_after):
    global driver
    time.sleep(time_before)
    try:
        out=driver.find_elements(By.CLASS_NAME,class_)[i].text
    except:
        out=""
    time.sleep(time_after)
    return out

repeat=input('Введите количество циклов: ')
rep=0

for rep in range(int(repeat)):
    try:
        with Watchdog(900):
            try:
                print('1. Переходим по ссылке https://login.live.com/login.srf и логинимся в почту используя данные из отдельного txt.')
                driver=webdriver.Firefox(executable_path="C:\jupyter\geckodriver32.exe")
                #driver=webdriver.Chrome()
                driver.set_page_load_timeout(30)
                driver.implicitly_wait(2)
                driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1669241880&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fexch%3d1%26nlp%3d1%26RpsCsrfState%3d03bdfb3c-8c4e-68be-d845-036b041156bc&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
                #Вход аккаунт майкрософт
                print(f'Вход в аккаунт майкрософт логин: {h_login[rep]}')
                input_id('i0116',h_login[rep],4,2)
                click('button_primary','Next',0,1,2)
                print(f'Вход в аккаунт майкрософт пароль: {h_pass[rep]}')
                input_id('i0118',h_pass[rep],1,2)
                click('button_primary','Sign in',0,1,2)
                #click('secondary-text','Skip for now (7 days until this is required)',0,1,2)
                click_noname('secondary-text',0,1,2)
                click('button_primary','Yes',0,1,2)
                click('secondary-text','No thanks',0,1,2)
                time.sleep(3)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при входе в почту (шаг 1)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                #Вход в твиттер
                print('2.Вход в твиттер')
                driver.execute_script("window.open('https://twitter.com/settings/email')")
                time.sleep(3)
                handles=driver.window_handles
                driver.switch_to.window(handles[1])
                #time.sleep(3)
                print(f'Ввод логина твиттер {t_login[rep]}')
                click_noname('r-30o5oe',0,1,2)
                input_class('r-30o5oe',t_login[rep],0,1,2)
                click('css-16my406','Next',8,1,2)
                print(f'Ввод пароля твиттер')
                click_noname('r-30o5oe',1,1,2)
                input_class('r-30o5oe',t_pass[rep],1,1,2)
                click('css-901oao','Log in',22,1,2)
                print(f'Ввод номера телефона {t_phone[rep]}')
                click_noname('r-30o5oe',0,1,2)
                input_class('r-30o5oe',t_phone[rep],0,1,2)
                click('css-901oao','Sign in',27,1,3)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при входе в твиттер (шаг 2)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                #Добавление email адреса
                print('3.Добавление email адреса')
                driver.get('https://twitter.com/settings/email')
                time.sleep(3)
                if driver.current_url=='https://twitter.com/account/access':
                    print(f'Аккаунт твиттера заблокирован')
                    driver.quit()
                    continue
                click_tagname2('span','Update email address','Add email address',1,2)
                #click('css-901oao','Update email address',28,15,2)
                print('3.1 Вводим пароль от твиттера')
                input_class('r-30o5oe',t_pass[rep],0,1,2)
                click('css-901oao','Next',15,1,2)
                print(f'3.2 Вставляем email {h_login[rep]}')
                input_class('r-30o5oe',h_login[rep],0,1,2)
                click('css-901oao','Next',20,1,2)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при добавлении email адреса (шаг 3)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                driver.switch_to.window(handles[0])
                click_noname('secondary-text',0,3,2)
                click_noname('button_primary',0,1,2)
                click_noname('secondary-text',0,1,5)
                click('textContainer-161','Accept All',6,3,2)
                click('textContainer-161','Принять все',6,3,2)
                print('3.3 Принимаем верификационный код по почте')
                #Поиск верификационного кода
                flag=True
                vkladka=0
                while flag:
                    click_noname('ms-Pivot-text',vkladka,3,2)
                    mesg=[]
                    mes=[]
                    #hcptT=''
                    hcptT=driver.find_elements(By.CLASS_NAME,'hcptT')
                    for h in hcptT:
                        mesg=h.text.split('\n')
                        if 'Twitter' in mesg:
                            itert=0
                            k=0
                            while itert<len(mesg):
                                if mesg[itert]=='Twitter':
                                    k=itert+1
                                    break
                                itert+=1
                            if k!=0:
                                mes=mesg[k].split(' ')
                                if ('is' in mes) and ('your' in mes):
                                    flag=False
                                    break
                    if vkladka==0:
                        vkladka=1
                    else:
                        vkladka=0
                #print(mes[0])
                #Вставка верификационного кода
                print('Вставка верификационного кода')
                driver.switch_to.window(handles[1])
                input_class('r-30o5oe',mes[0],0,3,2)
                click('css-901oao','Verify',20,1,2)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при приеме верификационного кода (шаг 3.3)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                #Идем по https://developer.twitter.com/en/portal/products/elevated
                print('Идем по https://developer.twitter.com/en/portal/products/elevated')
                flag=True
                while flag:
                    driver.get('https://developer.twitter.com/en/portal/products/elevated')
                    time.sleep(3)
                    body = driver.find_elements(By.TAG_NAME,'body')[0]
                    body.send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
                    sel=driver.find_elements(By.TAG_NAME,'select')
                    sel_btn=driver.find_elements(By.CLASS_NAME, 'FormSelect')
                    try:
                        ii=0
                        for ii in range(len(sel)):
                            attr_name=sel[ii].get_attribute('name')
                            if attr_name=='countryOfOperation':
                                sel_btn[ii].click()
                                time.sleep(1)
                                sel_btn[ii].click()
                                select1 = Select(sel[ii])
                                select1.select_by_visible_text('United States')
                            if attr_name=='useCase':
                                sel_btn[ii].click()
                                time.sleep(1)
                                sel_btn[ii].click()
                                select2 = Select(sel[ii])
                                select2.select_by_visible_text('Student')
                            if attr_name=='isGovernmentEntity':
                                sel_btn[ii].click()
                                time.sleep(1)
                                sel_btn[ii].click()
                                select3 = Select(sel[ii])
                                select3.select_by_visible_text('No')
                            time.sleep(2)
                    except:
                        pass
                    click_id('tdp__button--js-accept','Accept',1,2)
                    click('Button-label','Let\'s do this',0,1,5)
                    mmm=''
                    try:
                        mmm=driver.find_element(By.ID,'feather-form-field-text-16').text
                    except:
                        mmm=''
                    if mmm=='':
                        flag=False
                body = driver.find_elements(By.TAG_NAME, 'body')[0]
                body.send_keys(Keys.PAGE_DOWN)
                click_noname('Checkbox-input',0,5,2)
                click_one_click('Button-label','Submit',1,2,2)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при создании приложения (шаг 4)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                print('5. Идем на почту и подтверждаем email ')
                #Идем на почту и подтверждаем email
                driver.switch_to.window(handles[0])
                try:
                    time.sleep(2)
                    kol=0
                    for kol in range(15):
                        if check_exists_class('ms-Button-textContainer','Accept All',kol):
                            click('ms-Button-textContainer','Accept All',kol,3,2)
                        if check_exists_class('ms-Button-textContainer','Принять все',kol):
                            click('ms-Button-textContainer','Принять все',kol,3,2)
                except:
                    pass
                flag=True
                vkladka=1
                while flag:
                    click_noname('ms-Pivot-text',vkladka,3,2)
                    hcptT=driver.find_elements(By.CLASS_NAME,'hcptT')
                    for h in hcptT:
                        mesg=h.text.split('\n')
                        #print(mesg)
                        if 'Verify your Twitter Developer Account' in mesg:
                            try:
                                time.sleep(2)
                                kol=0
                                for kol in range(15):
                                    if check_exists_class('ms-Button-textContainer','Accept All',kol):
                                        click('ms-Button-textContainer','Accept All',kol,3,2)
                            except:
                                pass
                            h.click()
                            flag=False
                    if vkladka==0:
                        vkladka=1
                    else:
                        vkladka=0
                click_tagname('a','Confirm your email',5,2)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации при подтверждении письма (шаг 5)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                print('Идем по https://developer.twitter.com/en/portal/products/elevated')
                #Идем по https://developer.twitter.com/en/portal/products/elevated
                time.sleep(3)
                handles=driver.window_handles
                driver.switch_to.window(handles[1])
                driver.get('https://developer.twitter.com/en/portal/products/elevated')
                click('Button-label','Apply',0,5,2)
                time.sleep(3)
                body = driver.find_elements(By.TAG_NAME,'html')[0]
                body.send_keys(Keys.END)
                time.sleep(1)
                body = driver.find_elements(By.TAG_NAME,'body')[0]
                body.send_keys(Keys.END)
                time.sleep(2)
                sel=driver.find_elements(By.TAG_NAME,'select')
                sel_btn=driver.find_elements(By.CLASS_NAME, 'FormSelect')
                ii=0
                for ii in range(len(sel)):
                    attr_name=sel[ii].get_attribute('name')
                    if attr_name=='codingCapabilities':
                        sel_btn[ii].click()
                        time.sleep(1)
                        sel_btn[ii].click()
                        select1 = Select(sel[ii])
                        select1.select_by_visible_text('Highly experienced')
                click_noname('Checkbox-input',0,3,2)
                click_id('tdp__button--js-accept','Accept',2,2)
                click_one_click('Button-label','Next',3,2,2)
                input_class('index__solutionDescriptionTextarea--kCOkg','I\'m blog writer and writing a blogs on my website. Every time I write a blog on my website, I need to publish my blog URL on my Twitter account with using API calls, For that I\'m using a sodial auto poster plugin.',0,3,2)
                click_noname('Switch-control',0,2,2)
                input_class('index__intentScreenTextarea--Lw-6T','Every time I write a blog on website, I need to publish my blog URL on my Twitter account. For that I\'m using a social auto poster plugin.',0,3,2)
                click_noname('Switch-control',2,2,2)
                click_noname('Switch-control',3,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                click_one_click('Button--primary','Next',2,2,2)
                click_noname('Checkbox-input',0,2,2)
                time.sleep(3)
                click('Button-label','Submit',1,2,2)
                time.sleep(3)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации (шаг 6)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                #Идем по https://developer.twitter.com/en/portal/projects-and-apps и жмем +Add Project
                print('Идем по https://developer.twitter.com/en/portal/projects-and-apps и жмем +Add Project')
                driver.get('https://developer.twitter.com/en/portal/projects-and-apps')
                click('Button--primary','Create Project',0,5,2)
                input_class('FormInput',random10(),0,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                time.sleep(3)
                sel=driver.find_elements(By.TAG_NAME,'select')
                for s in sel:
                    attr_name=s.get_attribute('name')
                    if attr_name=='useCase':
                        select5 = Select(s)
                        select5.select_by_visible_text('Making a bot')
                    time.sleep(2)
                click_one_click('Button--primary','Next',0,2,2)
                input_class('FormTextarea',random10(),0,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                click_one_click('Button--primary','Next',0,2,2)
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации (шаг 7)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                flag=True
                while flag:
                    time.sleep(2)
                    out=driver.find_elements(By.CLASS_NAME,'index__title--34re5')[0].text
                    if out=='Name your App':
                        input_class('FormInput','',0,2,2)
                        time.sleep(2)
                        input_class('FormInput',random10(),0,2,2)
                        click_one_click('Button--primary','Next',0,2,2)
                    else:
                        flag=False
                print('Создаем словарь Development')
                Development={}
                Development['api_key']=get_input('index__credentialValue--Ng8r7',0,2,2)
                Development['api_secret']=get_input('index__credentialValue--Ng8r7',1,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                click_one_click('index__tab--2Jxym','Keys and tokens',0,2,2)
                click_one_click('Button--primary','Next',2,2,2)
                Development['access_key']=get_input('index__credentialValue--Ng8r7',3,2,2)
                Development['access_secret']=get_input('index__credentialValue--Ng8r7',4,2,2)
                print('Сохраняем словарь Development')
                '''with open("saveData.json", "a") as outfile:
                    json.dump(Development, outfile,indent="")
                    outfile.write(',\n')'''
                with open("saveData.json", "a") as outfile:
                    outfile.write('{\n')
                    outfile.write(f"\"api_key\": \"{Development['api_key']}\",\n")
                    outfile.write(f"\"api_secret\": \"{Development['api_secret']}\",\n")
                    outfile.write(f"\"access_key\": \"{Development['access_key']}\",\n")
                    outfile.write(f"\"access_secret\": \"{Development['access_secret']}\",\n")
                    outfile.write('},\n')
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации, словарь Development (шаг 8)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                driver.get('https://developer.twitter.com/en/portal/projects-and-apps')
                #print('Ждем 1 минуту')
                time.sleep(15)
                click('Button--primary','Add App',0,5,2)
                click_noname('Tile-selectCircle',1,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                flag=True
                while flag:
                    time.sleep(2)
                    out=driver.find_elements(By.CLASS_NAME,'index__title--34re5')[0].text
                    if out=='Name your App':
                        input_class('FormInput','',0,2,2)
                        time.sleep(2)
                        input_class('FormInput',random10(),0,2,2)
                        click_one_click('Button--primary','Next',0,2,2)
                    else:
                        flag=False
                print('Создаем словарь Staging')
                Staging={}
                Staging['api_key']=get_input('index__credentialValue--Ng8r7',0,2,2)
                Staging['api_secret']=get_input('index__credentialValue--Ng8r7',1,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                click_one_click('index__tab--2Jxym','Keys and tokens',0,2,2)
                click_one_click('Button--primary','Next',2,2,2)
                Staging['access_key']=get_input('index__credentialValue--Ng8r7',3,2,2)
                Staging['access_secret']=get_input('index__credentialValue--Ng8r7',4,2,2)
                print('Сохраняем словарь Staging')
                '''with open("saveData.json", "a") as outfile:
                    json.dump(Staging, outfile,indent="")
                    outfile.write(',\n')'''
                with open("saveData.json", "a") as outfile:
                    outfile.write('{\n')
                    outfile.write(f"\"api_key\": \"{Staging['api_key']}\",\n")
                    outfile.write(f"\"api_secret\": \"{Staging['api_secret']}\",\n")
                    outfile.write(f"\"access_key\": \"{Staging['access_key']}\",\n")
                    outfile.write(f"\"access_secret\": \"{Staging['access_secret']}\",\n")
                    outfile.write('},\n')
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации, словарь Staging (шаг 9)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue

            try:
                driver.get('https://developer.twitter.com/en/portal/projects-and-apps')
                #print('Ждем 1 минуту')
                time.sleep(15)
                click('Button--primary','Add App',0,5,2)
                click_noname('Tile-selectCircle',2,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                flag=True
                while flag:
                    time.sleep(2)
                    out=driver.find_elements(By.CLASS_NAME,'index__title--34re5')[0].text
                    if out=='Name your App':
                        input_class('FormInput','',0,2,2)
                        time.sleep(2)
                        input_class('FormInput',random10(),0,2,2)
                        click_one_click('Button--primary','Next',0,2,2)
                    else:
                        flag=False
                print('Создаем словарь Production')
                Production={}
                Production['api_key']=get_input('index__credentialValue--Ng8r7',0,2,2)
                Production['api_secret']=get_input('index__credentialValue--Ng8r7',1,2,2)
                click_one_click('Button--primary','Next',0,2,2)
                click_one_click('index__tab--2Jxym','Keys and tokens',0,2,2)
                click_one_click('Button--primary','Next',2,2,2)
                Production['access_key']=get_input('index__credentialValue--Ng8r7',3,2,2)
                Production['access_secret']=get_input('index__credentialValue--Ng8r7',4,2,2)
                print('Сохраняем словарь Production')
                '''with open("saveData.json", "a") as outfile:
                    json.dump(Production, outfile,indent="")
                    outfile.write(',\n')'''
                with open("saveData.json", "a") as outfile:
                    outfile.write('{\n')
                    outfile.write(f"\"api_key\": \"{Production['api_key']}\",\n")
                    outfile.write(f"\"api_secret\": \"{Production['api_secret']}\",\n")
                    outfile.write(f"\"access_key\": \"{Production['access_key']}\",\n")
                    outfile.write(f"\"access_secret\": \"{Production['access_secret']}\",\n")
                    outfile.write('},\n')
                print(f'Конец {rep+1} итерации')
                driver.quit()
            except:
                print(f'Ошибка {rep+1} итерации')
                driver.quit()
                with open("error.txt", "a") as out:
                    out.write(f"{datetime.now()} - Ошибка {rep+1} итерации, словарь Production (шаг 9)\n")
                    out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
                    out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
                    out.write("-------------------------------------------------------------------\n")
                continue
    except Watchdog:
        print(f"Время выполнения {rep} итерации закончилось")
        with open("error.txt", "a") as out:
            out.write(f"{datetime.now()} - Время выполнения {rep} итерации закончилось\n")
            out.write(f"Email:{h_login[rep]}:{h_pass[rep]}\n")
            out.write(f"Twitter:{t_login[rep]}:{t_pass[rep]}:{t_phone[rep]}\n")
            out.write("-------------------------------------------------------------------\n")
        continue