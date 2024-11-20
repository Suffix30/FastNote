# FastNote

A lightweight clipboard note-taking utility for Linux with keyboard shortcuts and a sleek KIRASec-themed interface.

## 🚀 Features

- **Silent Operation**: Copy and clear notes without popup notifications
- **Quick Access**: Keyboard shortcuts for all operations
- **Clipboard Integration**: Instantly save clipboard content
- **KIRASec Theme**: Stylish cyan and black interface
- **Multi-Desktop Support**: Works with XFCE and other Linux desktop environments
- **Error Handling**: Clear error messages when something goes wrong

## 🛠️ Installation

1. Install required system packages:
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-easygui xclip python3-pyperclip python3-xlib xfce4-terminal
   ```

2. Run the setup script:
   ```bash
   sudo python3 set-up.py
   ```

## ⌨️ Usage

### Keyboard Shortcuts

- `Ctrl + Shift + S` - Display your notes
- `Ctrl + Shift + C` - Save clipboard content to notes
- `Super + N` - Clear all notes

### Command Line

```bash
python3 fastDisplay.py    # View notes
python3 fastnote.py       # Save clipboard
python3 fastnoteclear.py  # Clear notes
```

### Applications Menu

Find FastNote in your applications menu with three options:
- FastNote Display
- FastNote Save
- FastNote Clear

## 📝 Notes Location

By default, notes are stored in:
```
~/fastnote.txt
```

To change the location, set the `FASTNOTE_PATH` environment variable:
```bash
export FASTNOTE_PATH="/your/preferred/path/notes.txt"
```

## 🔧 Troubleshooting

### Keyboard Shortcuts Not Working?

1. Open Settings Manager
2. Go to Keyboard > Application Shortcuts
3. Add these commands manually:
   - `python3 /path/to/fastDisplay.py` (Ctrl+Shift+S)
   - `python3 /path/to/fastnote.py` (Ctrl+Shift+C)
   - `python3 /path/to/fastnoteclear.py` (Super+N)

### Clipboard Issues?

1. Ensure xclip is installed:
   ```bash
   sudo apt-get install xclip
   ```

2. Check if clipboard has content:
   ```bash
   xclip -o -selection clipboard
   ```

### Permission Issues?

1. Check notes file permissions:
   ```bash
   ls -l ~/fastnote.txt
   ```

2. Fix ownership if needed:
   ```bash
   sudo chown $USER:$USER ~/fastnote.txt
   ```

## 🔄 Updates

To update FastNote:

1. Pull the latest changes
2. Run setup again:
   ```bash
   sudo python3 set-up.py
   ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔐 Security

FastNote stores notes in plain text. Do not use it for sensitive information.
-NET