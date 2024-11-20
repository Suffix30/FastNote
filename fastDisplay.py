#!/usr/bin/env python3
import config
import easygui
import os

def fastDisplay():
    try:
        if not os.path.exists(config.text_path):
            easygui.msgbox("No notes found.", "Fast Note 1.0", "OK")
            return

        with open(config.text_path, "r") as data:
            message = data.read()
            
        if not message.strip():
            message = "No notes yet."
            
        title = "Fast Note 1.0"
        ok_btn_txt = "Continue"
        easygui.msgbox(message, title, ok_btn_txt)
    except Exception as e:
        easygui.msgbox(f"Error: {str(e)}", "Error", "OK")

if __name__ == '__main__':
    fastDisplay()