# FasterTK
A FastAPI based framework, that allows fast release with data integrity and security.

# Why?
A FasterTK wants to apply the Zen of python to FastAPI. FastAPI is great in giving freedom and performance, but not in giving a One, obvious way to do stuff. It requires repeating stuff, as database inteactions, and json schemas are defined on seperate places. FasterTK is a list of seperate tools, that can be used seperatly. However, together they give the programmer a fast route to a secure and fast app.

## Principles
* Everything is forbidden, unless specified otherwise, or you're in god mode.
* A data scheme should be defined in one place.
* A data scheme should also define the circumstances any row should be inserted, read, updated or deleted. The data sceme should define the default behaviour of all it's components.
* Checking the Api, should lead to testing.
* The toolkit must define the structure of the code, and provide ways to eavluate the code.

## Tools
* TorotoiSec: This tool expends of the excelent torotise ORM with lambda functions that prevent inserting, updating, selecting or deleting, without explicit permission. (Comming Soon)
* PydanSec: A mode of pydantic that can be translated easly into TorotoiSec. (Comming Soon)
* Faster: A wrapper on fastAPI with additional permission handling, and updating openapi.json (Comming Soon)
* FasterAuth: Data schemes for users and groups. As this is an API library, it contains a wide varity of auth scemes. (Comming Soon)
* PostToTest: A UI tool to test Api requests live, and to create a TestSuite to run. This tool is also designed to help examine secutiy decitions.(Comming Soon)