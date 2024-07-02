# mini\_util

## Introduction

This is a simple example that construct a PyPI package with poetry.

## Project Setup

Commands and steps:

```sh
# init project
poetry new <package-name>

cd <package-name>

# you can init your git, and do something with it here

# if ready to release
poetry version  # this will display version
poetry version 0.1.2  # this will set version to 0.1.2
poetry publish --build  # this will publish to pypi and build to `dist/`, you may need to wait around 2 mins to update
```
