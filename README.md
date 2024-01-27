Table of contents
- [Manage dependencies and virtual environment](#manage-dependencies-and-virtual-environment)
  * [Create the virtual environment from the environment.yml file](#create-the-virtual-environment-from-the-environmentyml-file)
  * [Activate the virtual environment](#activate-the-virtual-environment)
  * [Verify the virtual environment dependencies](#verify-the-virtual-environment-dependencies)
  * [Install a new dependency](#install-a-new-dependency)
  * [Remove a dependency](#remove-a-dependency)
  * [Update environment.yml file](#update-environmentyml-file)
- [Run the app](#run-the-app)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Manage dependencies and virtual environment

## Create the virtual environment from the environment.yml file
```shell
conda env create -f environment.yml
```
## Activate the virtual environment
```shell
conda activate ./venv
```
## Verify the virtual environment dependencies
```shell
conda list
```
## Install a new dependency
```shell
conda install <dependency>
```
## Remove a dependency
```shell
conda remove <dependency>
```
## Update environment.yml file
```shell
conda env export --verbose --no-builds --from-history --prefix ./venv > environment.yml
```
Important:
The export command will set `prefix` and `name` as an absolute path from your personal home directory to the `./venv` in the root of the project, so you'll need to convert the prefix to a relative path pointing to the project's root directory (`~/path/to/repo/venv` -> `./venv`).
You can do this on linux with the following `sed` command:
```shell
sed -i 's|prefix: .*|prefix: ./venv|; s|name: .*|name: new_environment_name|' environment.yml
```

# Run the app
```shell
python src/app.py
```


