from tkinter import *

russel = Tk()
russel.title("The Rising Of Mother")
russel.geometry("1366x768")

screen_w = 1254
screen_h = 768

canvas = Canvas(russel, width=screen_w, height=screen_h)
canvas.pack()

# ---------------- GAME OBJECTS ----------------
ground = canvas.create_rectangle(0, 420, screen_w, screen_h, fill="green")

img = PhotoImage(file="block.png")
player = canvas.create_image(100, 400, image=img)

canvas.itemconfigure(player, state="hidden")
canvas.itemconfigure(ground, state="hidden")

# ---------------- VARIABLES ----------------
x_speed = 0
y_speed = 0
gravity = 1
jump_power = -15
on_ground = False

# ---------------- CONTROLS ----------------
def key_press(event):
    global x_speed, y_speed

    key = event.keysym.lower()

    if key == "a":
        x_speed = -5
    elif key == "d":
        x_speed = 5
    elif key == "w" and on_ground:
        y_speed = jump_power


def key_release(event):
    global x_speed

    if event.keysym.lower() in ["a", "d"]:
        x_speed = 0


# ---------------- MENU ----------------
def show_menu():
    global play_btn, settings_btn, exit_btn
    global menu_bg, menu_bg_id

    # BACKGROUND IMAGE
    menu_bg = PhotoImage(file="MainMenubg.png")
    menu_bg_id = canvas.create_image(0, 0, image=menu_bg, anchor="nw")

    # PLAY BUTTON
    play_btn = Button(
        russel,
        text="PLAY",
        font=("Times New Roman", 20, "bold"),
        fg="black",
        bg="lightgreen",
        activebackground="green",
        activeforeground="black",
        width=15,
        command=start_game
    )
    play_btn.place(x=560, y=250)

    # SETTINGS BUTTON
    settings_btn = Button(
        russel,
        text="SETTINGS",
        font=("Times New Roman", 20, "bold"),
        fg="black",
        bg="lightgreen",
        activebackground="green",
        activeforeground="black",
        width=15,
        command=open_settings
    )
    settings_btn.place(x=560, y=330)

    # EXIT BUTTON
    exit_btn = Button(
        russel,
        text="EXIT",
        font=("Times New Roman", 20, "bold"),
        fg="black",
        bg="lightgreen",
        activebackground="green",
        activeforeground="black",
        width=15,
        command=russel.quit
    )
    exit_btn.place(x=560, y=410)


# ---------------- START GAME ----------------
def start_game():
    play_btn.destroy()
    settings_btn.destroy()
    exit_btn.destroy()

    canvas.delete(menu_bg_id)

    canvas.itemconfigure(player, state="normal")
    canvas.itemconfigure(ground, state="normal")

    update()


# ---------------- SETTINGS ----------------
def open_settings():
    win = Toplevel(russel)
    win.title("Settings")
    win.geometry("300x200")

    Label(win, text="Settings", font=("Arial", 16)).pack(pady=10)
    Label(win, text="(Add options here)").pack()


# ---------------- GAME LOOP ----------------
def update():
    global y_speed, on_ground

    canvas.move(player, x_speed, y_speed)
    y_speed += gravity

    x, y = canvas.coords(player)

    if y >= 400:
        canvas.coords(player, x, 400)
        y_speed = 0
        on_ground = True
    else:
        on_ground = False

    russel.after(20, update)


# ---------------- INPUT ----------------
russel.bind("<KeyPress>", key_press)
russel.bind("<KeyRelease>", key_release)

# ---------------- START ----------------
show_menu()
russel.mainloop()