# nearly: a tool for approximate matching of complex structures

`nearly` lets you test the equality of complex structures when you only care
about some of the values. A `...` value acts as a wildcard, causing any value
to match.

For example, the following statements are all `True`:

```
>>> from nearly import Nearly
>>> Nearly(1) == ...
True
>>> Nearly([1, 2, 3, 4]) == [1, 2, ...]
True
>>> Nearly({"name": "alice", "widgets": 10}) == {"name": "alice", "widgets": ...}
True
```

But these are `False`:

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
