"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

path = "C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get('www.google.com')"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select
import random
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from models import Emails

#webdriver local location
path = "C:\Program Files\chromedriver.exe"

#list of tags and urls
URLs=[["http://snappysurveys.net/","email","started"],
["https://youreducationfuture.com/","firstname","lastname","address","city","state","email","areacode","phone","btn btn-large btn-primary"],
["https://www.nationalpayday.com/","first_name","email","amount","option","submit"],
["http://mycharityshopping.com/","fname","lname","exampleInputEmail1","pwd1","pwd2","checkbox"],
["http://mortgageloans101.com/index.php/mortgage-quote-form/","wpforms[fields][9]","wpforms[fields][10]","wpforms[fields][18]","wpforms[fields][14]","wpforms[fields][7]","wpforms[fields][15]","wpforms[fields][0][first]","wpforms[fields][0][last]","wpforms[fields][3]","wpforms[fields][2]","wpforms-107-field_12_1","wpforms[submit]"],
["http://kidsdineforfree.com/","fname","lname","email","pwd1","pwd2","newsletter","frmaction"],
["http://emortgagefinders.com/","input_5","input_6","input_50","input_8","input_10","input_51","input_12.3","input_12.6","input_14","gform_next_button_6_1"],
["http://consumerofferstore.com/","fname","lname","email","contact","state","city","country","checkbox","checkbox1","a-b3xqfy75bf3j","Submit"]]

#lise of american fake identities
Identities=[["Mary","M.Pfister","NewYork","Huntington","4045 Lost Creek Road","+1 610-934-1119"],
["Raymond","M.Gamboa","Kentucky","Owensboro","4072 Coffman Alley","+1 270-691-3671"],
["Pamela","K.Smith","Georgia","Atlanta","1707 Musgrave Street","+1 404-934-8171"],
["Nadine","B.Lowe","Arizona","Superstition","423 East Avenue","+1 480-358-3654"],
["Oscar","L.Merrill","Georgia","Atlanta","411 Pine Garden Lane","+1 770-741-7993"],
["Theresa","K.Johnson","Florida","Sunrise","1116 Ridenour Street","+1 786-306-3113"],
["Theodore","J.Mejia","Georgia","Atlanta","2207 Edington Drive","+1 678-799-9599"],
["Kenneth","E.Pabon","Maryland","Sykesville","15 Woodhill Avenue","+1 410-795-2288"],
["Juanita","J.Perry","Iowa","Des Moines","4372 Southern Avenue","+1 641-328-8365"],
["Pamela","J.Chancellor","Iowa","Westside","2497 Centennial Farm Road","+1 712-663-4676"],
["Mack","P.King","California","Burbank","2181 Quiet Valley Lane","+1 818-972-1068"],
["Chris","M.Bibb","Ohio","Dayton","1580 College Avenue","+1 937-434-9264"],
["Dorothy","J.Honeycutt","New Jersey","Camden","939 Valley Street","+1 856-885-6555"],
["Scott","E.Brown","California","Bakersfield","179 Atha Drive","+1 661-586-6085"],
["Barry","L.Murchison","Kentucky","Pleasant Ridge","2210 Broaddus Avenue","+1 270-275-3710"],
["Maye","L.Moseley","Michigan","Grand Rapids","916 Goff Avenue","+1 269-589-1746"],
["Jerry","Y.Winn","Tennessee","Portland","422 Frum Street","+1 615-325-8391"],
["Andrew","N.Jones","Ohio","Cincinnati","2576 Goldie Lane","+1 513-374-9889"],
["Timothy","B.Frye","California","Sherman Oaks","3789 Par Drive","+1 805-808-3371"],
["Kevin","D.Carrillo","Alabama","Opelika","1774 Fleming Street","+1 334-364-1184"]]
#["fname","lname","state","city","adress","phone number"]

#list of e-mails
emails=[]

#list of proxies
PROXIES=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list
for i in range(20):
    PROXIES[i]=proxies[i].get_address()

count = Emails.objects.all().count()
emails[0]= Emails.objects.first()
k= Emails.objects.first().pk
k=k+1
for j in range(1,count-1):
	if Emails.objects.get(pk=k):

		emails[j]=Emails.objects.get(pk=k)
		k=k+1
	else:
		k=k+1

#Registration in 1st website
for email in emails:
    proxy=random.choice(PROXIES)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    browser = webdriver.Chrome(path)
    browser.get(URLs[0][0])
    element = browser.find_element_by_name(URLs[0][1])
    element.send_keys(email)
    element = browser.find_element_by_class_name(URLs[0][2])
    element.click()
    browser.close()

#Registration in 2nd website
for email in emails:
    proxy=random.choice(PROXIES)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    i=random.randint(0, 20)
    browser = webdriver.Chrome(path)
    browser.get(URLs[1][0])
    element = browser.find_element_by_name(URLs[1][1])
    element.send_keys(Identities[i][0])
    element = browser.find_element_by_name(URLs[1][2])
    element.send_keys(Identities[i][1])
    element = browser.find_element_by_name(URLs[1][3])
    element.send_keys(Identities[i][4])
    element = browser.find_element_by_name(URLs[1][4])
    element.send_keys(Identities[i][3])
    element = browser.find_element_by_name(URLs[1][5])
    element.send_keys(Identities[i][2])
    element = browser.find_element_by_name(URLs[1][6])
    element.send_keys(email)
    element = browser.find_element_by_name(URLs[1][7])
    element.send_keys('907')
    element = browser.find_element_by_name(URLs[1][8])
    element.send_keys(Identities[i][5])
    element = browser.find_element_by_class_name(URLs[1][9])
    element.click()
    browser.close()

