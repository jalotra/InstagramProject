import time
import sys
import searching_for_all_hashtags as Searcher
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException , InvalidArgumentException


class LikeAllHashtagsLinks(Searcher.SearchHastags):

    def __init__(self, username, password, HASHTAG):
        super(LikeAllHashtagsLinks,self).__init__(username, password, HASHTAG)
        self.Photolist = []
        

    def do_you_want_to_follow_all(self):
        totalInstaAccountsFound = len(self.Photolist)
        print('\n{0} PEOPLE ACCOUNTS CAN BE SCRAPED OUT FROM THE {1} PAGE\n.DO YOU WANT TO FOLLOW ALL THESE PEOPLE\n'.format(totalInstaAccountsFound ,self.hashtag ))
        
        followInput = input('YES OR NO \n')

        if followInput.lower() == 'yes':
            return True
        else:
            return False
            print('THANKYOU FOR USING ME.')

    def get_name_of_accounts(self):
        self.Photolist = self.all_photos_elements_list()
        for links in self.Photolist:
            time.sleep(self.sleepTime/2)
            self.driver.get(links)
        #xpath for Follow Button: "//button[contains(text(), 'Follow')]"
        
        #xpath for Title : "//a[@title = '*']"
        #xpath for Text : "//a[contains(text(), '*')]"
        # titleElement = self.driver.find_element(By.XPATH,"//a[@title = '']")
        # textElement = self.driver.find_element(By.XPATH, "//a[contains(text(), '*')]") 
        # if titleElement.text() == textElement.text():
        #     followButton.click()
        #     print("The Person with {} username Has been Followed".format(titleElement))

    #    '''
    #     Right Now the class name that holds the nameOfTheInstagramAccount DOM element
    #     is "FPmhX notranslate nJAzx"  this may change with respect to time.SO keep this in Mind.
    #     I tried to do this another way from Line 20 to Line 24 , bUT didn't know how to use regex with xpath.
    #     So sad'''
        #Task is to get the name of the instagram account that you are following:
        #Accomplishing this task with the help of my brain 

            try:
                # Get names of all the Instagram Account that are presnt
                nameOfTheInstagramAccount = self.driver.find_element(By.CLASS_NAME, 'FPmhX.notranslate.nJAzx')
                with open(r'instagram_account_details.txt' , 'a+') as name_output_file:
                    #To know more about the different modes please head to this url:
                    # https://www.geeksforgeeks.org/reading-writing-text-files-python/
                    name_output_file.write('{}\n'.format(nameOfTheInstagramAccount.text))
                
                # Like all the photos 
                # SO I call the click_like_button(self) Button
                self.click_like_button()
                

            except (NoSuchElementException, InvalidArgumentException) as e:
                # self.close_browser()
                print("Name param cannot be found out")

    def click_follow_button(self):
        print('\nWELCOME IF YOU WANT TO FOLLOW ALL THE PEOPLE WHOSE NAMES ARE THERE IN THE instagram_accounts_details.txt FILE \n')
        if self.do_you_want_to_follow_all():
            Photolist = self.all_photos_elements_list()
            for links in Photolist:
                time.sleep(self.sleepTime)
                self.driver.get(links)
                try:
                    followButton = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]")
                    #followButton Works

                    # self.driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length;++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',nameOfTheInstagramAccount)

                    followButton.click()
                except (NoSuchElementException, InvalidArgumentException) as e:
                    print("\nFOLLOW BUTTON CANNOT BE FOUND\n")

    def click_like_button(self):
        try:
            likeButton = self.driver.find_element(By.XPATH , '//button[./span[@aria-label="Like"]]')
            likeButton.click()
            time.sleep(self.sleepTime)

        except (NoSuchElementException, InvalidArgumentException) as e:
            print("\nLIKE BUTTON CANNOT BE FOUND")

            
        

        

       
    #this thing works but is very SLow
    def all_photos_elements_list(self):
        try:
            photosLinkList = self.main()
            return photosLinkList

        except KeyboardInterrupt:
            self.close_browser()

if __name__ == "__main__":
    try:
        LikeObject = LikeAllHashtagsLinks(sys.argv[2], sys.argv[3] , sys.argv[4])
        LikeObject.login_in_instagram()
        LikeObject.get_name_of_accounts()
        LikeObject.click_follow_button()
    except KeyboardInterrupt:
        LikeObject.close_browser()
