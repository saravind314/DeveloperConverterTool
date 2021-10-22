from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from bin.utils.logging.logger_handler import logger

root = Tk()
root.title('Developer Converter Tools')
root.minsize(670, 670)
# Removes the maximize button
root.resizable(0,0)



def browse_files():

    file_path = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    file_name = file_path.split("/")[-1]

    file_input_canvas.create_text(250, 25, font=('Helvetica', 9, 'bold'),
                                  text="File Selected: " + file_name, width=500)


def convert_click(root, action, input_text):
    if action == "copy":
        text = input_text.get("1.0",'end-1c')
        root.clipboard_clear()
        root.clipboard_append(text)

    elif action == "choose_file":
        browse_files()



convert_from = StringVar()
convert_from.set("Convert From")
convert_to = StringVar()
convert_to.set("Convert To")
options = ["base64_decode", "base64_encode"] 

title_label = Label(root, text="Developer Converter Tools", font=("Helvetica", 25)).place(x=165,y=10)
option1_label= Label(root, text="Option 1: Copy Paste your input here", font=("Helvetica", 10, 'bold')).place(x=90,y=90)
option2_label= Label(root, text="Option 2: Upload your file", font=("Helvetica", 10, 'bold')).place(x=90,y=370)

input_text = scrolledtext.ScrolledText(root)
input_text.place(x=90, y=110, width=490,  height=210)
copy_to_clipboard_button = Button(root, text="Copy to Clipboard",font=("Helvetica", 9, 'bold'), command=lambda: convert_click(root=root, action="copy", input_text=input_text), bg="#0050EF", fg="white" ).place(x=470,y =330)

file_input_canvas = Canvas(root, height=50, width = 490, bg="#BAC8D3")
file_input_canvas.place(x=90,y=390)

choose_file_button = Button(root, text="Choose File",font=("Helvetica", 9, 'bold'), command=lambda: convert_click(root=root, action="choose_file", input_text=input_text)).place(x=100, y = 400, width=100, height=30)

convert_from_dropdown = OptionMenu(root, convert_from,  *options,).place(x=90,y=510, width=220, height=40)
# convert_from_dropdown(bg="#D5E8D4")
convert_to_dropdown = OptionMenu(root,convert_to,  *options).place(x=360, y=510, width=220, height=40)
# convert_to_dropdown.config(bg="#D5E8D4")

convert_download_button = Button(root, text="Convert and Download",font=("Helvetica", 10, 'bold'), command=lambda: convert_click(action="convert_download"), bg="#DAE8FC").place(x=360, y=570, width=220, height=40)
convert_button = Button(root, text="Convert",font=("Helvetica", 9, 'bold'), command=lambda: convert_click("convert"), bg="#DAE8FC").place(x=90, y = 570, width=220, height=40)

def run():
    try:
        logger.info("Inside execution of main screen")
        root.mainloop()
    except Exception as e:
        print(str(e))