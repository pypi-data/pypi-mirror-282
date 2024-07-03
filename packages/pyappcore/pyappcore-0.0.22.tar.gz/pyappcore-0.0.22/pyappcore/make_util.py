#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union
import builtins
import ast
from datetime import datetime as DateTime
import importlib
import inspect
import json
import os
from .json_util import RemoveAllCommentsInString
from .str_util import GetSplitFilePath


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
DEPENDENCIESINBUILDFILENAME : str = "__pyappcore_dependencies_in_build__.py"
SYMBOLSINBUILDFILENAME : str = "__pyappcore_symbols_in_build__.py"
SEMICOLON : str = ";"
COLON : str = "."
PYEXTENSION : str = ".py"
PACKAGE : str = "PACKAGE"
MODULE : str = "MODULE"
CLASS : str = "CLASS"
FUNCTION : str = "FUNCTION"
CARRIAGERETURN : str = "\r"
LINEFEED : str = "\n"
READMODE : str = "r"
WRITEMODE : str = "w"
UTF8 : str = "utf-8"


#------------------------------------------------------------------------
# 대상 디렉토리에서 모듈을 찾아서 목록을 반환.
#------------------------------------------------------------------------
def FindModuleFilePaths(moduleDirPath : str) -> set:
	moduleFilePaths = set()
	for root, dirs, files in os.walk(moduleDirPath):
		for file in files:
			if not file.lower().endswith(PYEXTENSION):
				continue
			moduleFilePaths.add(os.path.join(root, file))
	return moduleFilePaths


#------------------------------------------------------------------------
# 패키지 여부.
#------------------------------------------------------------------------
def IsPackage(name : str) -> bool:
	try:
		spec = importlib.util.find_spec(name)
		return spec and spec.submodule_search_locations
	except ModuleNotFoundError:
		return False


#------------------------------------------------------------------------
# import importTarget 일 때 importTarget의 종류 반환.
#------------------------------------------------------------------------
def GetImportType(importTargetName : str) -> str:
	try:
		importTarget = importlib.import_module(importTargetName)
		if IsPackage(importTarget):
			return PACKAGE
		if inspect.ismodule(importTarget):
			return MODULE
		elif inspect.isclass(importTarget):
			return CLASS
		elif inspect.isfunction(importTarget):
			return FUNCTION
		return None
	except Exception as exception:
		return None


#------------------------------------------------------------------------
# from fromTarget import importTarget 일 때 importTarget의 종류 반환.
#------------------------------------------------------------------------
def GetImportFromType(fromTargetName : str, importTargetName : str) -> str:
	try:
		fromTarget = importlib.import_module(fromTargetName)
		importTarget = builtins.getattr(fromTarget, importTargetName)
		importTargetFullName = f"{fromTargetName}.{importTargetName}"
		if IsPackage(importTargetFullName):
			return PACKAGE
		elif inspect.ismodule(importTarget):
			return MODULE
		elif inspect.isclass(importTarget):
			return CLASS
		elif inspect.isfunction(importTarget):
			return FUNCTION
		return None
	except Exception as exception:
		return None


#------------------------------------------------------------------------
# "# type: ignore" 를 추가할지 말지 여부.
#------------------------------------------------------------------------
def IsTypeIgnore(name : str) -> bool:
	if not name:
		return False
	try:
		if not importlib.util.find_spec(name):
			return True
	except Exception as exception:
		return True
	return False


#------------------------------------------------------------------------
# "# type: ignore" 를 추가할지 말지 여부.
#------------------------------------------------------------------------
def IsTypeIgnores(names : list[str]) -> bool:
	if not names:
		return False
	try:
		for name in names:
			if IsTypeIgnore(name):
				return True
	except Exception as exception:
		return True
	return False


#------------------------------------------------------------------------
# .vscode/settings.json 파일 불러오기.
#------------------------------------------------------------------------
def GetVisualStudioCodeSettings(rootDirPath : str) -> Union[dict, None]:
	try:
		settingsFilePath = f"{rootDirPath}/.vscode/settings.json"
		if os.path.exists(settingsFilePath):
			with builtins.open(settingsFilePath, READMODE, encoding = UTF8) as file:
				string = file.read()
				jsonText = RemoveAllCommentsInString(string)
				vscodeSettings = json.loads(jsonText)
				return vscodeSettings
		return None
	except Exception as exception:
		builtins.print(exception)
		return None


