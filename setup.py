import cx_Freeze
executables =[
    cx_Freeze.Executable(script="spaceMaker.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "Space Maker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bg.jpg",
                            "space.png",
                            "SpaceAudio.mp3"
                            ]
        }
    }, executables = executables
)