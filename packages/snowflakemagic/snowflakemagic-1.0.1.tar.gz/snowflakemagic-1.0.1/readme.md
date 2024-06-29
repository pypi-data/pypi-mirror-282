# Snowflake Magic 

An ipython magic function to simplify usage of Snowflake SQL in your notebooks.

Example
```
import pandas as pd
result = %snowflake SELECT timestamp, value FROM mytable;
df = pd.DataFrame(result)
df.plot.line();
```

## Setup and Configuration

### Install the extension

```
pip install snowflakemagic
```

### Load extension
```
%reload_ext snowflakemagic
```

## Available magic functions

### %snowflake_auth
Inline function connecting to your snowflake account. Reads connection parameters from .env file:

You can either authenticate via SSO, which opens an external browser, or using credentials. 

Provide your snowflake account details:

```
snowflake_account="<YOUR-SNOWFLAKE-ACCOUNT>"
```

If you want to connect via sso, provide your sso username: 

```
snowflake_ssouser="<YOUR-SSO-USERNAME>"
```

If you want to connect via use-credentials, provide the password, otherwise SSO authentication is used.
```
snowflake_user="<YOUR-USERNAME>"
snowflake_password="<YOUR-PASSWORD>"
```

For more details on .env file see [How to NOT embedded credential in Jupyter notebook](https://yuthakarn.medium.com/how-to-not-show-credential-in-jupyter-notebook-c349f9278466) or [python-dotenv](https://pypi.org/project/python-dotenv/)


### %%snowflake, %snowflake or %snowflake_script
* Executes a snowflake query/script and returns the result as a json object. 
* Multiple queries/statements separated by ; can be exceuted, but only last result will be returned. 
* A query MUST end with a semi-colon (;)

### Example 1 
Query in code-cell
```
%%snowflake my_result
SELECT * 
    FROM xyz;
```

.. use result in another code cell:
```
import pandas as pd

#put result into a dataframe
df = pd.DataFrame(my_result)

#...
```

### Example 2 - Inline query
```
import pandas as pd

my_result = %snowflake SELECT * FROM xyz;
df = pd.DataFrame(my_result)

#...
```

### Example 3 - From script
Query using external query script files e.g. myscript.snowql
```
SELECT * FROM xyz;
```

Then in your code-cell, pass the script name 
```
import pandas as pd

my_result = %snowflake_script myscript.snowql
df = pd.DataFrame(my_result)

#...
```

### Example 4 - Parameterized script
Query using external query script files e.g. myscript.snowql which can be parameterized
```
SELECT * FROM xyz WHERE mycolumn=@MYVALUE@@;
```

Then in your code-cell, pass the script name 
```
import pandas as pd

my_result = %snowflake_script myscript.snowql @@MYVALUE@@=test
df = pd.DataFrame(my_result)

#...
```

### Example 5 - Chaining multiple scripts
You can also chain multiple scripts

mycte.snowql
```
WITH
    my_cte AS (
        SELECT col_1, col_2
            FROM xyz
    )
```

myscript.snowql
```
SELECT * FROM my_cte WHERE col_1=@MYVALUE@@;
```

Then in your code-cell, you can append the various script files
```
import pandas as pd

my_result = %snowflake_script mycte.snowql<<myscript.snowql @@MYVALUE@@=test
df = pd.DataFrame(my_result)

#...
```