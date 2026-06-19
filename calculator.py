import tkinter as tk

BG_COLOR = "#1f2937"
CARD_COLOR = "#111827"
TEXT_COLOR = "#e5e7eb"
ACCENT = "#60a5fa"
SUCCESS = "#34d399"
WARNING = "#fbbf24"
ERROR = "#f87171"

FONT_TEXT = ("Helvetica", 11)
FONT_BUTTON = ("Helvetica", 11, "bold")


def wechsel_auswahl(*args):
    blutdruck_frame.pack_forget()
    mad_frame.pack_forget()
    dipping_frame.pack_forget()

    if auswahl.get() == "Blutdruck berechnen":
        blutdruck_frame.pack(fill="both", expand=True, padx=20, pady=10)
        sys_entry.focus_set()

    elif auswahl.get() == "MAD berechnen":
        mad_frame.pack(fill="both", expand=True, padx=20, pady=10)
        mad_sys_entry.focus_set()

    elif auswahl.get() == "Dipping-Wert":
        dipping_frame.pack(fill="both", expand=True, padx=20, pady=10)
        tag_entry.focus_set()


def berechne_blutdruck():
    try:
        sys = float(sys_entry.get())
        dia = float(dia_entry.get())

        if sys < 120 and dia < 80:
            text = "Normaler Blutdruck"
            color = SUCCESS
        elif sys < 140 or dia < 90:
            text = "Erhöhter Blutdruck"
            color = WARNING
        else:
            text = "Bluthochdruck"
            color = ERROR

        blutdruck_ergebnis.config(text=text, fg=color)
    except:
        blutdruck_ergebnis.config(text="Bitte gültige Zahlen eingeben", fg=ERROR)


def berechne_mad():
    try:
        sys = float(mad_sys_entry.get())
        dia = float(mad_dia_entry.get())

        mad = dia + (sys - dia) / 3

        mad_ergebnis.config(
            text=f"MAD: {mad:.1f} mmHg",
            fg=SUCCESS
        )
    except:
        mad_ergebnis.config(text="Bitte gültige Zahlen eingeben", fg=ERROR)


def berechne_dipping():
    try:
        tag = float(tag_entry.get())
        nacht = float(nacht_entry.get())

        if tag <= 0:
            raise ValueError

        dipping = ((tag - nacht) / tag) * 100

        if dipping >= 10:
            status = "Normaler Dipping-Wert"
            color = SUCCESS
        else:
            status = "Non-Dipper"
            color = WARNING

        dipping_ergebnis.config(
            text=f"Dipping: {dipping:.1f}%\n{status}",
            fg=color
        )
    except:
        dipping_ergebnis.config(text="Bitte gültige Zahlen eingeben", fg=ERROR)


def create_card_frame(parent):
    frame = tk.Frame(parent, bg=CARD_COLOR, bd=0, relief="flat")
    frame.pack_propagate(False)
    frame.configure(height=250)
    return frame


root = tk.Tk()
root.title("Blutdruck, MAD und Dipping-Wert")
root.geometry("440x380")
root.configure(bg=BG_COLOR)

auswahl = tk.StringVar(value="Blutdruck berechnen")
auswahl.trace_add("write", wechsel_auswahl)

dropdown = tk.OptionMenu(
    root,
    auswahl,
    "Blutdruck berechnen",
    "MAD berechnen",
    "Dipping-Wert"
)
dropdown.config(bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT, highlightthickness=0)
dropdown["menu"].config(bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT)
dropdown.pack(pady=15)



blutdruck_frame = create_card_frame(root)

tk.Label(blutdruck_frame, text="Systolisch:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
sys_entry = tk.Entry(blutdruck_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
sys_entry.pack(ipady=6, ipadx=5)

tk.Label(blutdruck_frame, text="Diastolisch:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
dia_entry = tk.Entry(blutdruck_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
dia_entry.pack(ipady=6, ipadx=5)

tk.Button(blutdruck_frame, text="Berechnen", command=berechne_blutdruck,
          bg=ACCENT, fg="#0b1220", font=FONT_BUTTON, bd=0).pack(pady=12, ipadx=10, ipady=6)

blutdruck_ergebnis = tk.Label(blutdruck_frame, text="", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT)
blutdruck_ergebnis.pack()



mad_frame = create_card_frame(root)

tk.Label(mad_frame, text="Systolisch:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
mad_sys_entry = tk.Entry(mad_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
mad_sys_entry.pack(ipady=6, ipadx=5)

tk.Label(mad_frame, text="Diastolisch:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
mad_dia_entry = tk.Entry(mad_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
mad_dia_entry.pack(ipady=6, ipadx=5)

tk.Button(mad_frame, text="MAD berechnen", command=berechne_mad,
          bg=ACCENT, fg="#0b1220", font=FONT_BUTTON, bd=0).pack(pady=12, ipadx=10, ipady=6)

mad_ergebnis = tk.Label(mad_frame, text="", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT)
mad_ergebnis.pack()



dipping_frame = create_card_frame(root)

tk.Label(dipping_frame, text="Tag-Blutdruck:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
tag_entry = tk.Entry(dipping_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
tag_entry.pack(ipady=6, ipadx=5)

tk.Label(dipping_frame, text="Nacht-Blutdruck:", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT).pack(pady=5)
nacht_entry = tk.Entry(dipping_frame, font=FONT_TEXT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
nacht_entry.pack(ipady=6, ipadx=5)

tk.Button(dipping_frame, text="Dipping berechnen", command=berechne_dipping,
          bg=ACCENT, fg="#0b1220", font=FONT_BUTTON, bd=0).pack(pady=12, ipadx=10, ipady=6)

dipping_ergebnis = tk.Label(dipping_frame, text="", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_TEXT)
dipping_ergebnis.pack()


blutdruck_frame.pack(fill="both", expand=True, padx=20, pady=10)
sys_entry.focus_set()

root.mainloop()



