#!/usr/bin/env python3

import subprocess
import sys
import os
import pathlib
from datetime import datetime

APP_PATH = str(pathlib.Path(__file__).parent.absolute())

def print_banner():
    banner = """
\033[96m██╗  ██╗██╗██████╗  █████╗ ███████╗███████╗ ██████╗
██║ ██╔╝██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╔╝ ██║██████╔╝███████║███████╗█████╗  ██║     
██╔═██╗ ██║██╔══██╗██╔══██║╚════██║██╔══╝  ██║     
██║  ██╗██║██║  ██║██║  ██║███████║███████╗╚██████╗
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝\033[0m
           \033[93mFastNote Installation Wizard v1.0\033[0m
                      \033[96m㉿ NET ㉿\033[0m
\033[90m═══════════════════════════════════════════════════════\033[0m"""
    print(banner)
    print(f"\033[94m[*] Started installation at {datetime.now().strftime('%H:%M:%S')}\033[0m")

def install_deps():
    """Install system and Python dependencies"""
    print("\033[94m[*] Installing system dependencies...\033[0m")
    
    try:
        subprocess.run(['apt-get', 'update'], check=True)
        subprocess.run(['apt-get', 'install', '-y', 'python3-pip', 'python3-venv', 
                      'xclip', 'xfce4-terminal'], check=True)
        
        venv_path = os.path.join(APP_PATH, 'venv')
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
        
        pip_path = os.path.join(venv_path, 'bin', 'pip')
        subprocess.run([pip_path, 'install', '-r', os.path.join(APP_PATH, 'requirements.txt')], check=True)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"\033[91m[-] Error installing packages: {str(e)}\033[0m")
        return False

def create_launcher_script():
    """Create a launcher script that uses the virtual environment"""
    launcher_path = os.path.join(APP_PATH, 'run_fastnote.sh')
    venv_python = os.path.join(APP_PATH, 'venv', 'bin', 'python3')
    
    with open(launcher_path, 'w') as f:
        f.write(f"""#!/bin/bash
{venv_python} "$@"
""")
    os.chmod(launcher_path, 0o755)
    return launcher_path

def setup_xfce_shortcuts(launcher):
    """Set up keyboard shortcuts using xfconf-query"""
    try:
        user = os.getenv('SUDO_USER') or os.getenv('USER')
        if not user:
            raise Exception("Could not determine current user")

        commands = [
            ('<Primary><Shift>s', f'{launcher} {APP_PATH}/fastDisplay.py'),
            ('<Primary><Shift>c', f'{launcher} {APP_PATH}/fastnote.py'),
            ('<Super>n', f'{launcher} {APP_PATH}/fastnoteclear.py')
        ]

        script_content = '#!/bin/bash\n\n'
        script_content += 'xfconf-query -c xfce4-keyboard-shortcuts -p "/commands/custom" -r -R\n'
        
        for key, cmd in commands:
            script_content += f'xfconf-query -c xfce4-keyboard-shortcuts -n -p "/commands/custom/{key}" -t string -s "{cmd}"\n'

        script_path = '/tmp/fastnote_shortcuts.sh'
        with open(script_path, 'w') as f:
            f.write(script_content)
        os.chmod(script_path, 0o755)

        subprocess.run(['su', '-c', script_path, user], check=True)
        os.remove(script_path)

        print("\033[92m[+] Keyboard shortcuts configured\033[0m")
        return True

    except Exception as e:
        print(f"\033[91m[-] Error setting up shortcuts: {str(e)}\033[0m")
        print("\033[93m[!] Set up shortcuts manually in Settings > Keyboard > Shortcuts\033[0m")
        return False

def main():
    try:
        print_banner()
        
        if os.geteuid() != 0:
            print("\033[91m[!] This script needs root privileges to install packages.\033[0m")
            print("\033[93m[*] Rerunning with sudo...\033[0m")
            os.execvp('sudo', ['sudo', 'python3'] + sys.argv)
            return
        
        if not install_deps():
            sys.exit(1)
            
        print("\033[92m[+] Dependencies installed successfully\033[0m")
        
        launcher = create_launcher_script()
        
        setup_xfce_shortcuts(launcher)
        
        print("\n\033[92m[+] Installation completed!\033[0m")
        print("\n\033[93mTo use FastNote:\033[0m")
        print("  Ctrl+Shift+S - Display notes")
        print("  Ctrl+Shift+C - Save clipboard")
        print("  Super+N     - Clear notes")
        
        print("\n\033[93m[!] Log out and back in for shortcuts to take effect\033[0m")
        
    except KeyboardInterrupt:
        print("\n\033[91m[-] Installation cancelled by user\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[91m[-] Error: {str(e)}\033[0m")
        sys.exit(1)

if __name__ == '__main__':
    main()
