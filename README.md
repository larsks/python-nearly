# nearly: a tool for approximate matching of complex structures

`nearly` lets you test the equality of complex structures when you only care
about some of the values. A `...` value acts as a wildcard, causing any value
to match.

## Examples

When testing equality, `...` matches any value:

```
>>> from nearly import Nearly
>>> Nearly(1) == ...
True

```

At the end of a list, a `...` means "only pay attention to the values before this index":

```
>>> Nearly([1, 2, 3, 4]) == [1, 2, ...]
True

```

You can do the same thing at the beginning of a list:

```
>>> Nearly([1, 2, 3, 4]) == [..., 3, 4]
True

```

As a dictionary value, `...` will match the value of the corresponding key:

```
>>> Nearly({"name": "alice", "widgets": 10}) == {"name": "alice", "widgets": ...}
True

```

As a key, `...` will match any key:

```
>>> Nearly({"something": "somevalue"}) == {...: None}
True

```

In this case, the value is ignored (`None` makes a good placeholder).

This is useful when you only want to test the equality of a subset of dictionary keys, as in:

```
>>> have = {"name": "widget", "color": "blue", "size": "large", "count": 10}
>>> want = {"name": "widget", "size": "large", ...: None}
>>> Nearly(have) == want
True

```

In a `set`, `...` matches any member, so:

```
>>> Nearly({1, 2, 3}) == {3, 1, ...}
True

```

The follow expressions all evaluate to `False`:

```
>>> Nearly(1) == 2
False
>>> Nearly([1, 2, 3, 4]) == [2, 3, ...]
False
>>> Nearly({"name": "alice", "widgets": 10}) == {"name": "alice", "widgets": ..., "color": "red"}
False

```

See the [`examples`](examples/) directory and the tests in `test_nearly.py` for more examples.

## Installation

```
pip install git+https://github.com/larsks/python-nearly
```
