class ProjectData:
    baseUrl = 'https://demoqa.com'


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