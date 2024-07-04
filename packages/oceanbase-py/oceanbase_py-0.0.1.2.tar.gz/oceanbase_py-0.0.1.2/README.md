# OceanBase Python Client
A OceanBase client for the Python programming language.

OceanBase is an enterprise distributed relational database with high availability, high performance, horizontal scalability, and compatibility with SQL standards.

## Installation
```
pip install oceanbase_py
```


## SQLAlchemy Usage

To connect to OceanBase using SQLAlchemy, use a connection string (URL) following this pattern:

- **User**: User Name
- **Password**: Password
- **Host**: host
- **Port**: port
- **Database**: Database Name

[//]: # (- **Schema**: Schema Name)



Here's what the connection string looks like:

```
oceanbase://<User>:<Password>@<Host>:<Port>/<Database>
oceanbase_py://<User>:<Password>@<Host>:<Port>/<Database>
```

```
oceanbase://<User>:<Password>@<Host>:<Port>/<Owner>
oceanbase_py://<User>:<Password>@<Host>:<Port>/<Owner>
```

## Example
It is recommended to use python 3.x to connect to the OceanBase database, eg:
```
from sqlalchemy import create_engine
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.sql.expression import select, text

engine = create_engine('oceanbase://root:xxx@localhost:8081/db')
connection = engine.connect()

rows = connection.execute(text("SELECT * FROM test")).fetchall()
```

## Limits
- Oracle tenants are not currently supported.