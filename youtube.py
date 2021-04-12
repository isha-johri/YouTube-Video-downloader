from pytube import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import *


#total size container
file_size = 0

def startDownload():
      global file_size
      try:
          url = urlField.get()
          print(url)
          #changing button text
          dBtn.config(text='Please wait....')
          dBtn.config(state=DISABLED)
          path_to_save_video = askdirectory()
          if path_to_save_video is None:
              return
          #creating objeect with url...
          ob = YouTube(url)
          #strms = ob.streams.all()
          #for s in strms:
          #    print(s)
          strm = ob.streams.first()

          vTitle.config(text=strm.title)
          vTitle.pack(side=TOP)
          print(file_size)

          #print(strm)
          #print(strm.filesize)
          #print(strm.title)
          #print(ob.description)
          #now downloading the video
          strm.download(path_to_save_video)
          print("done...")
          dBtn.config(text="Start Download")
          dBtn.config(state=NORMAL)
          showinfo("Download Finished", "Downloaded Successfully")
          urlField.delete(0, END)
          vTitle.pack_forget()

      except Exception as e:
          print(e)
          print("error !!")



#starting gui building
main = Tk()

#setting the title
main.title("My YouTube Downloader")

#set the icon
main.iconbitmap('icon.ico')

main.geometry("500x600")

#heading icon
file = PhotoImage(file='yotube logo.jpg')
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

# url textifield
urlField = Entry(main, font=("verdana", 20), justify=CENTER)
urlField.pack(side=TOP, pady=10)
#download button
dBtn = Button(main, text="start download", font=("verdana", 20),relief='ridge',command=startDownload)
dBtn.pack(side=TOP,pady=10)

#video title
vTitle = Label(main,text="video title")

#vTitle.pack(side=TOP)
main.mainloop()
