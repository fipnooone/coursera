import functools

print(
    functools.reduce(
        lambda l, c: l * c,
        list(
            map(
                lambda x: int(x) ** 5,
                input().split()
            )
        ),
    )
)
