# mini_util

## Project Setup


Commands and steps:

```
# init project
poetry new <package-name>

cd <package-name>

# you can init your git here

# if ready to release
poetry version  # this will display version
poetry version 0.1.2  # this will set version to 0.1.2
poetry publish --build  # this will publish to pypi and build to `dist/`, you may need to wait around 2 mins to update
```
