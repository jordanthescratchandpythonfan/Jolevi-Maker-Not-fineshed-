from cx_Freeze import setup, Executable

build_exe_options = {"build_exe": "/path/to/build/directory"}

setup(
    name="Jolevi Maker",
    version="1.0",
    description="Code in GUISCL",
    options={"build_exe": build_exe_options},
    executables=[Executable("jmaker.py")]
)

