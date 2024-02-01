class ProjectData:
    baseUrl = 'https://demoqa.com'


class InvalidEmailAddresses:
    badEmails = ['badEmail', 'email.domain.com', '@domain.com',
    '#@%^%#$@#$@#.com', 'email@domain.com (Joe Smith)', 'email@domain@domain.com', '.email@domain.com',
    'email.@domain.com', 'email..email@domain.com', 'あいうえお@domain.com', 'email@-domain.com', 'email@.domain.com',
    'email@111.222.333.44444', 'email@domain..com']
  
  
class DemoQATextForm(object):
    pageTitle = 'Text Box'
    cName = "John Snow"
    cEmail = "jsnow@winterfell.com"
    cAddress = "101 Main Street /n New York, NY 10010"
    cPermAddress = cAddress