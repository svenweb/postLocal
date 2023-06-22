import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time

# Author: Sven Jensen
# Purpose: Create listings on craigslist

def jsonToDict(json):
    return json.loads(json)


def createSession(cookies):
    print("Collecting cookies...")
    session_cookie = next(cookie for cookie in cookies if cookie["name"] == "cl_session")
    login_cookie = next(cookie for cookie in cookies if cookie["name"] == "cl_login")
    b_cookie = next(cookie for cookie in cookies if cookie["name"] == "cl_b")

    # Session object to keep cookies and stuff
    s = requests.Session()
    s.cookies.set("cl_login",str(login_cookie), domain=".craigslist.org")
    s.cookies.set("cl_session",str(session_cookie), domain=".craigslist.org")
    s.cookies.set("cl_b",str(b_cookie), domain=".craigslist.org")
    
    return [s,s.cookies]

#sub Area
def subArea(index, r, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"n":index, "cryptedStepCheck":cryptedStepCheck}, verify=False, cookies=cookies)

#type
def type(id, r, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"id":"fso", "cryptedStepCheck":cryptedStepCheck}, verify=False, cookies=cookies)


#Category
def category(id, r, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"id":id, "cryptedStepCheck":cryptedStepCheck}, verify=False, cookies=cookies)


#EDIT
def edit(r, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"PostingTitle":"Best Bicycle!!","price":"1000","geographic_area":"North Van","postal":"V7N2G4","PostingBody":"description","bicycle_frame_size_freeform":"Medium","sale_manufacturer":"","sale_model":"","serial_number":"","bicycle_type":"8","bicycle_wheel_size":"9","bicycle_frame_material":"2","bicycle_suspension":"","bicycle_brake_type":"","bicycle_handlebar_type":"","bicycle_electric_assist":"","condition":"","language":"5","FromEMail":"bit4104@gmail.com","Privacy":"C","go":"continue","cryptedStepCheck":cryptedStepCheck}, verify=False, cookies=cookies)



#GEO
def geo(r, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"xstreet0": None, "xstreet1": None, "city": None, "postal": "V", "lat": "49.35", "lng": "-123.0679", "AreaID": "16", "draggedpin": "0", "geocoder_latitude": "49.35", "geocoder_longitude": "-123.0679", "geocoder_accuracy": "25", 
                                                                           "cryptedStepCheck": cryptedStepCheck}, headers={"Sec-GPC": "1"}, verify=False, cookies=cookies)

#IMAGES
def images(r, path, s, cookies):
    soup = BeautifulSoup(r.text, "html.parser")
    cryptedStepCheck = soup.find("input", {"name":"cryptedStepCheck"})["value"]
    return s.post(r.url, data={"cryptedStepCheck":cryptedStepCheck, "a": "fin", "go": "Done with Images"}, headers={"Sec-GPC": "1"}, verify=False, cookies=cookies)



def login(playwright):
    print("Logging in...")
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto('https://accounts.craigslist.org/login/')
    
    page.fill('#inputEmailHandle', 'bit4104@gmail.com')
    page.fill('#inputPassword', 'The1doogielester!')
    page.click('#login')
    
    page.wait_for_load_state()

    cookies = page.context.cookies()
    return cookies



def publish(playwright, r, cookies):
    cookies = []
    for cookie in cookies:
        cookies.append({'name':str(cookie.name), 'value':str(cookie.value), 'path':str(cookie.path), 'domain':str(cookie.domain), 'secure':cookie.secure})

    
    print("Publishing Ad...")
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context()
    context.add_cookies(cookies)
    page = browser.new_page()
    page.goto(r.url)
    page.click('button[name="go"]')
    page.wait_for_load_state()
    




def main(metadata):
    
    
    #Login and get cookies
    with sync_playwright() as playwright:
        cookies = login(playwright)

        
    
    #Create session with cookies
    sesh = createSession(cookies)
    sessionCookies = sesh[1]
    s = sesh[0]
    print("Creating Ad...")

    r = s.get("https://post.craigslist.org/c/van", verify=False, cookies = sessionCookies)
    

    subResponse = subArea(metadata['subarea'], r, s, sessionCookies)
    typeResponse = type(1, subResponse, s, sessionCookies)
    catResponse = category(1, typeResponse, s, sessionCookies)
    editResponse = edit(catResponse, s, sessionCookies)
    geoResponse = geo(editResponse, s, sessionCookies)
    imageResponse = images(geoResponse, "C:\\Users\\danie\\Desktop\\bike.jpg", s, sessionCookies)


    with sync_playwright() as playwright:
        publish(playwright,imageResponse, cookies)



subArea = {
    'city of vancouver':'1',
    'north shore':'2',
    'burnaby/newwest':'3',
    'delta/surrey/langley':'4',
    'tricities/pitt/maple':'5',
    'richmond':'6'
    }

