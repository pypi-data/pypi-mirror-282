prettify-json
===========

make pretty json.

Documentation: https://github.com/VeritasXu/prettify-json


Installation
------------

```
pip install prettify-json
```


Usage
-----

```python
import json
import prettify_json as pj


# raw contents for json
boxes = [[1, 2, 3, 4],
         [2, 3, 1, 4]]

sample = {'id': 1}

# wrap data that want to indent = 0
sample['boxes'] = pj.NoIndent(boxes)

# dumps
json_data = pj.dumps(sample, indent=2)
print(json_data)

# write json
pj.write_json(sample, './tmp.json', indent=2)

# compare with raw
sample['boxes'] = boxes
raw_json = json.dumps(sample, indent=2)
print(raw_json)
```

   

**See default sample**

```python
from prettify_json import sample
raw, new = sample()

print('+++++++++ old +++++++++')
print(raw)

print('+++++++++ pretty +++++++++')
print(new)
```

**With Prettify**

![](./exp1.png)



**Without Prettify**

![](./exp2.png)


Authors
-------

See contributors section on GitHub.
