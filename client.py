import requests
import logging
import time

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT)
logging.info("Client Started")

statusTable={"None":"0","sayHello":"1","uploadSnapshot":"2"}

run=True
while run:
    serverUrl="http://localhost:8888"
    res=requests.get(serverUrl).json()
    logging.debug(res)
    if(res["newMessage"]!=0):
        logging.info("New message")
        logging.info(res["code"])
        if(res["code"]==statusTable["sayHello"]):
            print("Hello,World!")
            requests.get(serverUrl+"/done")
        if(res["code"]==statusTable["uploadSnapshot"]):
            requests.post(serverUrl+"/uploadSnapshot",files=dict(pic=open("doge.jpeg","rb")))
    time.sleep(5)
    run=True