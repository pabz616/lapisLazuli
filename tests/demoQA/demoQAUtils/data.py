class ProjectData:
    baseUrl = 'https://demoqa.com'
    mixedCharSet = 'Lorem ipsum dolor sit amet, Римский император Константин I Великий, 北京位於華北平原的西北边缘'
    sanskrit = 'وضع ابن الهيثم تصور واضح للعلاقة بين النموذج الرياضي المثالي ومنظومة الظواهر الملحوظة.'
    sqlInjection = "Robert'); DROP TABLE Students;--"
    jsInjection = "Nice site,  I think I'll take it. <script>alert('Executing JS')</script>"
    brokenHTML = '<i><b>Bold</i></b>'
    xssImageTag = "<img src=x onerror=alert(‘boo’)>"
    demoQAUsn = 'demoQA'
    demoQAPwd = 'blUeMöon97$'
    

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