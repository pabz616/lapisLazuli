from demoQAComponentLocators.pageElements import PracticeForm
from playwright.sync_api import expect
import datetime

date = datetime.datetime.now()
today = date.strftime("%d"+" "+"%b"+" "+"%Y")


class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.registrationHeader = page.locator(PracticeForm.FORM_TITLE)
        
        # REGISTRATION FORM
        self.student_fname = page.locator(PracticeForm.STUDENT_FIRSTNAME)
        self.student_fname_placeholder = self.student_fname.get_attribute('placeholder')
        self.student_lname = page.locator(PracticeForm.STUDENT_LASTNAME)
        self.student_lname_placeholder = self.student_lname.get_attribute('placeholder')
        self.student_email = page.locator(PracticeForm.STUDENT_EMAIL)
        self.student_email_placeholder = self.student_email.get_attribute('placeholder')
        self.student_is_female = page.locator(PracticeForm.STUDENT_GENDER_F)
        self.student_is_male = page.locator(PracticeForm.STUDENT_GENDER_M)
        self.student_is_neutral = page.locator(PracticeForm.STUDENT_GENDER_O)
        self.student_phone_number = page.locator(PracticeForm.STUDENT_PHONE)
        self.student_phone_number_placeholder = self.student_phone_number.get_attribute('placeholder')
        self.student_dob = page.locator(PracticeForm.STUDENT_DOB)    
        self.student_subjects = page.locator(PracticeForm.STUDENT_SUBJECT)
        self.student_hobby_sports = page.locator(PracticeForm.STUDENT_HOBBY1)
        self.student_hobby_reading = page.locator(PracticeForm.STUDENT_HOBBY2)
        self.student_hobby_music = page.locator(PracticeForm.STUDENT_HOBBY3)
        self.student_profile_pic_upload = page.locator(PracticeForm.STUDENT_PIC_UPLOAD)
        self.student_address_input = page.locator(PracticeForm.STUDENT_ADDR)
        self.student_address_placeholder = self.student_address_input.get_attribute('placeholder')
        self.student_address_state = page.locator(PracticeForm.STUDENT_STATE_DDL)
        self.student_address_state_input = page.locator(PracticeForm.STUDENT_STATE_INPUT)
        self.student_address_city = page.locator(PracticeForm.STUDENT_CITY_DDL)
        self.submit_form_button = page.locator(PracticeForm.SUBMIT_BUTTON)
        
        # CONFIRMATION POP-UP
        self.confirmation_modal = page.locator(PracticeForm.CONFIRMATION_WINDOW)
        self.close_modal_button = page.locator(PracticeForm.CLOSE_BUTTON)
        
    def checkUI(self):
        expect(self.student_fname).to_be_visible()
        expect(self.student_fname).to_be_empty()
        expect(self.student_fname_placeholder).to_have_text('First Name')
        #
        expect(self.student_lname).to_be_visible()
        expect(self.student_lname).to_be_empty()
        expect(self.student_lname_placeholder).to_have_text('Last Name')
        #
        expect(self.student_email).to_be_visible()
        expect(self.student_email).to_be_empty()
        expect(self.student_email_placeholder).to_have_text('name@example.com')
        #
        expect(self.student_is_male).to_be_visible()
        expect(self.student_is_male).to_have_text('Male')
        expect(self.student_is_male).not_to_be_checked()
        #
        expect(self.student_is_female).to_be_visible()
        expect(self.student_is_female).to_have_text('Female')
        expect(self.student_is_female).not_to_be_checked()
        #
        expect(self.student_is_neutral).to_be_visible()
        expect(self.student_is_neutral).to_have_text('Other')
        expect(self.student_is_neutral).not_to_be_checked()
        #
        expect(self.student_phone_number).to_be_visible()
        expect(self.student_phone_number).to_be_empty()
        expect(self.student_phone_number_placeholder).to_have_text('Mobile Number')
        #
        expect(self.student_dob).to_be_visible()
        expect(self.student_dob).not_to_contain_text(f"{today}")
        #
        expect(self.student_subjects).to_be_visible()
        expect(self.student_subjects).to_be_empty()
        #
        expect(self.student_hobby_sports).to_be_visible()
        expect(self.student_hobby_sports).not_to_be_checked()
        expect(self.student_hobby_sports).to_have_text('Sports')
        #
        expect(self.student_hobby_reading).to_be_visible()
        expect(self.student_hobby_reading).not_to_be_checked()
        expect(self.student_hobby_reading).to_have_text('Reading')
        #
        expect(self.student_hobby_music).to_be_visible()
        expect(self.student_hobby_music).not_to_be_checked()
        expect(self.student_hobby_music).to_have_text('Music')
        #
        expect(self.student_profile_pic_upload).to_be_visible()
        expect(self.student_profile_pic_upload).to_be_enabled()
        expect(self.student_profile_pic_upload).to_be_contain_text('Choose File')
        #
        expect(self.student_address_input).to_be_visible()
        expect(self.student_address_input).to_be_empty()
        expect(self.student_address_input_placeholder).to_have_text('Current Address')
        #
        expect(self.student_address_state).to_be_visible()
        expect(self.student_address_city).to_be_visible()
        #
        expect(self.submit_form_button).to_be_visible()
        expect(self.submit_form_button).to_be_enabled()
        expect(self.submit_form_button).to_contain_text('Submit')
          
    def submitForm(self, first, last, email, tel, birthday, subj, address):
        self.student_fname.fill(first)
        self.student_lname.fill(last)
        self.student_email.fill(email)
        self.student_is_male.click()
        self.student_phone_number.fill(tel)
        self.student_dob.fill(birthday)
        self.page.keyboard.press("Enter")
        self.student_subjects.click()
        self.student_subjects.type(subj)
        self.page.keyboard.press("Tab")
        self.student_hobby_music.click()
        self.student_address_input.fill(address)
        
        self.student_address_state_input.fill('NCR')
        self.page.keyboard.press("Enter")
        
        self.student_address_state.click()
        self.student_address_state.type('Noida')
        self.page.keyboard.press("Enter")
        self.submit_form_button.click()
        
    def confirmSuccessfulRegistration(self):
        expect(self.confirmation_modal).to_be_visible()
        self.close_modal_button.click()
        
    def submitBlankForm(self):
        self.submit_form_button.click()
        
    def confirmUnsuccessfulRegistration(self):
        expect(self.confirmation_modal).not_to_be_visible()