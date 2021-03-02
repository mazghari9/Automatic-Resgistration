from django.shortcuts import render
import sys
from Home.models import Emails
from django.http import HttpResponse 
from subprocess import run,PIPE
from .forms import EmailsForm
from django.shortcuts import get_object_or_404
import os




def home(request):
	return render(request, 'Home/Home.html')

# Create your views here.
def Home(request):
        if request.method == 'POST':
            if request.POST.get('email'):
            	
                post=Emails()
                post.Email= request.POST.get('email')
                post.save()
                return render(request,'Home/Home.html')  
        else:
                return render(request,'Home/Home.html')

def Homee(request):
        if request.method == 'POST':
            if request.POST.get('removeemail'):
            	               
                email1= request.POST.get('removeemail')
                #obj=get_object_or_404(Emails, Email=email1)
                obj=Emails.objects.get(Email=email1)
                obj.delete()
                return render(request,'Home/Home.html')  
        else:
                return render(request,'Home/Home.html')


def Run(request):
	if request.method == 'POST':
		inp= request.POST.get('param')
		out= run([sys.executable,'C://Users//admin//Desktop//WebAppProject//WebApp//Home//PythonScript.py',inp],shell=False,stdout=PIPE)
		print(out)
		return render(request,'Home/Home.html')

    

def Delete(request):
        if request.method == 'POST':
            if request.POST.get('delete'):
            	                              
                Emails.objects.all().delete()
                return render(request,'Home/Home.html')  
        else:
                return render(request,'Home/Home.html')
