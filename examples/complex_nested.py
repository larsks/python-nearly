from nearly import Nearly

have_does_not_match = {
    "name": "alice",
    "age": 40,
    "widgets": {
        "thing1": {
            "size": "large",
            "count": 10,
        },
        "thing3": {
            "size": "medium",
            "count": 10,
        },
    },
}

have_matches = {
    "name": "alice",
    "age": 40,
    "widgets": {
        "thing1": {
            "size": "large",
            "count": 10,
        },
        "thing2": {
            "size": "medium",
            "count": 10,
        },
        "thing3": {
            "size": "medium",
            "count": 10,
        },
    },
}

want = {
    "name": "alice",
    "age": ...,
    "widgets": {
        "thing1": {
            "size": "large",
            "count": 10,
        },
        "thing2": {
            "size": "medium",
            "count": ...,
        },
        ...: None,
    },
}

print(Nearly(have_matches) == want)
print(Nearly(have_does_not_match) == want)
