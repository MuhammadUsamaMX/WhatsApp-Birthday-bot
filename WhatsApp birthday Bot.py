import pandas as pd
import datetime
import webbrowser as web
import pyautogui as gui
import time
import datetime

def msg_sender(cntname, message):
    sel_contact(cntname)
    gui.click(767, 816)
    gui.typewrite(message)  # message
    gui.click(1466, 815)

def sel_contact(cntname):
    web.open("https://web.whatsapp.com/")
    time.sleep(10) #temp change bcz slow network
    gui.click(253, 239)
    gui.typewrite(cntname)
    gui.hotkey('enter')
    gui.sleep(1.5)
if __name__ == "__main__":
    df = pd.read_excel("contact.xlsx") #Your contact birthday file check demo.xlsx
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        bday = item['Birthday']
        if(today == bday) and yearNow not in str(item['Year']):
            msg_sender(str(item['Name']), str(item['message'])) 
            writeInd.append(index)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
    df.to_excel('contact birthday.xlsx', index=False)   