"""
def Heome(request):
    if request.method == "POST":
        form = EmailsForm(request.POST)
        if form.is_valid():
        	
            form.save()
            return redirect('Home/Home.html')

    else:
        form = EmailsForm()
    return render(request, 'Home/Home.html', {'form': form})
"""
def Run(request):
	if request.method == 'POST':
		if request.POST.get('param'):

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
			from Home.models import Emails
			from selenium.webdriver.remote.webdriver import WebDriver


			#webdriver local location
			path = "C:\Program Files\chromedriver.exe"

			#list of tags and urls
			URLs=[["http://snappysurveys.net/","email","started","first_name","last_name","dob_month","dob_day","dob_year","addr_full","addr_city","addr_state_province","addr_zip","addr_phone","offers1","offers2","offers3","offers4","offers5","submitBtn"],
			["https://youreducationfuture.com/","firstname","lastname","address","city","state","email","areacode","phone","btn btn-large btn-primary"],
			["https://www.nationalpayday.com/","first_name","email","amount","option","submit"],
			["http://mycharityshopping.com/","fname","lname","exampleInputEmail1","pwd1","pwd2","checkbox"],
			["http://mortgageloans101.com/index.php/mortgage-quote-form/","wpforms[fields][9]","wpforms[fields][10]","wpforms[fields][18]","wpforms[fields][14]","wpforms[fields][7]","wpforms[fields][15]","wpforms[fields][0][first]","wpforms[fields][0][last]","wpforms[fields][3]","wpforms[fields][2]","wpforms-107-field_12_1","wpforms[submit]"],
			["http://kidsdineforfree.com/","fname","lname","email","pwd1","pwd2","newsletter","frmaction"],
			["http://emortgagefinders.com/","input_5","input_6","input_50","input_8","input_10","input_51","input_12.3","input_12.6","input_14","gform_next_button_6_1"],
			["http://consumerofferstore.com/","fname","lname","email","contact","state","city","country","checkbox","checkbox1","a-b3xqfy75bf3j","Submit"]]

			#lise of american fake identities
			Identities=[["Mary","M.Pfister","NewYork","Huntington","4662 Duncan Avenue","+1 610-934-1119","11743"],
			["Raymond","M.Gamboa","Kentucky","Owensboro","4072 Coffman Alley","+1 270-691-3671","42301"],
			["Pamela","K.Smith","Georgia","Atlanta","1707 Musgrave Street","+1 404-934-8171","30303"],
			["Nadine","B.Lowe","Arizona","Superstition","423 East Avenue","+1 480-358-3654","85207"],
			["Oscar","L.Merrill","Georgia","Atlanta","411 Pine Garden Lane","+1 770-741-7993","30305"],
			["Theresa","K.Johnson","Florida","Sunrise","1116 Ridenour Street","+1 786-306-3113","33323"],
			["Theodore","J.Mejia","Georgia","Atlanta","2207 Edington Drive","+1 678-799-9599","30303"],
			["Kenneth","E.Pabon","Maryland","Sykesville","15 Woodhill Avenue","+1 410-795-2288","21784"],
			["Juanita","J.Perry","Iowa","Des Moines","4372 Southern Avenue","+1 641-328-8365","50309"],
			["Pamela","J.Chancellor","Iowa","Westside","2497 Centennial Farm Road","+1 712-663-4676","51467"],
			["Mack","P.King","California","Burbank","2181 Quiet Valley Lane","+1 818-972-1068","91502"],
			["Chris","M.Bibb","Ohio","Dayton","1580 College Avenue","+1 937-434-9264","45459"],
			["Dorothy","J.Honeycutt","New Jersey","Camden","939 Valley Street","+1 856-885-6555","08102"],
			["Scott","E.Brown","California","Bakersfield","179 Atha Drive","+1 661-586-6085","93304"],
			["Barry","L.Murchison","Kentucky","Pleasant Ridge","2210 Broaddus Avenue","+1 270-275-3710","40769"],
			["Maye","L.Moseley","Michigan","Grand Rapids","916 Goff Avenue","+1 269-589-1746","49503"],
			["Jerry","Y.Winn","Tennessee","Portland","422 Frum Street","+1 615-325-8391","37148"],
			["Andrew","N.Jones","Ohio","Cincinnati","2576 Goldie Lane","+1 513-374-9889","45214"],
			["Timothy","B.Frye","California","Sherman Oaks","3789 Par Drive","+1 805-808-3371","91403"],
			["Kevin","D.Carrillo","Alabama","Opelika","1774 Fleming Street","+1 334-364-1184","36801"]]
			#["fname","lname","state","city","adress","phone number"]

			#list of e-mails
			emails=[1,2,3,4,5,6,7,8,9,7,8,9,7,8,9,7,8,9,7,8,9,7,8,9,7,8,9]

			#list of proxies
			PROXIES=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
			req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
			proxies = req_proxy.get_proxy_list() #this will create proxy list
			for i in range(20):
			    PROXIES[i]=proxies[i].get_address()

			count = Emails.objects.all().count()
			emails[0]= Emails.objects.first().Email
			k= Emails.objects.first().pk
			k=k+1
			for j in range(1,count-1):
				if Emails.objects.get(pk=k):

					emails[j]=Emails.objects.get(pk=k).Email
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
				i=random.randint(0, 20)
				browser = webdriver.Chrome(path)
				browser.maximize_window()
				browser.get(URLs[0][0])
				time.sleep(2)
				element = browser.find_element_by_name(URLs[0][1])
				element.send_keys(email)
				element = browser.find_element_by_class_name(URLs[0][2])
				element.click()
				window_after = browser.window_handles[1]
				browser.switch_to.window(window_after)
				time.sleep(5)
				element = browser.find_element_by_name(URLs[0][3])
				element.send_keys(Identities[i][0])
				element = browser.find_element_by_name(URLs[0][4])
				element.send_keys(Identities[i][1])
				browser.find_element_by_xpath("//select[@name='dob_month']/option[text()='December']").click()
				browser.find_element_by_xpath("//select[@name='dob_day']/option[text()='1']").click()
				browser.find_element_by_xpath("//select[@name='dob_year']/option[text()='2000']").click()
				element = browser.find_element_by_name(URLs[0][8])
				element.send_keys(Identities[i][4])
				element = browser.find_element_by_name(URLs[0][9])
				element.send_keys(Identities[i][3])
				element = browser.find_element_by_name(URLs[0][10])
				element.send_keys(Identities[i][2])
				element = browser.find_element_by_name(URLs[0][11])
				element.send_keys(Identities[i][6])
				element = browser.find_element_by_name(URLs[0][12])
				element.send_keys(Identities[i][5])
				element = browser.find_element_by_name(URLs[0][13])
				element.click()
				element = browser.find_element_by_name(URLs[0][14])
				element.click()
				element = browser.find_element_by_name(URLs[0][15])
				element.click()
				element = browser.find_element_by_name(URLs[0][16])
				element.click()
				browser.find_element_by_xpath("//input[@name='offers4' and @value=5]").click()
				element = browser.find_element_by_name(URLs[0][18])
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
			    time.sleep(2)
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
			    time.sleep(2)
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
			    time.sleep(2)
			    element = browser.find_element_by_name(URLs[3][1])
    			#element.send_keys(Identities[i][0])
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
			    time.sleep(2)
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
			    time.sleep(2)
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
		
		return render(request,'Home/Home.html')




