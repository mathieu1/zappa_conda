# zappa_conda
Example of deploying apps using zappa and conda

## Requirements

The instructions below are meant to be executed on a linux 64-bit machine.
- Install `conda` (e.g. using the [Miniconda](http://conda.pydata.org/miniconda.html) installer) and make sure `conda` is on your path.
- Change your bucket name in `zappa_settings.json`.

## First deployment
Clone this repository, then

```shell
cd zappa_conda
conda env create
source activate zappa_conda_env
zappa deploy dev
```

## Subsequent deployments

(This will overwrite the `zappa_conda_env` conda environment)
```shell
conda env create --force
source activate zappa_conda_env
zappa update dev
```

## Testing the package size

The `package_size` executable zips the current project and displays the resulting size.