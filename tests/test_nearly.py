import pytest

from nearly import Nearly


@pytest.mark.parametrize("value", [1, [], {}, (), set()])
def test_identity(value):
    assert Nearly(value) == value


@pytest.mark.parametrize(
    "this,that",
    [
        ([1, 2, ...], [1, 2, 3, 4]),
        ([1, 2, 3, 4], [1, 2, ...]),
        ([..., 3, 4], [0, 0, 0, 3, 4]),
        ([...], [...]),
        ([..., 1, 2, ...], [..., 1, 2, ...]),
    ],
)
def test_compare_list(this, that):
    assert Nearly(this) == that


@pytest.mark.parametrize(
    "this,that",
    [
        ([1, 2], [2, 3, ...]),
        ([..., 1, 2, ...], [..., 3, 4, ...]),
    ],
)
def test_negative_compare_list(this, that):
    assert Nearly(this) != that


@pytest.mark.parametrize(
    "this,value",
    [
        ([1, 2, 3], 1),
        ([...], 1),
    ],
)
def test_contains_list(this, value):
    assert value in Nearly(this)


@pytest.mark.parametrize(
    "this,value",
    [
        ([2, 3], 1),
    ],
)
def test_not_contains_list(this, value):
    assert value not in Nearly(this)


@pytest.mark.parametrize(
    "this,that",
    [
        ((1, 2, ...), (1, 2, 3, 4)),
        ((1, 2, 3, 4), (1, 2, ...)),
        ((..., 3, 4), (0, 0, 0, 0, 3, 4)),
    ],
)
def test_compare_tuple(this, that):
    assert Nearly(this) == that


@pytest.mark.parametrize(
    "this,that",
    [
        ((1, 2), (2, 3, ...)),
    ],
)
def test_negative_compare_tuple(this, that):
    assert Nearly(this) != that


@pytest.mark.parametrize(
    "this,value",
    [
        ((1, 2, 3), 1),
        ((...,), 1),
    ],
)
def test_contains_tuple(this, value):
    assert value in Nearly(this)


@pytest.mark.parametrize(
    "this,value",
    [
        ((2, 3), 1),
    ],
)
def test_not_contains_tuple(this, value):
    assert value not in Nearly(this)


@pytest.mark.parametrize(
    "this,that",
    [
        ({1, 2, ...}, {1, 3, 4, 2}),
        ({1, 3, 4, 2}, {1, 2, ...}),
    ],
)
def test_compare_set(this, that):
    assert Nearly(this) == that


@pytest.mark.parametrize(
    "this,value",
    [
        ({1, 2, 3}, 1),
        ({...}, 1),
    ],
)
def test_contains_set(this, value):
    assert value in Nearly(this)


@pytest.mark.parametrize(
    "this,value",
    [
        ({2, 3}, 1),
    ],
)
def test_not_contains_set(this, value):
    assert value not in Nearly(this)


@pytest.mark.parametrize(
    "this,that",
    [
        ({"name": "alice", "size": "large"}, {"name": "alice", "size": ...}),
        ({"name": "alice", ...: None}, {"name": "alice", "color": "purple"}),
        ({"name": "alice", "size": "llarge"}, {"name": "alice", ...: None}),
    ],
)
def test_compare_dict(this, that):
    assert Nearly(this) == that


@pytest.mark.parametrize(
    "this,that",
    [
        ({"name": "alice", ...: None}, {"color": "purple"}),
    ],
)
def test_negative_compare_dict(this, that):
    assert Nearly(this) != that


@pytest.mark.parametrize(
    "this,that",
    [
        (
            {"people": {"alice", "bob", ...}},
            {"people": {"mallory", "carol", "alice", "bob"}},
        ),
        (
            ("cn=user1,dc=example,dc=com", {"cn": "user1", "sn": "user1"}),
            ("cn=user1,dc=example,dc=com", {"cn": "user1", "sn": ...}),
        ),
        (
            {"name": "alice", "age": 40, "widgets": {"thing1": {"size": "large"}}},
            {"name": "alice", "age": 40, "widgets": {"thing1": {"size": ...}}},
        ),
    ],
)
def test_compare_nested(this, that):
    assert Nearly(this) == that


@pytest.mark.parametrize(
    "this,that",
    [
        (
            {"people": {"alice", "bob", ...}},
            {"people": {"mallory", "carol", "bob"}},
        ),
        (
            ("cn=user1,dc=example,dc=com", {"cn": "user1", "sn": "user1"}),
            ("cn=user1,dc=example,dc=com", {"cn": "user1"}),
        ),
        (
            {"name": "alice", "age": 40, "widgets": {"thing1": {"size": "large"}}},
            {"name": "alice", "age": 40, "widgets": {"thing2": {"size": ...}}},
        ),
    ],
)
def test_negative_compare_nested(this, that):
    assert Nearly(this) != that
