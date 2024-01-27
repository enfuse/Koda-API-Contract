Table of contents

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
conda env export --verbose --no-builds --name venv --from-history > environment.yml
```
Important:
The export command will set the prefix as an absolute path from your personal home directory, so you'll need to convert the prefix to a relative path pointing to the project's root directory (`~/path/to/repo/venv` -> `./venv`).
You can do this on linux with the following `sed` command:
```shell
sed -i 's|prefix: .*|prefix: ./venv|' environment.yml
```

# Run the app
```shell
python src/app.py
```


