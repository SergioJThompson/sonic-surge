from tkinter import *
from tkinter import filedialog
from os.path import expanduser

from simpleaudio import WaveObject

from PlayButton import PlayButton
from pydub import AudioSegment


def create_root_window():
    root = Tk()
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))
    root.title("Sonic Surge")

    play_btn = PlayButton(root, text="Play mp3")  # TODO: say "No file loaded" if button is clicked without file loaded
    choose_btn = Button(root, text="Choose mp3", command=lambda: change_audio(play_btn))
    play_btn.pack(side=LEFT, anchor=SW, padx=7, pady=8)
    choose_btn.pack(side=RIGHT, anchor=SE, padx=9, pady=8)


def get_file_path_from_user():
    return filedialog.askopenfilename(initialdir=expanduser("~/Music/"), filetypes=[("MP3 files", "*.mp3")])


def change_audio(play_btn):
    play_btn.stop()
    file_path = get_file_path_from_user()
    if file_path != '':
        play_btn.set_sound(get_wave_object(file_path))


def get_wave_object(audio_file_path):
    seg = AudioSegment.from_file(audio_file_path)
    return WaveObject(seg.raw_data, seg.channels, seg.sample_width, seg.frame_rate)


def main():
    create_root_window()
    mainloop()


main()

# TODO: backwards audio button!
