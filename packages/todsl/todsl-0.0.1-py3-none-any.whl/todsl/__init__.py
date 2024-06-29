from typing import Optional
from git import Repo
import tomllib
import os

class Component:
	def __init__(self, path: str, name: str, author: str, header: Optional[str], functions: list, footer: Optional[str], prebuild: list, postbuild: list):
		self.path = path
		self.name = name
		self.author = author
		self.header = header
		self.functions = functions
		self.footer = footer
		self.prebuild = prebuild
		self.postbuild = postbuild

class Project:
	def __init__(self, path: str, name: str, version: str, description: str, prebuild: list, postbuild: list):
		self.path = path
		self.name = name
		self.version = version
		self.description = description
		self.prebuild = prebuild
		self.postbuild = postbuild
		self.components = {}
	
	def add_component(self, component: Component):
		self.components[component.name] = component
	
	def build(self, output_path):
		os.makedirs(output_path, exist_ok=True)

		for command in self.prebuild:
			os.system(command.replace("[output]", output_path))

		repo = Repo(self.path)

		for name in self.components.keys():
			component = self.components[name]

			for command in component.prebuild:
				os.system(command.replace("[output]", output_path))

			code = ""

			if component.header != None:
				file = repo.commit(component.header).tree / component.path
				code += "// start header: " + component.header + "\n" + file.data_stream.read().decode() + "\n// end header: " + component.header + "\n"
			
			for function in component.functions:
				file = repo.commit(function).tree / component.path
				code += "// start function: " + function + "\n" + file.data_stream.read().decode() + "\n// end function: " + function + "\n"
			
			if component.footer != None:
				file = repo.commit(component.footer).tree / component.path
				code += "// start footer: " + component.footer + "\n" + file.data_stream.read().decode() + "\n// end footer: " + component.footer + "\n"
			
			os.makedirs(os.path.dirname(output_path + "/" + component.path), exist_ok=True)

			f = open(output_path + "/" + component.path, "w")
			f.write(code)
			f.close()

			for command in component.postbuild:
				os.system(command.replace("[output]", output_path))
		
		for command in self.postbuild:
			os.system(command.replace("[output]", output_path))

def parse_project(base_path, project_toml_path):
	f = open(project_toml_path, "rb")
	data = tomllib.load(f)
	f.close()

	project = Project(
		base_path,
		data["project"]["name"],
		data["project"]["version"],
		data["project"]["description"],
		data["project"]["prebuild"],
		data["project"]["postbuild"]
	)

	for name in data["components"].keys():
		component_data = data["components"][name]

		component = Component(
			component_data["path"],
			name,
			component_data["author"],
			component_data["header"] if "header" in component_data else None,
			component_data["functions"],
			component_data["footer"] if "footer" in component_data else None,
			component_data["prebuild"],
			component_data["postbuild"]
		)

		project.add_component(component)

	return project