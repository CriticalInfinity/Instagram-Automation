import Login
from Open_Browser import driver
from time import sleep
import random 


def InputHashtags():
    hashtags=[]
    numHashtag=0
    while numHashtag<=0: # To prevent users from inputting number of hashtags as less than 0 or equal to 0
        numHashtag=int(input("Enter the number of hashtags you want to enter : "))
    print("Enter the hashtags without space")
    for tags in range(numHashtag): #Takes input of hashtags 
        hashtags.append(input("Enter hashtag "+str(tags+1)+" : "))
    return hashtags
hashtags=InputHashtags()

def InputComments():
    numComment=0
    while numComment<=0: #Same reason as in line 7
        numComment=int(input("Enter the number of comments you want to enter : "))
    print("Enter the comments ")
    comments=[]
    for comment in range(numComment): #Takes input of the comments the user wants to comment on post
        comments.append(input("Enter comment "+str(comment+1)+" : "))
    return comments
comments=InputComments()

def Opens_First_Recent_Post(): #Opens First Recent Post at the time
    try: #If the page does not load, the except block will be executed
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div').click()
        sleep(2)
    except:
        sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div').click()
        sleep(2)

def NextPost():
    driver.find_element_by_xpath('//*[text()="Next"]').click()
    sleep(1)

def CommentsOnPost(comment):
    try:
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment)
        sleep(0.3)
    except:
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea').send_keys(comment)
        sleep(0.3)
    driver.find_element_by_xpath('//button[text()="Post"]').click()
    sleep(0.5)
    

com_per_hashtag=0
while com_per_hashtag<=0: #To take input of the number of comments a user wants to put into an hashtag
    com_per_hashtag=int(input("Enter the number of comments you want to post per hashtag : "))

for tag in hashtags:
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(tag))
    sleep(1)
    Opens_First_Recent_Post()    
    for com in range(com_per_hashtag):
        print("Posted comment ",str(com+1)," on tag ",tag)
        CommentsOnPost(random.choice(comments))
        NextPost()
        sleep(1)


