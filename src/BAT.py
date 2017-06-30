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
            'app': '/Users/bogdanbucur/PycharmProjects/BAT/src/BATLauncher27.06.2017.apk',
            'appPackage': 'com.udevoffice.Launcher'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

    def test(self):

        for i in range(2):
            try:
                # Input Username
                userField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/username')
                userField.click()
                userField.send_keys('test')
                self.driver.press_keycode('66')

                # Input Password
                passField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/password')
                passField.click()
                passField.send_keys('test')
                self.driver.press_keycode('66')

                self.driver.hide_keyboard()

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
                                                  '/android.widget.TextView[1]').click()
                dunhillFCStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                        '/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]'
                                                                        '/android.widget.EditText[1]')
                dunhillFCStocPachet.click()
                dunhillFCStocPachet.clear()
                dunhillFCStocPachet.send_keys('1000')
                self.driver.back()

                dunhillFCStocApaTermala = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                            '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                            '/android.widget.LinearLayout[2]/android.widget.EditText')
                dunhillFCStocApaTermala.click()
                dunhillFCStocApaTermala.clear()
                dunhillFCStocApaTermala.send_keys('1000')
                self.driver.back()

                dunhillFCStocCremaDeSoare = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                              '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                              '/android.widget.LinearLayout[3]/android.widget.EditText')
                dunhillFCStocCremaDeSoare.click()
                dunhillFCStocCremaDeSoare.clear()
                dunhillFCStocCremaDeSoare.send_keys('1000')
                self.driver.back()

                # Stoc PallMall
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                                                  '/android.widget.TextView').click()
                pallmallStocBricheta = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                         '/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.EditText')
                pallmallStocBricheta.click()
                pallmallStocBricheta.clear()
                pallmallStocBricheta.send_keys('1000')
                self.driver.back()

                pallmallStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                       '/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                pallmallStocPachet.click()
                pallmallStocPachet.clear()
                pallmallStocPachet.send_keys('1000')
                self.driver.back()

                # Stoc Dunhill FS
                dunhillFSStoc = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                  '/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView'
                                                                  '/android.widget.TextView[1]')
                dunhillFSStoc.click()
                dunhillFSStoc.clear()
                dunhillFSStoc.send_keys('1000')
                self.driver.back()

                # Stoc Kent
                kentStocBricheta = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                     '/android.widget.LinearLayout[4]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.EditText')
                kentStocBricheta.click()
                kentStocBricheta.clear()
                kentStocBricheta.send_keys('1000')
                self.driver.back()

                kentStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                   '/android.widget.LinearLayout[4]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                kentStocPachet.click()
                kentStocPachet.clear()
                kentStocPachet.send_keys('1000')
                self.driver.back()

                # Stoc Vogue
                vogueStocPachet = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]'
                                                                         '/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.support.v7.widget.RecyclerView'
                                                                         '/android.widget.LinearLayout[1]/android.widget.EditText')
                vogueStocPachet.click()
                vogueStocPachet.clear()
                vogueStocPachet.send_keys('1000')
                self.driver.back()

                vogueStocTermala = self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.support.v7.widget.RecyclerView'
                                                                       '/android.widget.LinearLayout[5]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.EditText')
                vogueStocTermala.click()
                vogueStocTermala.clear()
                vogueStocTermala.send_keys('1000')
                self.driver.back()

                # Save Stoc
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/save').click()
                sleep(3)

                # Iterate First 8 Brands
                index = i % 8
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                                  '/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TextView[contains(@index, "{0}")]'.format(str(index))).click()
                self.driver.find_element_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]'
                                                  '/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[1]').click()
                sleep(2)
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/bestProductImg').click()

                # Input Phone Number
                sleep(2)
                phoneField = self.driver.find_element_by_id('com.udevoffice.Launcher:id/phone')
                phoneField.click()
                phoneField.send_keys('0732875621')
                self.driver.press_keycode('66')

                # Send Code
                self.driver.find_element_by_id('com.udevoffice.Launcher:id/sendPhoneButton').click()

            except:
                pass

            # index = i % 8
            # self.driver.find_elements_by_xpath('//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout'
            #                                    '/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TextView[contains(@index, {0})]'.format(str(index)))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BAT)
    unittest.TextTestRunner(verbosity=2).run(suite)
