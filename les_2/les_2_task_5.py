#https://drive.google.com/file/d/1KcYCD6cHMvxzB9i7XrnoOqvJCCrx-Ay-/view?usp=sharing
COLUMN_COUNT = 10
item_count = 0
for i in range(32, 127+1):
    print(f'\t{i}-{chr(i)}', end='')
    item_count += 1
    if item_count == COLUMN_COUNT:
        print()
        item_count = 0
