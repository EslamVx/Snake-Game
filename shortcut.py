import os
import sys
import win32com.client


def create_shortcut(name, target, arguments, icon=None):
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
    shortcut_path = os.path.join(desktop, f"{name}.lnk")

    if not os.path.exists(desktop):
        os.makedirs(desktop)

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    if icon:
        shortcut.IconLocation = icon
    shortcut.save()
    print(f"Shortcut created at: {shortcut_path}")


if __name__ == "__main__":
    target = sys.executable
    arguments = os.path.abspath("main.py")
    icon_path = os.path.abspath("icon/snake_icon.png")
    create_shortcut("EB Snake", target, arguments, icon=icon_path)
