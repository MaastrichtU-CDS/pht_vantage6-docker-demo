**Repository location moved! Please check [https://github.com/MaastrichtU-CDS/pht_vantage6-docker-demo](https://github.com/MaastrichtU-CDS/pht_vantage6-docker-demo)**
# Vantage6 Docker Demo

**This repository is still work-in-progress, please note that the documentation may be incomplete**

A video of this repository can be found at [https://vimeo.com/459005703](https://vimeo.com/459005703)

## How to run this infrastructure?
The infrastructure can simply be started by running `docker compose up -d`. The infrastructure can
then be taken down by running `docker compose down`

**Pro tip**: download the analysis containers before running the researcher algorithms. This will speed up the execution the first time. You can run the following command:
```
docker pull jaspersnel/vtg.tpl jaspersnel/v6-average-py
```

### For researchers to run their algorithm in Python
1. Go to the folder [./researcher/python](./researcher/python)
2. Execute `sh run.sh`

The run.py file contains the actual code as a researcher to execute a train on the infrastructure.

### For researchers to run their algorithm in R
1. Go to the folder [./researcher/R](./researcher/R)
2. Execute `sh run.sh`

The test.r file contains the actual code as a researcher to execute a train on the infrastructure.

TODO: This needs to be updated to a more mature version of the R code for Vantage6

## How to configure the infrastructure for more specific cases?

If the datafiles need to be changed, simply replace the `nodeX.csv` files in the [./containerfiles](./containerfiles)
directory.

To add or remove stations in the infrastructure:
- Make or remove additional `nodeX.yaml` and `nodeX.csv` files in the [./containerfiles](./containerfiles) directory.
- Duplicate or remove one of the organizations from the [./containerfiles/entities.yaml](./containerfiles/entities.yaml) file.
- Duplicate one of the node entries in the [./docker-compose.yml](./docker-compose-yml) file
