#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
import builtins
import os
from setuptools import setup, find_packages
from dotenv import load_dotenv


#------------------------------------------------------------------------
# 환경 변수 목록 파일 로드.
#------------------------------------------------------------------------
load_dotenv()
VERSION = os.getenv("VERSION")
NAME = os.getenv("NAME")
AUTHOR = os.getenv("AUTHOR")
AUTHOR_EMAIL = os.getenv("AUTHOR_EMAIL")
DESCRIPTION = os.getenv("DESCRIPTION")
LONG_DESCRIPTION_CONTENT_TYPE = os.getenv("LONG_DESCRIPTION_CONTENT_TYPE")
URL = os.getenv("URL")
PYTHON_REQUIRES = os.getenv("PYTHON_REQUIRES")
PYPI_API_TOKEN = os.getenv("PYPI_API_TOKEN")
builtins.print(f"set PYPI_API_TOKEN={PYPI_API_TOKEN}")

#------------------------------------------------------------------------
# 설치.
#------------------------------------------------------------------------
setup(
	name = NAME,
	version = "v0.0.11",
	author = AUTHOR,
	author_email = AUTHOR_EMAIL,
	description = DESCRIPTION,
	long_description = open(file = "README.md", mode = "r", encoding = "utf-8").read(),
	long_description_content_type = LONG_DESCRIPTION_CONTENT_TYPE,
	url = URL,
	packages = find_packages(),
	include_package_data = True,
	package_data = {
		"": [
			"resources/*"
		],
	},
    install_requires = [
		"pyinstaller",
		"debugpy"
	],
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires = PYTHON_REQUIRES
)