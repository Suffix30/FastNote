#!/usr/bin/env python3
import config
import easygui
import os

def clearTxt():
    try:
        if os.path.exists(config.text_path):
            open(config.text_path, 'w').close()
        else:
            easygui.msgbox("No notes file found.", "Warning", "OK")
    except Exception as e:
        easygui.msgbox(f"Error clearing notes: {str(e)}", "Error", "OK")

if __name__ == '__main__':
    clearTxt()
