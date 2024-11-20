#!/usr/bin/env python3
import pyperclip
import easygui
import config
import os
import subprocess

def get_clipboard_text():
    """Get clipboard text using multiple methods"""
    try:
        text = pyperclip.paste()
        if text and text.strip():
            return text.strip()
            
        try:
            result = subprocess.run(['xclip', '-o', '-selection', 'clipboard'], 
                                 capture_output=True, text=True)
            if result.stdout.strip():
                return result.stdout.strip()
        except:
            pass
            
        try:
            result = subprocess.run(['xclip', '-o', '-selection', 'primary'], 
                                 capture_output=True, text=True)
            if result.stdout.strip():
                return result.stdout.strip()
        except:
            pass
            
        return None
    except:
        return None

def ensure_note_dir():
    """Ensure the notes directory exists"""
    note_dir = os.path.dirname(config.text_path)
    if note_dir and not os.path.exists(note_dir):
        os.makedirs(note_dir, exist_ok=True)

def txtPaste(text, outfile):
    """Save text to file"""
    try:
        ensure_note_dir()
        with open(outfile, "a", encoding='utf-8') as fhandle:
            fhandle.write(f'{text}\n')
        return True
    except Exception as e:
        easygui.msgbox(f"Error saving note: {str(e)}", "Error", "OK")
        return False

def main():
    try:
        clipboard_text = get_clipboard_text()
        if not clipboard_text:
            return
            
        txtPaste(clipboard_text, config.text_path)
            
    except Exception as e:
        easygui.msgbox(f"Error: {str(e)}", "Error", "OK")

if __name__ == '__main__':
    main()
