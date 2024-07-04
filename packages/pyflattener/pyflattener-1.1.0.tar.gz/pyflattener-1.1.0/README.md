# pyflattener
One useful utility for making Swimlane Bundles is the Flattener, which helps to simplify complex JSON.

## Basic Usage
```python
from pyflattener import Flattener, do_flatten

data = {
    "outer_key": {
        "inner_key1": "inner val 1",
        "inner_key2": "inner val 2"
    },
    "basic_key": "value",
    "basic_list": ["1", "2", "3"],
    "mixed_list": [1, "2", "3"],
    "basic_list2": [1, 2, 3]
}

# Simple flatten
flat_data = do_flatten(data)

# Instance analogue
flat_data = Flattener(prefix=None, stringify_lists=True, shallow_flatten=False,
                      keep_simple_lists=True, autoparse_dt_strs=True).flatten(data)
```
flat_data will now look like:
```python
{
'outer_key_inner_key1': 'inner val 1',
'basic_list': ['1', '2', '3'],  # Simple list kept as a list
'basic_key': 'value',
'outer_key_inner_key2': 'inner val 2',
'basic_list2': [1, 2, 3],  # Simple list kept as list
'mixed_list': '1,2,3'  # Nonsimple list CVSV'd
}
```
Here is a description of the params you can pass to a Flattener() object or do_flatten

### Prefix
Prefix to add to the data after flattening
```python
do_flatten({"a": 5}, prefix="my_prefix")
# {"my_prefix_a": 5}
```

### Stringify Lists
Turn lists with basic types into CSV, defaults to True. This option is ignored for simple lists if keep_simple_lists is True
```python
stringify = <True or False>
do_flatten({"a": [1,2,3]}, stringify_lists=stringify, keep_simple_lists=False)
# True -> {"a": "1,2,3"}
# False -> {"a": [1,2,3]}
```

### Shallow Flatten
Ignore the first level of nesting, and only flatten each element within it. Used for lists of dictionaries
```python
data = [
    {"a": { "sub_a": 1 }, "b": 5},
    {"a": { "sub_a": 2 }, "b": 6},
]
shallow = <True or False>
do_flatten(data, shallow_flatten=shallow)
# True -> [
#    {"a_sub_a": 1, "b": 5},
#    {"a_sub_a": 2, "b": 6}
# ]

# False -> {"a_sub_a": [1,2], "b": [5,6]}
```

### Keep Simple Lists
If a list in the resulting flattened dict is only integers or only strings, even if stringify_lists is True, keep this list
```python
simple = <True or False>
do_flatten({"a": [1,2,3], "b": ["c", 4]}, keep_simple_lists=simple)
# True -> {"a": [1,2,3], "b": "c,4"}
# False -> {"a": "1,2,3", "b": "c,4"}
```

## Misc Flattening Functions
There are many useful flattening functions for more complicated data

### Hoist Key(s)

Grab keys from a list of dicts
```python
hoist_key("a", [{"a": 5}, {"a": 6}])
# -> [5, 6]

hoist_keys(["a", "b"], [{"a": 5, "b": 1}, {"a": 6, "b": 2}])
# -> [[5, 6], [1, 2]]
```

### Replace Dict Prefix
Replace a prefix in a dictionary
```python
replace_dict_prefix("aaa", "bbbb", {"aaa_data": 5})
# -> {'bbbb_data': 5}
# Or more commonly like:

replace_dict_prefix("aaa_", "", {"aaa_data": 5})
# -> {'data': 5}
```
### Merge Dicts
Merge two dictionaries together, regardless if they share keys or not.
If they share keys, it uses combine_listdict
```python
merge_dicts({"a": 1}, {"b": 2})
# -> {"a": 1, "b": 2}

merge_dicts({"a": 1}, {"a": 2})
# -> {"a": [1, 2]})
```
### Is SimpleList

Check if a list is purely of integers or purely of strings
```python
is_simplelist([1,2,3])
# -> True
is_simplelist([1,2,"3"])
# -> False
```

### Flatten Single Lists

Flatten all keys in a dict that are lists with a single entry
```python
flatten_single_lists({"a": [1,2,3], "b": [5]})
# -> {"b": 5,"a": [1, 2, 3]}
```

### Combine ListDict

Combine a list of dictionaries into a single dictionary
```python
combine_listdict([{"a": 1},{"a": 2}, {"a": 3}])
# -> {"a": [1, 2, 3]}

complicated_data = [
    {
        "a": "entry 1",
        "b": "v1"
    },
    {
        "b": "v2"
    },
    {
        "a": "entry 2"
    }
]
combine_listdict(complicated_data)
# -> {
#   'a': ['entry 1', None, 'entry 2'],
#   'b': ['v1', 'v2', None]
#}
```
Note how the missing entries were filled in with None This is to ensure the ordering of elements can be 
obtained in the flattened dict result.

Also note that attempting to combine a list of dictionaries with nonbasic keys (subdicts or lists) can
lead to odd results, or not be possible to combine in that form

### Clean XMLToDict Result

XMLToDict returns very ugly data, this helps clean it up. It only cleans top-level keys, so it is most 
effective after flattening

```python
import xmltodict

ugly_xml = "<xml><key attr=\"5\">val</key></xml>"
xml_dict = xmltodict.parse(ugly_xml)
clean_xmltodict_result(do_flatten(xml_dict))
# -> {u'xml_key_text': u'val', u'xml_key_attr': "5"}
```