from tkinter import *
import tkinter.scrolledtext as scrolledtext

root = Tk()
root.title('Developer Converter Tools')
root.minsize(670, 670)
root.maxsize(670, 670)

def convert_click(action):
    output = Label(root, text=entry.get())
    output.pack()

convert_from = StringVar()
convert_from.set("Convert From")
convert_to = StringVar()
convert_to.set("Convert To")
options = ["base64_decode", "base64_encode"] 

title_label = Label(root, text="Developer Converter Tools", font=("Helvetica", 25)).place(x=165,y=10)
option1_label= Label(root, text="Option 1: Copy Paste your input here", font=("Helvetica", 10, 'bold')).place(x=90,y=90)
option2_label= Label(root, text="Option 2: Upload your file", font=("Helvetica", 10, 'bold')).place(x=90,y=370)

entry = scrolledtext.ScrolledText(root).place(x=90, y=110, width=490,  height=210)
copy_to_clipboard_button = Button(root, text="Copy to Clipboard",font=("Helvetica", 9, 'bold'), command=lambda: convert_click(action="copy"), bg="#0050EF", fg="white" ).place(x=470,y =330)

file_input_canvas = Canvas(root, height=50, width = 490, bg="#BAC8D3").place(x=90,y=390)
choose_file_button = Button(root, text="Choose File",font=("Helvetica", 9, 'bold'), command=lambda: convert_click(action="choose_file")).place(x=100, y = 400, width=100, height=30)

convert_from_dropdown = OptionMenu(root, convert_from,  *options,).place(x=90,y=510, width=220, height=40)
# convert_from_dropdown(bg="#D5E8D4")
convert_to_dropdown = OptionMenu(root,convert_to,  *options).place(x=360, y=510, width=220, height=40)
# convert_to_dropdown.config(bg="#D5E8D4")

convert_download_button = Button(root, text="Convert and Download",font=("Helvetica", 10, 'bold'), command=lambda: convert_click(action="convert_download"), bg="#DAE8FC").place(x=360, y=570, width=220, height=40)
convert_button = Button(root, text="Convert",font=("Helvetica", 9, 'bold'), command=lambda: convert_click("convert"), bg="#DAE8FC").place(x=90, y = 570, width=220, height=40)

def run():
    try:
        root.mainloop()
    except Exception as e:
        print(str(e))