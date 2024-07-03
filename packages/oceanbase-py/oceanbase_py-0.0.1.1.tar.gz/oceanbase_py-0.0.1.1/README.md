# OceanBase Python Client
A OceanBase client for the Python programming language.

OceanBase is a high-performance, real-time analytical database based on MPP architecture, known for its extreme speed and ease of use. It only requires a sub-second response time to return query results under massive data and can support not only high-concurrent point query scenarios but also high-throughput complex analysis scenarios. All this makes OceanBase an ideal tool for scenarios including report analysis, ad-hoc query, unified data warehouse, and data lake query acceleration. On OceanBase, users can build various applications, such as user behavior analysis, AB test platform, log retrieval analysis, user portrait analysis, and order analysis.

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
