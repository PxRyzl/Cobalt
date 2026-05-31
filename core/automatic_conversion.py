import os
import shutil
import subprocess
import pathlib
import difflib
import itertools
from pathlib import Path
from difflib import get_close_matches
from os import listdir

home = pathlib.Path.home()
cwd_dir = Path.cwd()

def AutomaticConversion(file_path_dir, theme_name, theme_com):

    cur_alias = {
        "Pointer": "Default",
        "Normal": "Default",
        "Precision": "Cross",
        "Diagonal1": "Dgn1",
        "Diagonal2": "Dgn2",
        "Handwriting": "Hand"
}

    cursor_name = ["Alternate", "Busy", "Cross", "Default", "Dgn1", "Dgn2", "Hand", "Help", "Horizontal", "Link", "Move", "Text", "Unavailable", "Vertical", "Work"]

    checkdir = Path(f"{home}/.local/share/cobalt/input")
    checkdir.mkdir(parents=True, exist_ok=True)

    prosdir = Path(f"{home}/.local/share/cobalt/input/process")
    prosdir.mkdir(parents=True, exist_ok=True)

    for filename in os.listdir(file_path_dir):
        cur_file = os.path.join(file_path_dir, filename)
        if os.path.isfile(cur_file):
            shutil.copy(str(cur_file), str(checkdir))

    files = itertools.chain(
        Path(checkdir).glob("*.cur"),
        Path(checkdir).glob("*.ani")
    )
    for file in files:
        match = matching(file.name, cursor_name)

        if match:
            suffix = file.suffix
            dest = checkdir / f"{match}{suffix}"

            if file != dest:
                file.rename(dest)

            subprocess.run(["win2xcur", str(dest), "-o", str(prosdir)])

    cursor_map = {
        "Alternate": ["bottom_left_corner", "bottom_right_corner", "bottom_side", "down-arrow", "left-arrow", "left_side", "right-arrow", "right_side", "top_left_corner", "top_right_corner", "top_side", "up_arrow"],
        "Busy": ["half-busy", "wait", "watch"],
        "Cross": ["cross", "crosshair"],
        "Default": ["arrow", "default", "left_ptr", "size-bdiag", "size-fdiag", "size-hor", "size-ver", "top_left_arrow"],
        "Dgn1": ["nw-resize", "nwse-resize", "se-resize", "size_fdiag"],
        "Dgn2": ["ne-resize", "nesw-resize", "sw-resize", "size_bdiag"],
        "Hand": ["draft", "pencil"],
        "Help": ["help", "left_ptr_help", "question_arrow", "whats_this"],
        "Horizontal": ["col-resize", "e-resize", "ew-resize", "h_double_arrow", "sb_h_double_arrow", "size_hor", "split_h", "w-resize"],
        "Link": ["grab", "hand", "hand1", "hand2", "openhand", "pointer", "pointing_hand"],
        "Move": ["all-scroll", "closedhand", "dnd-move", "dnd-none", "fleur", "grabbing", "move", "size_all"],
        "Text": ["ibeam", "text", "xterm"],
        "Unavailable": ["circle", "crossed_circle", "dnd_no_drop", "forbidden", "no_drop", "not_allowed"],
        "Vertical": ["n-resize", "ns-resize", "row-resize", "s-resize", "sb_v_double_arrow", "size_ver", "split_v", "v_double_arrow"],
        "Work": ["left_ptr_watch", "pirate", "progress"],
}
    output_dir = Path(f"{home}/.local/share/cobalt/test-cursors/cursors")
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in cursor_map:
        converted = prosdir / name

        if converted.exists() and name in cursor_map:
            if converted.exists():
                prim = output_dir / cursor_map[name][0]
                shutil.copy(str(converted),str(prim))

                for cursor_name in cursor_map[name][1:]:
                    dest = output_dir / cursor_name
                    os.symlink(prim.name, dest)

    cursor_dir = Path(f"{home}/.local/share/cobalt/test-cursors")

    shutil.move(str(cursor_dir), str(Path.home() / ".icons" / theme_name))

    index = Path(f"{home}/.icons/{theme_name}/index.theme")
    index.write_text(f"[Icon Theme]\nName={theme_name}\nComment={theme_com}")

    shutil.rmtree(str(checkdir))

def matching(filename,cursor_name):

    cur_alias = {
        "Pointer": "Default",
        "Normal": "Default",
        "Precision": "Cross",
        "Diagonal1": "Dgn1",
        "Diagonal2": "Dgn2",
}

    cursor_name = ["Alternate", "Busy", "Cross", "Default", "Dgn1", "Dgn2", "Hand", "Help", "Horizontal", "Link", "Move", "Text", "Unavailable", "Vertical", "Work"]

    name = Path(filename).stem.lower()

    for alias, label in cur_alias.items():
        if alias.lower() in name:
            return label

    if name in cur_alias:
        return cur_alias[name]

    match = get_close_matches(name, [c.lower() for c in cursor_name], n=1, cutoff=0.5)
    if match:
        return cursor_name[[c.lower() for c in cursor_name].index(match[0])]
    return match[0] if match else None
