import datetime
import json
import Pmw
import pygame
from tkinter import *
import webbrowser

# init pygame for playing sound and datetime for live date
pygame.mixer.init()
today = datetime.datetime.now()


# all morse characters
def morse_dict():
    morse_file = open("morse_characters.json", encoding='utf-8')
    data = json.load(morse_file)
    return data["morse_characters"]


# Read data from lang.txt and return the value
def language():
    with open("lang.txt") as i_file:
        lang = i_file.read()
        return lang


# Write new data in lang.txt
def modify_language(lang):
    with open("lang.txt", "w") as i_file:
        i_file.write(lang)


# Set screen
screen = Tk()
screen.config(padx=100, pady=50, bg='#323232')
screen.title('Morse Converter')


# ALL FUNCTIONS

# run the converter and insert the input value into converter
def convert_command():
    input_value = morse_converter_entry.get("1.0", "end-1c").lower()
    out = converter(input_value)
    morse_output.delete('1.0', END)
    morse_output.insert(END, f'{out}')


# convert the given character to morse code and return the value
def converter(x):
    word = x
    morse_word = []
    morse_chars = morse_dict()
    for i in word:
        if i in morse_chars:
            i = morse_chars[i]
        elif i == ' ':
            i = '/    '
        elif i not in morse_chars:
            i = ''
        morse_word.append(i)
    return "".join(morse_word)


# English text
def english():
    morse_converter_title.config(text="Morse code translator")
    morse_converter_input_label.config(text='Type your text here:')
    convert_button.config(text='Convert')
    play_button.config(text='Play')
    morse_converter_output_label.config(
        text="Morse code\n(The letters of a word are separated by spaces, and words are separated by '/')")
    menubar.entryconfig(1, label='File')
    char_speed.config(text='Character speed')
    word_speed.config(text='Farnsworth speed')
    file.entryconfig(0, label='Language')
    submenu.entryconfig(0, label='English')
    submenu.entryconfig(2, label='Hungarian')
    file.entryconfig(2, label='Exit')
    menubar.entryconfig(2, label='Help')
    help_.entryconfig(0, label="User's Guide")
    help_.entryconfig(2, label='About Morse Converter')
    lang = "english"
    modify_language(lang)


# Hungarian text
def magyar():
    morse_converter_title.config(text="Morze átalakító program")
    morse_converter_input_label.config(text='Gépeld be az átalakítani kívánt szöveget:')
    convert_button.config(text='Átalakítás')
    play_button.config(text='Lejátszás')
    morse_converter_output_label.config(
        text="Morze kód:\n(a betűk szóközzel, míg a szavak '/' jellel vannak elválasztva)")
    menubar.entryconfig(1, label='Fájl')
    file.entryconfig(0, label='Nyelv')
    char_speed.config(text='Karakter gyorsaság')
    word_speed.config(text='Szavak gyorsasága')
    submenu.entryconfig(0, label='Angol')
    submenu.entryconfig(2, label='Magyar')
    file.entryconfig(2, label='Kilépés')
    menubar.entryconfig(2, label='Súgó')
    help_.entryconfig(0, label="Használati útmutató")
    help_.entryconfig(2, label='Morse Converter névjegye')
    lang = "hungarian"
    modify_language(lang)


# Set language based on the lang.txt file
def set_language():
    if language() == "hungarian":
        magyar()
    elif language() == "english":
        english()


# play long morse sound
def long():
    pygame.mixer.music.load("long.mp3")
    pygame.mixer.music.play(loops=0)


# play short morse sound
def short():
    pygame.mixer.music.load("short.mp3")
    pygame.mixer.music.play(loops=0)


# play break sound
def silent():
    pygame.mixer.music.load("silent.mp3")
    pygame.mixer.music.play(loops=0)


# read characters and character speed
# play the corresponding sounds
def play():
    input_value = morse_converter_entry.get("1.0", "end-1c").lower()
    out = converter(input_value)
    specified_char_speed = int(char_speed_slider_variable.get())
    specified_word_speed = int(word_speed_slider_variable.get())
    for i in out:
        if i == '⬤':
            short()
            screen.after(specified_char_speed)
        elif i == '▬':
            long()
            screen.after(specified_char_speed)
        elif i == '/':
            silent()
            screen.after(specified_word_speed)
        elif i == ' ':
            screen.after(int(specified_word_speed / 2))


