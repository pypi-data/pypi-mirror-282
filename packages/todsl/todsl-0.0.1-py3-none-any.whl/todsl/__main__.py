from . import parse_project
import sys
import os

def main():
	if not os.path.isdir(".git") or not os.path.isdir("versions") or not os.path.isdir("components"):
		print("ERROR: Invalid project structure. (are you in the wrong directory?)")
		exit(1)
		return
	
	if 2 > len(sys.argv):
		print("ERROR: No subcommand specified.")
		exit(1)
		return
	
	subcommand = sys.argv[1]

	if subcommand == "build":
		if 3 > len(sys.argv):
			print("ERROR: No project version specified.")
			exit(1)
			return
		
		project = parse_project(os.getcwd(), os.getcwd() + "/versions/" + sys.argv[2] + ".toml")

		project.build("dist/" + sys.argv[2])

		return

	print("ERROR: Invalid subcommand.")
	exit(1)

if __name__ == "__main__":
	main()