#Registration in 3nd website
for email in emails:
    proxy=random.choice(PROXIES)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    i=random.randint(0, 20)
    browser = webdriver.Chrome(path)
    browser.get(URLs[2][0])
    element = browser.find_element_by_name(URLs[2][1])
    element.send_keys(Identities[i][0])
    element = browser.find_element_by_name(URLs[2][2])
    element.send_keys(email)
    browser.find_element_by_xpath("//select[@name='amount']/option[text()='$600']").click()
    element = browser.find_element_by_name(URLs[2][5])
    element.click()
    browser.close()

#Registration in 4th website
for email in emails:
    proxy=random.choice(PROXIES)

    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    i=random.randint(0, 20)
    browser = webdriver.Chrome(path)
    browser.get(URLs[3][0])
    element = browser.find_element_by_name(URLs[3][1])
    element.send_keys(Identities[i][0])
    element = browser.find_element_by_name(URLs[3][2])
    element.send_keys(Identities[i][1])
    element = browser.find_element_by_id(URLs[3][3])
    element.send_keys(email)
    element = browser.find_element_by_name(URLs[3][4])
    element.send_keys("password")
    element = browser.find_element_by_name(URLs[3][5])
    element.send_keys("password")
    element = browser.find_element_by_class_name(URLs[3][6])
    element.click()
    element = browser.find_element_by_xpath("//button[@type='submit' and @class='btn btn-orange']")
    element.click()
    browser.close()

#Registration in 5th website
for email in emails:
    proxy=random.choice(PROXIES)

    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    i=random.randint(0, 20)
    browser = webdriver.Chrome(path)
    browser.get(URLs[4][0])
    browser.find_element_by_xpath("//select[@name='wpforms[fields][9]']/option[text()='Refinance']").click()
    browser.find_element_by_xpath("//select[@name='wpforms[fields][10]']/option[text()='Condo']").click()
    browser.find_element_by_xpath("//select[@name='wpforms[fields][18]']/option[text()='Alabama']").click()
    browser.find_element_by_xpath("//select[@name='wpforms[fields][14]']/option[text()='$50,000 - $60,000']").click()
    browser.find_element_by_xpath("//select[@name='wpforms[fields][7]']/option[text()='Excellent (800+)']").click()
    browser.find_element_by_xpath("//select[@name='wpforms[fields][15]']/option[text()='Yes']").click()
    element = browser.find_element_by_name(URLs[4][7])
    element.send_keys(Identities[i][0])
    element = browser.find_element_by_name(URLs[4][8])
    element.send_keys(Identities[i][1])
    element = browser.find_element_by_name(URLs[4][9])
    element.send_keys(Identities[i][5])
    element = browser.find_element_by_name(URLs[4][10])
    element.send_keys(email)
    element = browser.find_element_by_xpath("//input[@type='checkbox' and @id='wpforms-107-field_12_1']")
    element.click()
    #element = browser.find_element_by_id(URLs[4][11])
    #element.click()
    element = browser.find_element_by_name(URLs[4][12])
    element.click()
    browser.close()

#Registration in 6th website
for email in emails:
    proxy=random.choice(PROXIES)

    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":proxy,
        "ftpProxy":proxy,
        "sslProxy":proxy,
        "proxyType":"MANUAL",
    }
    i=random.randint(0, 20)
    browser = webdriver.Chrome(path)
    browser.get(URLs[5][0])
    element = browser.find_element_by_name(URLs[5][1])
    element.send_keys(Identities[i][0])
    element = browser.find_element_by_name(URLs[5][2])
    element.send_keys(Identities[i][1])
    element = browser.find_element_by_name(URLs[5][3])
    element.send_keys(email)
    element = browser.find_element_by_name(URLs[5][4])
    element.send_keys("password")
    element = browser.find_element_by_name(URLs[5][5])
    element.send_keys("password")
    element = browser.find_element_by_name(URLs[5][6])
    element.click()
    element = browser.find_element_by_name(URLs[5][7])
    element.click()
    browser.close()

#Registration in 7th website / later





#"fname","lname","email","contact","state","city","country","checkbox","checkbox1","a-b3xqfy75bf3j","Submit"



#element1 = browser.find_element_by_name(URLs[0][1])
#element1.send_keys("CliftonEBertram@armyspy.com")

#browser.implicitly_wait(5) # seconds
#element1 = browser.find_element_by_name(URLs[8][3])
#element1.send_keys("first")
#browser.implicitly_wait(10)

#element1 = browser.find_element_by_class_name(URLs[0][2])
#element1.click()

#element3 = browser.find_element_by_name(URLs[2][3])
#element3.click()

#browser.find_element_by_xpath("//select[@name='amount']/option[text()='$600']").click()

#Select(browser.find_element_by_name(URLs[2][3])).select_by_value('300')

#element5 = browser.find_element_by_name(URLs[2][5])
#element5.click()
#try:
#    element = WebDriverWait(browser, 10).until(
#        EC.presence_of_element_located((By.class, "started"))
#    )
#    element.click()
#except:
#    browser.quit()
