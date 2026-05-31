import os
import shutil
import subprocess
import pathlib
from pathlib import Path

home = pathlib.Path.home()
cwd_dir = Path.cwd() # idk why I even manually put this here, since its not needed

def InfConversion(file_path, theme_name, theme_com):

    output_dir = Path(f"{home}/.local/share/cobalt/test-cursors/cursors")
    output_dir.mkdir(parents=True, exist_ok=True)

    cursor_dir = Path(f"{home}/.local/share/cobalt/test-cursors")

    subprocess.run(["iconv", "-f", "cp1252", "-t", "utf-8", str(file_path), "-o" , str(file_path)])
    subprocess.run(["win2xcurtheme", str(file_path), "-o" , str(output_dir)])

    shutil.move(str(cursor_dir), str(Path.home() / ".icons" / theme_name))

    index = Path(f"{home}/.icons/{theme_name}/index.theme")
    index.write_text(f"[Icon Theme]\nName={theme_name}\nComment={theme_com}")
