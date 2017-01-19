import sys
from cx_Freeze import setup, Executable

include_files = [
    ("icon.ico", "icon.ico"),
    ("config.ini", "config.ini"),
    ("gui/")
]
includes = []
excludes = ["urllib"]
packages = ["os", "sys", "tkinter", "tkRAD"]

build_exe_options = {
    "build_exe": "../build",
    "packages": packages,
    "includes": includes,
    "excludes": excludes,
    "include_files": include_files,
}

base = None
# Check, if you have win32
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    script="main.py",
    icon="icon.ico",
    base=base,
    path="source"
)

setup(name="Obj Viewer",
      version="0.1",
      description="Obj Viewer",
      author="Daniel Derevjanik",
      url="http://www.st.fmph.uniba.sk/~derevjanik7/",
      package_dir={'': 'source'},
      options={"build_exe": build_exe_options},
      executables=[exe])
