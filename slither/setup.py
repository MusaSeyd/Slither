from http.server import executable
import cx_Freeze

executables = [cx_Freeze.Executable("slither.py")]

cx_Freeze.setup(
	name = "Slither",
	options = {"build_exe":{"packages":["pygame"], "include_files":["apple.png", "snakehead.png"]}},

	description = "Slither Game",
	executables = executables
)