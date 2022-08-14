from cProfile import label
from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from tkinter import messagebox
import os
# for copy file and folder to another location
import shutil

#Function 1
def select_path():
    # to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


#Function 3
def Downloading():
    return messagebox.showinfo('Wait!!','Your Video Is Downloading')

# function 4 for 144p 
def download_360p():
    get_link = link_field.get()
    user1_path = path_label.cget("text")
    main.title('Processing..')
    vid_360p = YouTube(get_link).streams.filter(res="360p").first().download()
    vid_360p_clip = VideoFileClip(vid_360p)
    vid_360p_clip.close()
    shutil.move(vid_360p, user1_path)
    main.title('Download Completed! Download Another File')

#Function 2 for 480p
def download_480p():
    #ge path
    get_link = link_field.get()
    #selected path
    user2_path = path_label.cget("text")
    main.title('Processing..')
    #Download Video
    vid_480p = YouTube(get_link).streams.filter(res="480p").first().download()
    vid_clip_480p = VideoFileClip(vid_480p)
    vid_clip_480p.close()
    #move file to selected folder
    shutil.move(vid_480p, user2_path)
    main.title('Download Completed! Download Another File')

    # function 4 for 480p 
def download_720p():
    get_link = link_field.get()
    user3_path = path_label.cget("text")
    main.title('Processing..')
    vid_720p = YouTube(get_link).streams.filter(res="720p").first().download()
    vid_720p_clip = VideoFileClip(vid_720p)
    vid_720p_clip.close()
    shutil.move(vid_720p, user3_path)
    main.title('Download Completed! Download Another File')

   # function 4 for 480p 
def download_1080p():
    get_link = link_field.get()
    user4_path = path_label.cget("text")
    main.title('Processing..')
    vid_1080p = YouTube(get_link).streams.filter(res="720p").first().download()
    vid_1080p_clip = VideoFileClip(vid_1080p)
    vid_1080p_clip.close()
    shutil.move(vid_1080p, user4_path)
    main.title('Download Completed! Download Another File')

# function for mp3 
def mp3():
    get_link = link_field.get()
    usermp3_path = path_label.cget("text")
    main.title('Processing..')
    filepath = str(usermp3_path)
    yt = YouTube(str(get_link))
    x = yt.streams.filter(only_audio=True).first().download(filepath)
    base, ext = os.path.splitext(x)
    new_file = base + '.mp3'
    os.rename(x, new_file)

def Downloading_mp3():
    return messagebox.showinfo('Wait','Your MP3 is Downloading')


main = Tk()
title = main.title('Youtube Video Downloader')
canvas = Canvas(main, width=600, height=600)
canvas.pack()

# icon image
icon_image = PhotoImage(file='download.png')
main.iconphoto(False,icon_image)

# logo image
logo_img = PhotoImage(file='logo222.png')
# adjusting logo
logo_img = logo_img.subsample(6, 6)
canvas.create_image(320, 100, image=logo_img)

#link field
link_field = Entry(main, width=50, font=('Arial', 10) )
link_label = Label(main, text="Enter Video URL", font=('Arial', 14))

#Add to window 
canvas.create_window(310, 190, window=link_label)
canvas.create_window(310, 230, window=link_field)

#Select Path for saving the video
path_label = Label(main, text="Select Folder For Download", font=('Arial', 12))
select_btn =  Button(main, text="Select Folder", bg='blue', padx='22', pady='5',font=('Arial', 10), fg='white', command=select_path)

#Add to window
canvas.create_window(310, 280, window=path_label)
canvas.create_window(310, 330, window=select_btn)

#main label
btn_label = Label(main, text="Click here to dowload video", font=('Arial', 14))
canvas.create_window(315, 380, window=btn_label)

#Download btn for 360p

download360_btn = Button(main, text="360p",bg='blue',padx='22', pady='5',font=('Arial', 12), fg='white',command=lambda:[Downloading(), download_360p()])
canvas.create_window(95, 440, window=download360_btn)

# download btn for 
download_btn = Button(main, text="480p",bg='blue',padx='22', pady='5',font=('Arial', 12), fg='white',command=lambda:[Downloading(), download_480p()])
canvas.create_window(220, 440, window=download_btn)

# download btn for 
download_btn = Button(main, text="720p",bg='blue',padx='22', pady='5',font=('Arial', 12), fg='white',command=lambda:[Downloading(), download_720p()])
canvas.create_window(350, 440, window=download_btn)

# download btn for 
download_btn = Button(main, text="1080p",bg='blue',padx='22', pady='5',font=('Arial', 12), fg='white',command=lambda:[Downloading(), download_1080p()])
canvas.create_window(480, 440, window=download_btn)

# label for mp3 btn 
btnmp3_label = Label(main, text="Click here to dowload MP3", font=('Arial', 14))
canvas.create_window(315, 500, window=btnmp3_label)
# btn for mp3
mp3_btn = Button(main, text='Download mp3', bg='blue', padx='11', pady='5', font=( 'Arial', 12), fg='white',command=lambda: [Downloading_mp3(), mp3()])
canvas.create_window(315, 540, window=mp3_btn)



main.mainloop()