import requests
import json
import tkinter as tk
import time
from PIL import Image, ImageTk
from urllib.request import urlopen
import io


key = "pV2POVWGHIZGJxPATGLWB5pAH3wB36YG"
print (key)



def getroute():
    global photo
    fromdr = fromVar.get()
    dest = destVar.get()

    fromdr = fromdr.replace(" ", "+")
    dest = dest.replace(" ","+")

    webresponse = requests.get("http://www.mapquestapi.com/directions/v2/route?key="+key+"&from="+fromdr+"&to="+dest)

    #format the output text in JSOn format
    jsonoutput = json.dumps(webresponse.text)

    #write the output of the API request to a file
    with open("output.txt","w")as outfile:
        json.dump(webresponse.json(),outfile)

    jb = webresponse.json()
    
    distance.config(text = "Distance: " +str( jb["route"]["distance"]) )
    distance.pack()

    distance2.config(text = "Time: " +str( jb["route"]["realTime"]) )
    distance2.pack()

    imageurl = jb["route"]["legs"][0]["maneuvers"][0]["mapUrl"]
    print(imageurl)
    u = urlopen(str(imageurl)).read()
    
    im = Image.open(io.BytesIO(u))
    photo = ImageTk.PhotoImage(im)
    distance3 = tk.Label(image = photo)
    distance3.pack()


top = tk.Tk()
top.geometry("300x300")
photo = ""
fromVar = tk.StringVar()
destVar = tk.StringVar()

fromm = tk.Entry (top,textvariable = fromVar)
fromm.pack()


to = tk.Entry (top,textvariable = destVar)
to.pack()

w = tk.Button (top,command = getroute, text = " Enter ", width=17,height=5, bg = "light blue",)
w.pack()

distance = tk.Label(top)
distance2 = tk.Label(top)


top.mainloop()

