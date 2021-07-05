from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def split(word):
    return [char for char in word]


class FHDA_ClassSignUp:
    """
    CLASS ABLE TO AUTOMATE SIGN UP PROCESS FOR CLASSES AT DE ANZA OR FOOTHILL COLLEGE
    """

    def __init__(self, portal_username, portal_password, De_Anza, Foothill, term, CRNs):
        """
        :param portal_username: your portal username
        :param portal_password: your portal password
        :param De_Anza: boolean value, true if signing up at De Anza
        :param Foothill: boolean value, true if signing up at Foothill
        :param term: seasonal quarter ie(winter, fall...etc)
        :param CRNs: list of CRN numbers for the classes you want to sign up for
        """

        self.portal_username = portal_username
        self.portal_password = portal_password
        self.De_Anza = De_Anza
        self.Foothill = Foothill
        self.term = term
        self.CRNs = CRNs
        self.driver = webdriver.Safari()

    def login(self):
        """
        Function logs into to myportal with the provided credentials
        :return:
        """

        logged_in = False
        while not logged_in:
            try:
                self.driver.get('https://myportal.fhda.edu')
                time.sleep(0.5)
                find_username = self.driver.find_element_by_id('j_username')
                find_username.send_keys(self.portal_username)
                find_password = self.driver.find_element_by_id('j_password')
                split_password = split(self.portal_password)
                time.sleep(0.0025)
                for letter in split_password:
                    find_password.send_keys(letter)
                    time.sleep(0.0025)
                find_password.send_keys(Keys.RETURN)
                time.sleep(5)
                logged_in = True
            except Exception as e:
                print('Error occurred. Attempting login again : ', e)

    def locate_student_registration(self):
        """
        Function navigates through the student's portal and finds the app for student registration,
        chooses to add classes, and submits the term and campus of choice
        :return:
        """

        at_add_classes_link = False
        while not at_add_classes_link:
            try:
                apps = self.driver.find_element_by_xpath('//*[@id="react-portal-root"]/div/div[1]/div[1]/ul/li[3]')
                apps.click()
                time.sleep(1.5)
                student_registration = self.driver.find_element_by_class_name("myapps-item-label")
                student_registration.click()
                time.sleep(1.5)
                add_classes = self.driver.find_element_by_link_text('Add or Drop Classes')
                add_classes.click()
                time.sleep(2.5)
                self.driver.get('https://ssb-prod.ec.fhda.edu/PROD/bwskfreg.P_AltPin')
                time.sleep(1)

                self.driver.switch_to.window(self.driver.window_handles[1])
                options = self.driver.find_elements_by_tag_name('option')
                for option in options:
                    text = option.text.lower()
                    if self.De_Anza:
                        if 'de anza' and self.term in text:
                            option.click()
                            time.sleep(.25)
                            option.submit()
                            time.sleep(0.25)
                            break
                    elif self.Foothill:
                        if 'foothill' and self.term in text:
                            option.click()
                            time.sleep(.25)
                            option.submit()
                            time.sleep(.25)
                            break

                at_add_classes_link = True
                time.sleep(1.5)
            except Exception as e:
                print('Error occurred while navigating myportal. Trying again.')

    def enter_classes(self):
        """
        Function inputs the given CRNs and signs you up for your classes
        :return:
        """

        signed_up = False
        while not signed_up:
            try:
                id_string = 'crn_id'
                index = 1
                for CRN in self.CRNs:
                    this_id_string = id_string + str(index)
                    this_CRN = self.driver.find_element_by_id(this_id_string)
                    this_CRN.send_keys(CRN)
                    time.sleep(0.1)
                    index += 1

                submit = self.driver.find_element_by_xpath("//input[@value='Submit Changes']")
                submit.click()
                time.sleep(1)
                ok_button = self.driver.find_element_by_xpath("button[@class='ui-button ui-corner-all ui-widget']")
                ok_button.click()
                time.sleep(10)
                signed_up = True
            except Exception as e:
                print('Error occured while adding classes. Trying again.')

    def sign_up_for_my_classes(self):
        """
        Function does the whole shabang
        :return:
        """

        self.login()
        self.locate_student_registration()
        self.enter_classes()
