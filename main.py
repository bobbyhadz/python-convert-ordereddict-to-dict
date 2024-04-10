# Convert an OrderedDict to a regular Dict in Python

from collections import OrderedDict
import json

# ✅ Convert an OrderedDict to a regular Dict

ordered_dict = OrderedDict(
    [('first', 'bobby'),
     ('last', 'hadz'),
     ('age', 30)]
)

dictionary = dict(ordered_dict)

# 👇️ {'first': 'bobby', 'last': 'hadz', 'age': 30}
print(dictionary)
print(type(dictionary))  # 👉️ <class 'dict'>

# ---------------------------------------------------

# ✅ Convert a nested OrderedDict to a regular dict

ordered_dict = OrderedDict(
    [('name', 'bobbyhadz'),
     ('address', OrderedDict([('post_code', 123)])),
     ]
)

json_str = json.dumps(ordered_dict)

regular_dict = json.loads(json_str)

# 👇️ {'name': 'bobbyhadz', 'address': {'post_code': 123}}
print(regular_dict)

print(type(regular_dict))  # 👉️ <class 'dict'>