type = {
    'job offered':'jo',
    'gig offered':'go',
    'resume / job wanted':'jw',
    'housing offered':'ho',
    'housing wanted':'hw',
    'for sale by owner':'fso',
    'for sale by dealer':'fsd',
    'wanted by owner':'iwo',
    'wanted by dealer':'iwd',
    'service offered':'so',
    'community':'c',
    'event / class':'e',
    }

category = {
            'antiques - by owner': '150', 'appliances - by owner': '149', 'arts & crafts - by owner': '135', 
            'atvs, utvs, snowmobiles - by owner': '191', 'auto parts - by owner': '122', 'auto wheels & tires - by owner': '203', 
            'aviation - by owner': '208', 'baby & kid stuff - by owner': '107', 'barter': '42', 'bicycle parts - by owner': '197', 
            'bicycles - by owner': '68', 'boat parts - by owner': '201', 'boats - by owner': '119', 'books & magazines - by owner': '92',
            'business/commercial - by owner': '134', 'cars & trucks - by owner': '145', 'cds / dvds / vhs - by owner': '117',
            'cell phones - by owner': '153', 'clothing & accessories - by owner': '94', 'collectibles - by owner': '95', 
            'computer parts - by owner': '199', 'computers - by owner': '7', 'electronics - by owner': '96', 'farm & garden - by owner': '133',
            'free stuff': '101', 'furniture - by owner': '141', 'garage & moving sales': '73', 'general for sale - by owner': '5', 
            'health and beauty - by owner': '152', 'heavy equipment - by owner': '193', 'household items - by owner': '97', 
            'jewelry - by owner': '120', 'materials - by owner': '136', 'motorcycle parts - by owner': '195', 'motorcycles/scooters - by owner': '69',
            'musical instruments - by owner': '98', 'photo/video - by owner': '137', 'rvs - by owner': '124', 'sporting goods - by owner': '93', 
            'tickets - by owner': '44', 'tools - by owner': '118', 'toys & games - by owner': '132', 
            'trailers - by owner': '205', 'video gaming - by owner': '151', 'wanted - by owner': '20'
    }







jsonInterpreter = {
    'subArea':{'city of vancouver':'1','north shore':'2','burnaby/newwest':'3','delta/surrey/langley':'4','tricities/pitt/maple':'5','richmond':'6'},
    'type':{'for sale by dealer':'fsd','for sale by owner':'fso'}, 
    'category':
            {
            'antiques - by owner': '150', 'appliances - by owner': '149', 'arts & crafts - by owner': '135', 
            'atvs, utvs, snowmobiles - by owner': '191', 'auto parts - by owner': '122', 'auto wheels & tires - by owner': '203', 
            'aviation - by owner': '208', 'baby & kid stuff - by owner': '107', 'barter': '42', 'bicycle parts - by owner': '197', 
            'bicycles - by owner': '68', 'boat parts - by owner': '201', 'boats - by owner': '119', 'books & magazines - by owner': '92',
            'business/commercial - by owner': '134', 'cars & trucks - by owner': '145', 'cds / dvds / vhs - by owner': '117',
            'cell phones - by owner': '153', 'clothing & accessories - by owner': '94', 'collectibles - by owner': '95', 
            'computer parts - by owner': '199', 'computers - by owner': '7', 'electronics - by owner': '96', 'farm & garden - by owner': '133',
            'free stuff': '101', 'furniture - by owner': '141', 'garage & moving sales': '73', 'general for sale - by owner': '5', 
            'health and beauty - by owner': '152', 'heavy equipment - by owner': '193', 'household items - by owner': '97', 
            'jewelry - by owner': '120', 'materials - by owner': '136', 'motorcycle parts - by owner': '195', 'motorcycles/scooters - by owner': '69',
            'musical instruments - by owner': '98', 'photo/video - by owner': '137', 'rvs - by owner': '124', 'sporting goods - by owner': '93', 
            'tickets - by owner': '44', 'tools - by owner': '118', 'toys & games - by owner': '132', 
            'trailers - by owner': '205', 'video gaming - by owner': '151', 'wanted - by owner': '20'
            }
    }

wheelSize = {'wheel size':{'10 in':'1','12 in':'2','14 in':'3','16 in':'4','18 in':'5','20 in':'6','24 in':'7','26 in':'8','27 in':'9','28 in':'10','29 in':'11','650B':'12','650C':'13','700C':'14','other/unknown':'15'}}
frameMaterial = {'frame material':{'alloy':'1','aluminum':'2','carbon fiber':'3','composite':'4','scandium':'5','steel':'6','titanium':'7','other/unknown':'8'}}
bicycleType = {'bicycle type':{'bmx':'1','cargo/pedicab':'2','cruiser':'3','cyclocross':'4','folding':'5','hybrid/comfort':'6','kids':'7','mountain':'8','recumbent/trike':'9','road':'10','tandem':'11','track':'12','other/unknown':'13'}}
