# mysql_wrap
A wrapper for Python Mysqldb with pandas functionality.

- Emiliano Lupo @HENN, June 2024
- Documentation https://pypi.org/project/mysqlwrap/
- License: GPL v2

Built on top of the SimpleMysql package available at https://github.com/knadh/simplemysql

# Installation
with pip:

pip install mysql_wrap

from source:

 python -m pip install .

# Usage
## For normal connection
```python
from mysql_wrap import MysqlWrap, ConnectionOptions

options = ConnectionOptions(
	host="127.0.0.1",
	db="mydatabase",
	user="username",
	passwd="password",
	keep_alive=True # try and reconnect timedout mysql connections?
)

db = MysqlWrap(**options)
```

## For SSL Connection
```python
from mysql_wrap import MysqlWrap

db = MysqlWrap(
    host="127.0.0.1",
    db="mydatabase",
    user="username",
    passwd="password",
    ssl = {'cert': 'client-cert.pem', 'key': 'client-key.pem'},
    keep_alive=True # try and reconnect timedout mysql connections?
)

```


```python
# insert a record to the <em>books</em> table
db.insert("books", {"type": "paperback", "name": "Time Machine", "price": 5.55, year: "1997"})

book = db.getOne("books", ["name"], ["year = 1997"])

print "The book's name is " + book.name
```

# Utility methods
getDataTypefromDType(), setMySqlFieldName()

# Pandas methods
getTable(), createTable(), SyncColumns(), insertFromDataFrame(), InsertOrUpdateFromDataFrame(), CreateInsertTable(), CreateUpdateTable()

# regular Query methods
insert(), update(), insertOrUpdate(), describe(), delete(), getOne(), getAll(), lastId(), query(), tableExist()

## insert(table, record{})
Inserts a single record into a table.

```python
db.insert("food", {"type": "fruit", "name": "Apple", "color": "red"})
db.insert("books", {"type": "paperback", "name": "Time Machine", "price": 5.55})
```

## update(table, row{}, condition[])
Update one more or rows based on a condition (or no condition).

```python
# update all rows
db.update("books", {"discount": 0})

# update rows based on a simple hardcoded condition
db.update("books",
	{"discount": 10},
	["id=1"]
)

# update rows based on a parametrized condition
db.update("books",
	{"discount": 10},
	("id=%s AND year=%s", [id, year])
)
```
## insertBatch(table, rows{})
Insert Multiple values into table.

```python
# insert multiple values in table
db.insertBatch("books", [{"discount": 0},{"discount":1},{"discount":3}])
```

## insertOrUpdate(table, row{}, key)
Insert a new row, or update if there is a primary key conflict.

```python
# insert a book with id 123. if it already exists, update values
db.insertOrUpdate("books",
		{"id": 123, type": "paperback", "name": "Time Machine", "price": 5.55},
		"id"
)
```

## getOne(table, fields[], where[], order[], limit[])
## getAll(table, fields[], where[], order[], limit[])
Get a single record or multiple records from a table given a condition (or no condition). The resultant rows are returned as namedtuples. getOne() returns a single namedtuple, and getAll() returns a list of namedtuples.

```python
book = db.getOne("books", ["id", "name"])
```

```python
# get a row based on a simple hardcoded condition
book = db.getOne("books", ["name", "year"], ("id=1"))
```

```python
# get multiple rows based on a parametrized condition
books = db.getAll("books",
	["id", "name"],
	("year > %s and price < %s", [year, 12.99])
)
```

```python
# get multiple rows based on a parametrized condition with an order and limit specified
books = db.getAll("books",
	["id", "name", "year"],
	("year > %s and price < %s", [year, 12.99]),
	["year", "DESC"],	# ORDER BY year DESC
	[0, 10]			# LIMIT 0, 10
)
```
## lastId()
Get the last insert id
```python
# get the last insert ID
db.lastId()
```

## lastQuery()
Get the last query executed
```python
# get the SQL of the last executed query
db.lastQuery()
```

## delete(table, fields[], condition[], order[], limit[])
Delete one or more records based on a condition (or no condition)

```python
# delete all rows
db.delete("books")

# delete rows based on a condition
db.delete("books", ("price > %s AND year < %s", [25, 1999]))
```

## query(table)
Run a raw SQL query. The MySQLdb cursor is returned.

```python
# run a raw SQL query
db.query("DELETE FROM books WHERE year > 2005")
```

## commit()
Insert, update, and delete operations on transactional databases such as innoDB need to be committed

```python
# Commit all pending transaction queries
db.commit()
```

To run tests: 

- add your test file to the tests/ folder

- import the modules you want to test using src.folder.module path

- run tests from terminal from the project root folder:
    python3 -m unittest tests.{test file} 
