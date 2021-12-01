from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""


#file location
def openLoaction():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please choose Folder!!",fg="red")

#downlaod video
def DownlaodVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(res="720p",progressive=True,type="video").first()

        elif(choice == choices[1]):
            select = yt.streams.filter(res="360p",progressive=True,type="video").last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True,abr="160kbps",progressive=False,type="audio").first()

        else:
            ytdError.config(text="Try Again!!",fg="red")

    #downlaod Fuction
        select.download((Folder_Name))
        ytdError.config(text="Downlaod Completed!!")


root =Tk()
root.title("Downloader")
root.geometry("350x400")  #set window
root.columnconfigure(0,weight=1)   #set all content in center

ytdLabel = Label(root,text="Enter the URL of the video",font=("jost",15))
ytdLabel.grid()

#entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#error msg
ytdError = Label(root,text="Error Msg",fg="red",font=("jost",10))
ytdError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLoaction)
saveEntry.grid()

#error msg location
locationError = Label(root,text="Error Msg of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download btn
downlaodbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownlaodVideo)
downlaodbtn.grid()

#developer Label
developerlabel = Label(root,text="LPU - Vivek",font=("jost",15))
developerlabel.grid()


root.mainloop()

