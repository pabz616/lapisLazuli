
from faker import Faker
fake = Faker()
day = fake.day_of_month()
month = fake.month_name()


class ProjectData:
    mixedCharSet = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, 北京位於華北平原的西北边缘'
    sanskrit = 'وضع ابن الهيثم تصور واضح للعلاقة بين النموذج الرياضي المثالي ومنظومة الظواهر الملحوظة.'
    sqlInjection = "Robert'); DROP TABLE Students;--"
    jsInjection = "Nice site,  I think I'll take it. <script>alert('Executing JS')</script>"
    brokenHTML = '<i><b>Bold</i></b>'
    xssImageTag = "<img src=x onerror=alert(‘boo’)>"
    newUser = 'turquoise777777QA!$'  # fake.color_name()+'777777'+'QA!$'
    fname = fake.first_name_male()
    lname = fake.last_name()
    email = fake.email()
    tel = '2123334455'
    birthday = day+" "+month+" "+'1975'
    subj = "English"
    address = fake.address()
    randomString = fake.pystr()
    response_limit = float(1.0)  # seconds


class DemoQA(object):
    baseUrl = 'https://demoqa.com'
    usn = 'demoQA'
    pwd = 'blUeMöon97$'
    loginData = {"userName": usn, "password": pwd}
    newUserData = {"userName": ProjectData.email, "password": ProjectData.newUser}
    userId = "83a593e0-4822-48d1-b770-2051ede2ddaa"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlbW9RQSIsInBhc3N3b3JkIjoiYmxVZU3Dtm9uOTckIiwiaWF0IjoxNzEzNDYzNTM4fQ.yXI26P4Zl-TvH2_MqbPRS-U5muGwedeKSjvVD1Lv-VQ"
    tokenHacker = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyTmFtZSI6ImRlbW9RQSIsInBhc3N3b3JkIjoiYmxVZU3Dtm9uOTckIiwiaWF0IjoxNzEzNDYzNTM4fQ.yXI26P4Zl-TvH2_MqbPRS-U5muGwedeKSjv-BaDGuy"
    userData = {"userId": userId}
    adminData = {"userName": "admin", "password": pwd}
    bookData = {"userId": userId, "isbn": "9781449331818"}
    bookCollection = {"userId": userId, "collectionOfIsbns": [
                    {"isbn": "9785303754511"},
                    {"isbn": "9712434961101"},
                    {"isbn": "9578984058653"}]
                    }
    

class NetworkScan(object):
    target_ip = "192.168.1.1/24"
    
    
class APIDemoData(object):
    restful_booker = "https://restful-booker.herokuapp.com"
    bearer_token = "Basic YWRtaW46cGFzc3dvcmQxMjM="
    booking_id = fake.random_digit()
    BOOKING_DETAILS = {
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'totalprice': 747,
        'depositpaid': True,
        'bookingdates': {
            'checkin': '2024-06-01',
            'checkout': '2024-06-30',
        },
        'additionalneeds': f"{fake.color_name} pillows"
    }
    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    } 
    AUTH_DETAILS = {
        'username': 'admin',
        'password': 'password123'
    }
    DEFAULT_DETAILS = {
        'firstname': 'Sally',
        'lastname': 'Brown',
        'totalprice': 747,
        'depositpaid': True,
        'bookingdates': {
            'checkin' : '2023-07-01',
            'checkout' : '2023-07-30'
        },
        'additionalneeds': "furry pillows"
    }
        
        
class ErrorMessages:
    userExistsMsg = 'user exists'
    passwordValidationMsg = "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special character and Password must be eight characters or longer."


class InvalidEmailAddresses:
    badEmails = ['badEmail', 'email.domain.com', '@domain.com',
    '#@%^%#$@#$@#.com', 'email@domain.com (Joe Smith)', 'email@domain@domain.com', '.email@domain.com',
    'email.@domain.com', 'email..email@domain.com', 'あいうえお@domain.com', 'email@-domain.com', 'email@.domain.com',
    'email@111.222.333.44444', 'email@domain..com']
    

class DemoQADates:
    simpleDate = '02/14/2024'
    sampleDateTime = 'February 14, 2024 4:20 PM'
  

class DemoQATextForm(object):
    pageTitle = 'Text Box'
    cName = "John Snow"
    cEmail = "jsnow@winterfell.com"
    cAddress = "101 Main Street /n New York, NY 10010"
    cPermAddress = cAddress


class DemoQAResponseMsg(object):
    created = 'Link has responded with staus 201 and status text Created'
    noContent = 'Link has responded with staus 204 and status text No Content'
    moved = 'Link has responded with staus 301 and status text Moved Permanently'
    badRequest = 'Link has responded with staus 400 and status text Bad Request'
    unauthorized = 'Link has responded with staus 401 and status text Unauthorized'
    forbidden = 'Link has responded with staus 403 and status text Forbidden'
    invalidUrl = 'Link has responded with staus 404 and status text Not Found'