# ox-db


ox-db is an open-source a lib to handle documents read write of different data structures efficiently and serialization, deserialization and processing

## Installation:

always build from source for latest and bug free version

### build from source :

```
pip install git+https://github.com/ox-ai/ox-doc.git
```
### from pip
```
pip install ox-doc
```
## docs :

- [docs.md](./docs/docs.md) will be released after major release


## oxd : OxDox

- ox-db uses `.oxd` virtual file(folder acts as file) format to store data in a bson file and also index it for efficiency and handelling hugefiles,

- `.oxd` is a hybrid file fromat stores data key-value pairs 

to work with oxd file or to use it in your project refere [test.oxd](test.oxd.ipynb) and [docs.oxd](./docs/oxd.md) 

### code snippet :

```py
from ox_doc.ld import OxDoc 

doc = OxDoc('data')

doc.set("k1"," dummy data-1")
doc.get("k1")
doc.add({'key4': 'value4', 'key5': 'value5'})
doc.delete("k1")

doc.load_data()
```



## directory tree :

```tree
.
├── __init__.py
└── d1.py
```