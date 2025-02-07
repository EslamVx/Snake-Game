from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Created by EslamVx && Bassel.",
    options={
        "build_exe": {
            "packages": ["playsound"],
            "include_files": [
                "Sounds/StartGame.mp3",
                "Sounds/GameOver.mp3",
            ],
        }
    },
    executables=[Executable("main.py", icon="icon/snake_icon.ico")],
)