# set description menu
def description():
    Pmw.aboutversion('1.0')
    Pmw.aboutcopyright(f'Copyright © Sándor Szilveszter 2021 - {today.year}\nMinden jog fenntartva')
    Pmw.aboutcontact(
        'További információkért az alábbi e-mail címen\n' +
        'keresztül érdeklődhetsz:\n' +
        'email: s.szilveszter1994@gmail.com'
    )
    return Pmw.AboutDialog(screen, applicationname='Morse Converter')


# Open user's guide link
def guide():
    webbrowser.open_new(r"https://drive.google.com/file/d/190xdWo-fh5MQSK04rYWZcflqRvd10M-b/view?usp=sharing")


# set UI
# set title
morse_converter_title = Label(text="Morze átalakító program", font=("Arvo", 36, "bold"), highlightthickness=0,
                              fg='#F76E11')
morse_converter_title.config(bg='#323232')
morse_converter_title.grid(column=0, row=1, pady=20, columnspan=2)

# set input area
morse_converter_input_label = Label(text="Gépeld be az átalakítani kívánt szöveget:", font=("Montserrat", 12, "bold"),
                                    highlightthickness=0, bg='#323232', fg='#F76E11')
morse_converter_input_label.grid(column=0, row=2, pady=5, columnspan=2)

morse_converter_entry = Text(width=50, height=5, font=("Montserrat", 12), highlightthickness=0, bg='#2C3333',
                             fg='#E5E3C9')
morse_converter_entry.focus()
morse_converter_entry.grid(column=0, row=3, columnspan=2)

# set convert button
convert_button = Button(text="Átalakítás", width=10, height=1, font=("Montserrat", 15, "bold"), command=convert_command,
                        bg='#FFBC80', fg='#F76E11', highlightthickness=0)
convert_button.grid(column=0, row=4, pady=10, columnspan=2)

# set output area
morse_converter_output_label = Label(text="Morze kód:\n(a betűk szóközzel, míg a szavak '/' jellel vannak elválasztva)",
                                     font=("Montserrat", 12, "bold"), highlightthickness=0, bg='#323232',
                                     fg='#F76E11')
morse_converter_output_label.grid(column=0, row=5, pady=10, columnspan=2)

morse_output = Text(width=75, height=7, font=("Impact", 8), highlightthickness=0, bg='#2C3333', fg='#E5E3C9')
morse_output.focus()
morse_output.grid(column=0, row=6, columnspan=2)

# set play button
play_button = Button(text="Lejátszás", width=10, height=1, font=("Montserrat", 15, "bold"), command=play,
                     bg='#FFBC80', fg='#F76E11', highlightthickness=0)
play_button.grid(column=0, row=7, pady=10, columnspan=2)

# set char speed slider
char_speed = Label(text="Karakter gyorsaság",
                   font=("Montserrat", 12, "bold"), highlightthickness=0, bg='#323232',
                   fg='#F76E11')
char_speed.grid(column=0, row=8)

char_speed_slider_variable = DoubleVar()
char_speed_slider_variable.set(200)
char_speed_slider_bar = Scale(screen, variable=char_speed_slider_variable, from_=50, to=1000, orient=HORIZONTAL)
char_speed_slider_bar.grid(column=0, row=9)

# set word speed slider
word_speed = Label(text="Szavak gyorsasága",
                   font=("Montserrat", 12, "bold"), highlightthickness=0, bg='#323232',
                   fg='#F76E11')
word_speed.grid(column=1, row=8)
word_speed_slider_variable = DoubleVar()
word_speed_slider_variable.set(200)
word_speed_slider_bar = Scale(screen, variable=word_speed_slider_variable, from_=50, to=1000, orient=HORIZONTAL)
word_speed_slider_bar.grid(column=1, row=9)

# Creating Menubar
menubar = Menu(screen)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Fájl', menu=file)
submenu = Menu(file, tearoff=0)
file.add_cascade(label='Nyelv', menu=submenu)
submenu.add_command(label="Angol", command=english)
submenu.add_command(label="Magyar", command=magyar)
file.add_command(label='Kilépés', command=screen.destroy)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Súgó', menu=help_)
help_.add_command(label='Használati útmutató', command=guide)
help_.add_command(label='Morse Converter névjegye', command=description)

# display Menu
screen.config(menu=menubar)

# apply the stored language
set_language()

# infinite loop
screen.mainloop()
