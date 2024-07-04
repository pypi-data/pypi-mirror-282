
## **NEW IN VERSION `2.0.0`**:
#### **Features:**
- Added `polars` functionality

#### **QL & Fixes:**
- Replaced `use_client` var with `gcp_client` for user clarity
- Fixed _N rows have been added to ..._ message in `write_bigquery()`


## **LICENSE**
### GPL-3 Summary:

You may copy, distribute and modify the software as long as you track changes/dates in source files. Any modifications to or software including (via compiler) GPL-licensed code must also be made available under the GPL along with build & install instructions.

**In other words, any derivative work of this software shall be released under the same GPL license as the original software, meaning the modified code must be exactly as free and open-source as the original.**


## ***ABOUT***

#### **gcloudy** is a wrapper for Google's GCP Python package(s) that aims to make interacting with GCP and its services more intuitive, especially for new GCP users. In doing so, it adheres to ***pandas-like*** syntax for function/method calls. 

#### The **gcloudy** package is not meant to be a replacement for GCP power-users, but rather an alternative for GCP users who are interested in using Python in GCP to deploy Cloud Functions and interact with certain GCP services, especially BigQuery and Google Cloud Storage.

#### The **gcloudy** package is built on top of cononical Google Python packages(s) without any alteration to Google's base code.


## ***INSTALL, IMPORT, & INITIALIZE***

- #### **gcloudy** is installed using pip with the _terminal_ command:

`$ pip install gcloudy`

- #### Once installed, the **BigQuery** class can be imported from the main **GoogleCloud** module with:

`from gcloudy.GoogleCloud import BigQuery`

- #### Then, the `bq` object is initialized with the following (where "gcp-project-name" is your GCP Project ID / Name):

`bq = BigQuery("gcp-project-name")`

- #### **NOTE**: It is important to also import the Pandas package:

`import pandas as pd`


## ***METHODS***

#### The following section contains the methods and their usage.

### ----------------------------


### `bq.read_bigquery` 
#### - Read an existing BigQuery table into a DataFrame.

#### _read_bigquery(bq_dataset_dot_table = None, date_cols = [], preview_top = None, to_verbose = True)_

- **bq_dataset_dot_table** : the "dataset-name.table-name" path of the existing BigQuery table
- **date_cols** : [optional] column(s) passed inside a list that should be parsed as dates
- **preview_top** : [optional] only read in the top ***N*** rows
- **to_verbose** : should info be printed? defaults to **True**

### EX:

```
my_table = bq.read_bigquery("my_bq_dataset.my_bq_table")
my_table = bq.read_bigquery("my_bq_dataset.my_bq_table", date_cols = ['date'])
```

### -----------


### `bq.write_bigquery` 
#### - Write a DataFrame to a BigQuery table.

#### _write_bigquery(df, bq_dataset_dot_table = None, use_schema = None, append_to_existing = False, to_verbose = True)_

- **df** : the DataFrame to be written to a BigQuery table
- **bq_dataset_dot_table** : the "dataset-name.table-name" path of the existing BigQuery table
- **use_schema** : [optional] a custom schema for the BigQuery table. **NOTE**: see **bq.guess_schema** below
- **append_to_existing** : should the DataFrame be appended to an existing BigQuery table? defaults to **False** (create new / overwrite)
- **to_verbose** : should info be printed? defaults to **True**

### EX:

```
bq.write_bigquery(my_data, "my_bq_dataset.my_data")
bq.write_bigquery(my_data, "my_bq_dataset.my_data", append_to_existing = True)
```

### -----------


### `bq.guess_schema`
#### - A helper for **bq.write_bigquery**, passed to its **use_schema** arg. Creates a custom schema based on the **dtypes** of a DataFrame.

***guess_schema(df, bq_type_default = "STRING")***

- **df** : the DataFrame to be written to a BigQuery table
- **bq_type_default** : default BQ type passed to **dtype** 'object'

### EX:

```
bq.write_bigquery(my_data, "my_bq_dataset.my_data", use_schema = bq.guess_schema(my_data))
```

### -----------


### `bq.read_custom_query`
#### - Read in a custom BigQuery SQL query into a DataFrame.

***read_custom_query(custom_query, to_verbose = True)***

- **custom_query** : the custom BigQuery SQL query that will produce a table to be read into a DataFrame
- **to_verbose** : should info be printed? defaults to **True**

### EX:

```
my_custom_table = bq.read_custom_query("""
    SELECT
        date,
        sales,
        products
    FROM
        my_bq_project_id.my_bq_dataset.my_bq_table
    WHERE
        sales_month = 'June'
""")
```

### -----------


### `bq.send_query`
#### - Send a custom SQL query to BigQuery. Note, does not return anything as the process is carried out within BigQuery.

***send_query(que, to_verbose = True)***

- **que** : the custom SQL query to be sent and carried out within BigQuery
- **to_verbose** : should info be printed? defaults to **True**

### EX:

```
bq.send_query("""
    CREATE TABLE my_bq_project_id.my_bq_dataset.my_new_bq_table AS 
    (
        SELECT
            date,
            sales,
            products
        FROM
            my_bq_project_id.my_bq_dataset.my_bq_table
        WHERE
            sales_month = 'June'
    )
""")
```

####
