# imported the requests library
import requests
import time

def downloadFile(url, type):
    if (type == "t20"):
        fileCreateLocation = "T20_Player_Files/"
    if (type == "odi"):
        fileCreateLocation = "ODI_Player_Files/"
    if (type == "test"):
        fileCreateLocation = "TEST_Player_Files/"

    file_name = url.split("=")[-1] + ".html"
    complete_Name = fileCreateLocation + file_name
    r = requests.get(url)
    with open(complete_Name, 'a+') as f:
        f.write(r.content)

start = 3930
till = 3950

for i in range(start, till):
    t20_url = "http://www.howstat.com/cricket/Statistics/Players/PlayerProgressBat_T20.asp?PlayerID=" + str(i)
    type = "t20"
    downloadFile(t20_url, type)
    time.sleep(1)

