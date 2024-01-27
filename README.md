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
Convert prefix to relative path: `~/path/to/repo/venv` -> `./venv`
```shell
sed -i 's|prefix: .*|prefix: ./venv|' environment.yml
```

# Run the app

```shell
python src/app.py
```


