def calculate_score(elements):
    total_score = 0
    for name, base, goes in elements:
        sorted_goes = sorted(goes)
        trimmed = sorted_goes[1:-1]
        avg_goe = sum(trimmed) / len(trimmed)
        element_score = base + (avg_goe * 0.1 * base)
        total_score += element_score
        print(f"{name}: {element_score:.2f}")
    return round(total_score, 1)


elements = [
    ("Triple Flip",            9.7,  [3, 2, 3, 3, 2, 4, 3, 2, 3]),
    ("Triple Lutz+Toe Combo", 12.5,  [4, 5, 4, 5, 5, 4, 4, 3, 4]),
    ("Triple Salchow",         7.0,  [2, 3, 2, 2, 3, 2, 2, 3, 2]),
    ("Triple Loop",            6.0,  [3, 3, 2, 4, 3, 3, 2, 3, 2]),
    ("Step Sequence",          3.3,  [4, 4, 4, 4, 3, 3, 4, 3, 4])
]

print("Total Score:", calculate_score(elements))
