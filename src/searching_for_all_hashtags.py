import login_into_instagram as Logger
from selenium.webdriver.common.by import By
import time
import re
import sys

class SearchHastags(Logger.LoginInstagram):
    def __init__(self, username, password, HASHTAG):
        self.hashtag = HASHTAG
        self.hashtagList = [] 
        self.hashtagLinksList = []
        super(SearchHastags,self).__init__(username, password)
    
    def print_login_details(self):
        print("username : {} \npassword : {}".format(self.username, self.password))

    
    def print_hastag_list(self):
        try:
            for lines in self.hashtagList:
                print(lines)
        except len(self.hashtagList) == 0:
            print('HASHTAG LIST IS EMPTY')

    def hastag_list_appender(self):
        with open('filename.txt', 'r') as file:
            for lines in file:
                    self.hashtagList.append(lines)

    def print_list_elements(self, AnyList):
        count = 0
        for elements in AnyList:
            try:
                count += 1
                print(elements)
            except elements == None:
                pass

    def pattern_finder(self, variableToBeMatched):
        # This can change with respect to changes in netflix developers changing the elements urls.
        # pattern = re.compile(r'\w+:/.\w+[.]\w+[.]\w+/p/\w+[-]\w+[/]')
        
        pattern = re.compile(r'\w+:/.\w+[.]\w+[.]\w+/p/\w*')
        answer = re.match(pattern , variableToBeMatched)
        if answer is not None:
            return answer.group()
        

            
    def getting_photos_links(self, hashtag = '\0'):
        navigateForward = input('DO YOU WANT TO GO TO TAGS PAGE\n')

        if navigateForward == 'yes' or navigateForward == 'Yes':
            self.driver.get('https://www.instagram.com/explore/tags/' + str(hashtag))
            time.sleep(self.sleepTime)
            searchPages = int(input('\nENTER THE NUMBER OF TIMES DO YOU WANT TO SCROLL THE {} PAGE  '.format(hashtag)))
            while(searchPages):
   
                #Done appending the hrefs Link of all the elements starting with anchor tags  
                pictureHrefElements = self.driver.find_elements(By.TAG_NAME, 'a')
                pictureHrefs = []
                for elements in pictureHrefElements:
                    # pictureHrefs.append(elements.get_attribute('href')) 
                    newElement = elements.get_attribute('href')
                    self.hashtagLinksList.append(self.pattern_finder(newElement))

                    '''Here all the href elements are getting in 
                    For example : 
                    if hastag == 'singers'
                    Then the pictureHrefs that I got are :
                    https://www.instagram.com/p/By997KiiCc8/ 1
                    https://www.instagram.com/p/By-nf4Jiw0o/ 2
                    https://www.instagram.com/p/By-gGOpn392/ 3
                    https://www.instagram.com/p/By8FY37nrn2/ 4
                    https://www.instagram.com/p/By9jTkIHxM0/ 5
                    https://www.instagram.com/p/By8Fm-kh6CU/ 6
''' 
                #Now I have to extract only the elements that are enclosed into the /p/ tags 
                #for example this baby right here --> https://www.instagram.com/p/By-zmY3B7Ke/
                #Using some regex Magic

                # time.sleep(self.sleepTime)

                # Uncomment This
                # pictureHrefs = self.pattern_finder(pictureHrefs)

                # self.hashtagLinksList.append(pictureHrefs)
                # pictureHrefs = [href for href in pictureHrefs if hashtag in href]
                # print(hashtag + 'photos are :' + str(len(pictureHrefs)))

                # self.print_list_elements(pictureHrefs)
                # for hrefElements in pictureHrefElements:
                #     try:
                #         likeButton = self.driver.find_element(By.LINK_TEXT, 'Like')
                #         likeButton.click()
                #         time.sleep(self.sleepTime*10)
                #     except Exception:
                #         time.sleep(1)   
                time.sleep(self.sleepTime/2) 
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
                time.sleep(self.sleepTime/2)    
                searchPages -= 1 
        else:
            self.getting_photos_links(hashtag)

    
    def main(self):
        self.getting_photos_links(self.hashtag)
        time.sleep(self.sleepTime)
        return list(filter(None, self.hashtagLinksList)) 

        
        
        
                





    # def tags(self, *args, **kwargs):
    #     try: 


    #     raise NotImplementedError


if __name__ == "__main__":
    SearchObject = SearchHastags(sys.argv[1], sys.argv[2], sys.argv[3])
    SearchObject.login_in_instagram() #Working
    # SearchObject.getting_photos_links('singers')
    print(SearchObject.main())
    # SearchObject.print_login_details() #Working