#------------------------------------------------------------------------
# 빌드시 심볼 파일 생성.
#------------------------------------------------------------------------
def CreateSymbolsInBuildToFile(symbols : list[str], symbolsDirPath : str) -> None:

	# 텍스트 작성.
	symbols = set(symbols)
	writelines = list()
	nowDateTime = DateTime.now()
	writelines.append(f"# Automatic dependency generation code used when building pyinstaller.")
	writelines.append(f"# Created time : {nowDateTime}")
	writelines.append("")
	writelines.append("")
	writelines.append(f"SYMBOLS = set()")
	for symbol in symbols:
		writelines.append(f"SYMBOLS.add(\"{symbol}\")")

	# 파일 작성.
	symbolsFilePath : str = f"{symbolsDirPath}/{SYMBOLSINBUILDFILENAME}"
	with open(symbolsFilePath, WRITEMODE, encoding = UTF8) as file:
		file.write(LINEFEED.join(writelines))


#------------------------------------------------------------------------
# 빌드시 의존성 참조 파일 생성.
#------------------------------------------------------------------------
def CreateDependenciesInBuildToFile(moduleDirPaths : list[str], includesDirPath : str) -> None:
	# 단독 임포트 금지 모듈 이름 목록.
	mustImportFroms = list()
	mustImportFroms.append("__future__")
	mustImportFroms.append("mathutils")

	# 제외 모듈, 파일 이름 목록.
	excludes = set()
	excludes.add(".")
	excludes.add("..")
	# for moduleFilePath in FindModuleFilePaths(CURRENTPATH):
	# 	path, name, extension = GetSplitFilePath(moduleFilePath)
	# 	excludes.add(moduleFilePath)
	# 	excludes.add(name)

	# 모든 모듈 파일 경로 가져옴.
	moduleFilePaths = set()
	for moduleDirPath in moduleDirPaths:
		filePaths = FindModuleFilePaths(moduleDirPath)
		for filePath in filePaths:
			if filePath in excludes:
				continue
			moduleFilePaths.add(filePath)

	# 저장 자료구조 추가.
	importData = dict()
	writelines = list()
	for moduleFilePath in moduleFilePaths:
		with open(moduleFilePath, READMODE, encoding = UTF8) as file:
			# 파싱 및 구문분석.
			astNode = ast.parse(file.read(), filename = moduleFilePath)   
			for current in ast.walk(astNode):
	
				# import 패키지 or 하위패키지 or 모듈.
				if isinstance(current, ast.Import):
					for alias in current.names:
						importTargetName = alias.name
						# importTargetType = GetImportType(alias.name)
						if importTargetName in excludes:
							continue
						if importTargetName in mustImportFroms:
							continue

						# importDatas.add(f"import {importTargetName}")
						# writelines.append(f"# [ast.Import][IMPORT] current.names.name: {importTargetName}, type: {importTargetType}")

						if not importTargetName in importData:
							importData[importTargetName] = list()

				# from 패키지 or 하위패키지 or 모듈 import 패키지 and 하위패키지 and 모듈 and 클래스 and 함수.
				elif isinstance(current, ast.ImportFrom):
					fromTargetName = current.module
					# fromTargettype = GetImportType(current.module)
					if fromTargetName:
						if fromTargetName in excludes:
							continue

						if not fromTargetName in importData:
							importData[fromTargetName] = set()

						# writelines.append(f"# [ast.ImportFrom][FROM] current.module: {fromTargetName}, type: {fromTargettype}")

						# 클래스나 함수 추가.
						for alias in current.names:
							importTargetName = alias.name
							importData[fromTargetName].add(importTargetName)
							# importTargetType = GetImportType(alias.name)
							# importAndFromDatas.add(f"from {fromTargetName} import {importTargetName}")
							# writelines.append(f"# [ast.ImportFrom][IMPORT] current.names.name: {importTargetName}, type: {importTargetType}")

	# 텍스트 작성.
	nowDateTime = DateTime.now()
	writelines.append(f"# Automatic dependency generation code used when building pyinstaller.")
	writelines.append(f"# Created time : {nowDateTime}")
	writelines.append("")
	writelines.append("")
	
	moduleNames = sorted(importData.keys())
	for fromTargetName in moduleNames:
		importTargetNames = importData[fromTargetName]
		if importTargetNames:
			importTargetsText = ", ".join(importTargetNames)
			if IsTypeIgnore(fromTargetName) or IsTypeIgnores(importTargetNames):
				writelines.append(f"from {fromTargetName} import {importTargetsText} # type: ignore")
			else:
				writelines.append(f"from {fromTargetName} import {importTargetsText}")
		else:
			if IsTypeIgnore(fromTargetName):
				writelines.append(f"import {fromTargetName} # type: ignore")
			else:
				writelines.append(f"import {fromTargetName}")

	# 파일 작성.
	includesFilePath : str = f"{includesDirPath}/{DEPENDENCIESINBUILDFILENAME}"
	with open(includesFilePath, WRITEMODE, encoding = UTF8) as file:
		file.write(LINEFEED.join(writelines))