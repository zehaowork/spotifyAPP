import api_request as ur
from tkinter import messagebox
import tkinter as tk
from playsound import playsound
from PIL import ImageTk
#main window
window = tk.Tk()


# stores result for one search
result = None
# current page count
counter = 0
# current track page count
track_counter = 0


# creates widget
search_frame = tk.Frame(window)
search_frame.pack(side='left', expand=True)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=0)

search_button = tk.Button(search_frame, text='Search', command=lambda : search_control(search_entry))
search_button.grid(row=1, column=0, columnspan=3)

info_frame = tk.Frame(window)
info_frame.pack(side='left',expand=True)

profile_pic_label = tk.Label(info_frame)
profile_pic_label.pack()

info_grid = tk.Frame(info_frame)
info_grid.pack()

artist_name_label = tk.Label(info_grid, text='Name')
artist_name_label.grid(row=0, column=0)
artist_name_label_entry = tk.Label(info_grid)
artist_name_label_entry.grid(row=0, column=1)

pop_label = tk.Label(info_grid, text='Popularity')
pop_label.grid(row=1, column=0)
pop_label_entry = tk.Label(info_grid)
pop_label_entry.grid(row=1, column=1)

follower_label = tk.Label(info_grid, text='Follower')
follower_label.grid(row=2, column=0)
follower_label_entry = tk.Label(info_grid )
follower_label_entry.grid(row=2, column=1)

genre_label = tk.Label(info_grid, text='Genre')
genre_label.grid(row=3, column=0)
genre_label_entry = tk.Label(info_grid)
genre_label_entry.grid(row=3, column=1)

top_track_label = tk.Label(info_grid,text='Top Track')
top_track_label.grid(row=4, column=0)
top_track_label_entry = tk.Label(info_grid)
top_track_label_entry.grid(row=4,column=1)

up_btn = tk.Button(info_grid, text='Up', width=10,command=lambda: display_result_up())
up_btn.grid(row=5, column=0,)
down_btn = tk.Button(info_grid,text='Down', width=10,command=lambda: display_result_down())
down_btn.grid(row=5, column=1)


track_player_frame = tk.Frame(window)
track_player_frame.pack(side = 'left')

track_name = tk.Label(track_player_frame,text='Track Name')
track_name.grid(row = 0,column =0)


track_name_entry = tk.Label(track_player_frame)
track_name_entry.grid(row = 0,column =1)

track_pop = tk.Label(track_player_frame,text='Popularity')
track_pop.grid(row = 1,column =0)

track_pop_entry = tk.Label(track_player_frame)
track_pop_entry.grid(row = 1,column =1)

track_play_btn = tk.Button(track_player_frame,text="PLAY",width=0,command=lambda: play_audio())
track_play_btn.grid(row=2,column=0,columnspan=2)



track_up_btn = tk.Button(track_player_frame, text='Up', width=10,command=lambda: display_track_result_up())
track_up_btn.grid(row=3, column=0)
track_down_btn = tk.Button(track_player_frame,text='Down', width=10, command = lambda: display_track_result_down())
track_down_btn.grid(row=3, column=1)


# event command for search button,execute one search
# param: search text box
def search_control(search_entry):
    global counter
    global track_counter
    counter = 0
    track_counter = 0
    search_query = search_entry.get()
    global result
    result = ur.search_artist(search_query)
    try:
        artist_name_label_entry['text'] = result[0].name
        follower_label_entry['text'] = result[0].follower
        genre_label_entry ['text'] = result[0].genre
        pop_label_entry['text'] = result[0].popularity
        image = ImageTk.PhotoImage(result[0].image)
        profile_pic_label.configure(image=image)
        profile_pic_label.image = image

        track_name_entry['text'] = (result[0]).tracks[0].name
        track_pop_entry['text'] = (result[0]).tracks[0].popularity

        top_track_label_entry['text'] =(result[0]).tracks[0].name
    except:
            messagebox.showinfo("Error","No Result Found")


# event command for getting the next artist
def display_result_down():
    global track_counter
    track_counter = 0
    global counter
    counter = counter+1
    if counter >= len(result):
        counter = counter%len(result)
    artist_name_label_entry['text'] = result[counter].name
    follower_label_entry['text'] = result[counter].follower
    genre_label_entry['text'] = result[counter].genre
    pop_label_entry['text'] = result[counter].popularity
    image = ImageTk.PhotoImage(result[counter].image)
    profile_pic_label.configure(image=image)
    profile_pic_label.image = image
    top_track_label_entry['text'] = (result[counter]).tracks[0].name
    track_name_entry['text'] = (result[counter].tracks)[0].name
    track_pop_entry['text'] = (result[counter].tracks)[0].popularity

# event command for getting the previous artist
def display_result_up():
    global track_counter
    track_counter = 0
    global counter
    counter = counter-1
    if counter < 0:
        counter = counter+len(result)
    artist_name_label_entry['text'] = result[counter].name
    follower_label_entry['text'] = result[counter].follower
    genre_label_entry['text'] = result[counter].genre
    pop_label_entry['text'] = result[counter].popularity
    image = ImageTk.PhotoImage(result[counter].image)
    profile_pic_label.configure(image=image)
    profile_pic_label.image = image
    top_track_label_entry['text'] = (result[counter]).tracks[0].name
    track_name_entry['text'] = (result[counter].tracks)[0].name
    track_pop_entry['text'] = (result[counter].tracks)[0].popularity


# event for getting the previous track
def display_track_result_up():
    global counter
    global result
    global track_counter
    track_counter = track_counter - 1
    if track_counter < 0:
        track_counter = track_counter + len(result[counter].tracks)
    track_name_entry['text'] = (result[counter].tracks)[track_counter].name
    track_pop_entry['text'] = (result[counter].tracks)[track_counter].popularity

# event for getting the next track
def display_track_result_down():
    global counter
    global track_counter
    track_counter = track_counter +1
    if track_counter >= len(result[counter].tracks):
        track_counter = track_counter % len(result[counter].tracks)
    track_name_entry['text'] = (result[counter].tracks)[track_counter].name
    track_pop_entry['text'] = (result[counter].tracks)[track_counter].popularity

# play audio from the track preview url
def play_audio():
    try:
        playsound(((result[counter]).tracks)[track_counter].preview_url,False)

    except:
        messagebox.showinfo("Error", "No Preview For This Track")


window.title('Spotify preview APP')
window.resizable(False,False)
window.mainloop()



