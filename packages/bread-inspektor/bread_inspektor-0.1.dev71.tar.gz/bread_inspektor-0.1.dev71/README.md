# idi-data-validation
Data Validation for IDI project

Welcome to Data Validation for the IDI Project. The purpose of this repo is to validate NTIA BEAD challenge process data.

**Note** This repo uses [pre-commit](https://pre-commit.com/) hook, please install by typing `pre-commit install`.

More information can be found:

1. [Video Link](https://www.youtube.com/watch?v=p3pOUUDEGVo)
2. [Detailed Description](https://broadbandusa.ntia.gov/technical-assistance/BEAD_Challenge_Process_Data_Submission)
3. [Challenge Submission Templates](https://broadbandusa.ntia.doc.gov/technical-assistance/BEAD_Challenge_Results_Submission_Templates)
4. [Link to challenge notice](https://www.internetforall.gov/bead-challenge-process-policy) This contains links to docs with detailed descriptions.


There are two components of this repo:
1. A set of scripts and utilities for generating CSVs for the illinois BEAD project.
2. A set of scripts and utilities for validating CSV files.


### IL Specific

The file `run_me.sh` will execute the illinois specific pipeline. This requires access to the illinois BEAD database.

* **Notebook** Contains work in progress notebooks
* **data** Data related to Illinois data generation project
* **scripts** Scripts relating to IL

### Data Validation

* **validation** Package for data validation.

Overview of Data Validation Package.

The purpose of this package is to execute and avoid common errors when submitting the NTIA CSV files.

#### Usage
To run the validations after placing data in the `/output_csv/` dir (IL-specific: run `run_me.sh`),

```console
mkdir logs
python validation/utils/validator.py output_csv --results_dir logs/
```

##### Installing route

I'll push this up to PyPI shortly, but for this commit, you can create an env and install this package via these commands.

```console
cd path/into/idi_data_validation_directory
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
bread_inspektor output_csv/
```


#### Current Status

| File name | Initial Code | Tests | Tested on IL | 
| --- | --- | --- | --- | 
| cai.csv | X | |  | 
| challengers.csv | X | |  |
| challenges.csv | X | | | 
| cai_challenges.csv |  | | 
| post_challenge_locations.csv | X | | | 
| post_challenge_cai.csv | X | | | 