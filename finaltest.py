from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
import tkinter
from tkinter import *
from tkinter import simpledialog

main = Tk()
main.geometry("1500x800")
main.config(bg='lightblue')
main.title('Healthbot')
intro = "------Welcome to Healthbot! We're here to check in with you!------"
messageVar = Message(main, text = intro) 
messageVar.config(bg='lightblue', width=800, font=("Helvetica", 24))
messageVar.pack()

# question1
question1 = simpledialog.askstring(title='question1', prompt = 'have you had water today(Y/N)')

# question2
question2 = simpledialog.askstring(title='question2', prompt = 'How many hours of sleep did you get?')
# question3
question3 = simpledialog.askinteger(title='question3', prompt = 'What are you feeling today on a scale of 1-10 (1 being worst, 10 being the best):')

# list of emotions
emotiontitle = Message(main, text = '-----List of Emotions-----')
emotionList = ["Accepting", "Joy", "Angry", "Annoyed", "Courageous", "Powerful", "Connected", "Loving", "Sad", "Disconnected", "Fragile", "Embarrassed", "Grateful", "Guilt", "Hopeful", "Powerless", "Calm", "Unsettled"]
displayList = []
for emotion in emotionList:
    display = Message(main, text = emotion)
    display.config(bg = 'lightblue', width = 500)
    display.pack()
    displayList.append(display)

# question4
question4 = simpledialog.askstring(title='emotions', prompt='Select the emotion that you feel most right now: ')

# question4 selenium
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(f'https://www.google.com/search?q=what+to+do+when+you+are+{question4}&start=0')

for display in displayList:
    display.pack_forget()

# options selenium
opttitle = '-----Here are your options-----'

optiontitle = Message(main, text = opttitle) 
optiontitle.config(bg='lightblue', width=500)
optiontitle.pack()

optionList = ['1. therapy', '2. youtube video' ,'3. yoga', '4. inspirational motivation', '5. google image', '6. book rec', '7. movie rec']

for option in optionList:
  displayOption = Message(main, text = option)
  displayOption.config(bg = 'lightblue', width = 500)
  displayOption.pack()


option = simpledialog.askinteger(title = "option", prompt= 'Pick one(1-7)')

#------therapy------
if option == 1:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/imghp?hl=EN')
#------calming music video------
elif option == 2:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/watch?v=lFcSrYw-ARY')
# ------yoga video------
elif option == 3:
    driver = webdriver.Chrome(ChromeDriverManager().install())  
    driver.get('https://www.youtube.com/watch?v=v7AYKMP6rOE')
#-----quote generator------
elif option == 4:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.unitpedia.com/motivational-quote-generator/')
    driver.execute_script("window.scrollTo(0, 350)")
#------favorite animal image------
elif option == 5:
    search_term = simpledialog.askstring(title = 'favanimal', prompt = "Favorite animal: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/search?q='+search_term+'&start=0')
#------book generator------
elif option == 6:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.whatshouldireadnext.com/')
#------rotten tomatoes------
elif option == 7:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.rottentomatoes.com/top/")

main.mainloop()