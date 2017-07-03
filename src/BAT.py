import unittest
from appium import webdriver
from time import sleep


class BAT(unittest.TestCase):
    def setUp(self):
        capabilities = {
            'automationName': 'Appium',
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'Nexus 9 API 22',
            'app': '/Users/bogdanbucur/PycharmProjects/BAT/src/BAT.apk',
            'appPackage': 'com.udevoffice.Launcher'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

    def test(self):

        for i in range(8):
            try:
                # Input Username
                userField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/username')
                userField.click()
                userField.send_keys('test')
                self.driver.back()

                # Input Password
                passField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/password')
                passField.click()
                passField.send_keys('test')
                self.driver.back()

                # Login
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/loginButton').click()
                sleep(2)

                # Select Location
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/text').click()
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[contains(@text, "SummerProject")]').click()

                # Select Multibrand
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/multibrand').click()
                sleep(4)

                # Stoc Dunhill FC
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.TextView[contains(@index, "1")]').click()
                dunhillFCStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                        '/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]'
                                                                        '/android.widget.EditText[1]')
                dunhillFCStocPachet.click()
                dunhillFCStocPachet.clear()
                dunhillFCStocPachet.send_keys('1000')
                self.driver.back()
                sleep(1)

                dunhillFCStocApaTermala = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                            '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                            '/android.widget.LinearLayout[2]/android.widget.EditText')
                dunhillFCStocApaTermala.click()
                dunhillFCStocApaTermala.clear()
                dunhillFCStocApaTermala.send_keys('1000')
                self.driver.back()
                sleep(1)

                dunhillFCStocCremaDeSoare = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                              '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                              '/android.widget.LinearLayout[3]/android.widget.EditText')
                dunhillFCStocCremaDeSoare.click()
                dunhillFCStocCremaDeSoare.clear()
                dunhillFCStocCremaDeSoare.send_keys('1000')
                self.driver.back()
                sleep(1)

                # Stoc PallMall
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]'
                                                  '/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TextView').click()
                pallmallStocBricheta = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                         '/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.EditText')
                pallmallStocBricheta.click()
                pallmallStocBricheta.clear()
                pallmallStocBricheta.send_keys('1000')
                self.driver.back()
                sleep(1)

                pallmallStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                       '/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                pallmallStocPachet.click()
                pallmallStocPachet.clear()
                pallmallStocPachet.send_keys('1000')
                self.driver.back()
                sleep(1)

                # Stoc Dunhill FS
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.TextView[contains(@index, "1")]').click()
                dunhillFSStoc = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                  '/android.widget.LinearLayout[3]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.EditText')
                dunhillFSStoc.click()
                dunhillFSStoc.clear()
                dunhillFSStoc.send_keys('1000')
                self.driver.back()
                sleep(1)

                # Stoc Kent
                kentStocBricheta = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                     '/android.widget.LinearLayout[4]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.EditText')
                kentStocBricheta.click()
                kentStocBricheta.clear()
                kentStocBricheta.send_keys('1000')
                self.driver.back()
                sleep(1)

                kentStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                   '/android.widget.LinearLayout[4]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                kentStocPachet.click()
                kentStocPachet.clear()
                kentStocPachet.send_keys('1000')
                self.driver.back()
                sleep(1)

                self.driver.scroll(dunhillFSStoc, dunhillFCStocPachet)

                # Stoc Vogue
                vogueStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                    '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.support.v7.widget.RecyclerView'
                                                                    '/android.widget.LinearLayout[1]/android.widget.EditText')
                vogueStocPachet.click()
                vogueStocPachet.clear()
                vogueStocPachet.send_keys('1000')
                self.driver.back()
                sleep(1)

                vogueStocTermala = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                     '/android.widget.LinearLayout[5]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                vogueStocTermala.click()
                vogueStocTermala.clear()
                vogueStocTermala.send_keys('1000')
                self.driver.back()
                sleep(1)

                # Save Stoc
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/save').click()
                sleep(3)

                # Iterate First 8 Brands
                index = i % 8
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                                  '/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TextView[contains(@index, "{0}")]'.format(str(index))).click()
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'
                                                  '/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/bestProductImg').click()

                # Input Phone Number
                sleep(2)
                phoneField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/phone')
                phoneField.click()
                phoneField.send_keys('0732875621')
                self.driver.back()
                sleep(3)

                # Send Code
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/sendPhoneButton').click()

                # Verify Code
                sleep(3)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/sendConfirmationButton').click()

                # Assign prize
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/giveAway').click()

                # Skip error
                try:
                    self.driver.find_element_by_id('android:id/button1').click()
                except:
                    pass

                # Restart
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/restart').click()
                sleep(2)

            except:

                # Iterate First 8 Brands
                index = i % 8
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                                  '/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TextView[contains(@index, "{0}")]'.format(str(index))).click()
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'
                                                  '/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView').click()
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/bestProductImg').click()

                # Input Phone Number
                sleep(2)
                phoneField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/phone')
                phoneField.click()
                phoneField.send_keys('0732875621')
                self.driver.back()
                sleep(3)

                # Send Code
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/sendPhoneButton').click()

                # Verify Code
                sleep(3)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/sendConfirmationButton').click()

                # Assign prize
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/giveAway').click()

                # Skip error
                try:
                    self.driver.find_element_by_id('android:id/button1').click()
                except:
                    pass

                # Restart
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/restart').click()
                sleep(2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BAT)
    unittest.TextTestRunner(verbosity=2).run(suite)
