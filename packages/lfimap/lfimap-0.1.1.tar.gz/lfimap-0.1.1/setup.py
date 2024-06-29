import pathlib
import setuptools

# Function to read the requirements.txt file
def read_requirements():
    requirements_path = pathlib.Path(__file__).parent / 'requirements.txt'
    if requirements_path.exists():
        with open(requirements_path) as req_file:
            return req_file.read().splitlines()
    else:
        return []

setuptools.setup(
	name = "lfimap",
	version = "0.1.1",
	description = "Local File Inclusion discovery and exploitation tool",
	long_description = pathlib.Path("README.md").read_text(),
	long_description_content_type = "text/markdown",
	url = "https://github.com/hansmach1ne /LFImap",
	author = "@h4nsmach1ne",
	license = "Apache License",
	project_urls = {
		"Installation": "https://github.com/hansmach1ne/lfimap/wiki/Installation",
		"Source": "https://github.com/hansmach1ne/LFImap"
	},
	python_requires = ">=3.8,<3.15",
	install_requires= read_requirements(),
	packages = setuptools.find_packages(),
	include_package_data = True,
	entry_points = {"console_scripts": ["lfimap = lfimap.lfimap:main"]}
)