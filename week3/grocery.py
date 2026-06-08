grocery = []

while True:
    try:
        item = input().upper().strip()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except (EOFError, KeyboardInterrupt):
        sorted_list = sorted(list(grocery.items()))
        sorted_dict = dict(sorted_list)
        for i in sorted_dict:
            print(f"{sorted_dict[i]} {i}")

        break
    except KeyError:
        pass