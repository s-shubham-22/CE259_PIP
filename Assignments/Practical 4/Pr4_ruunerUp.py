n = int(input())
ranks = [int(item) for item in input().split(" ")]
ranks_dict = list(dict.fromkeys(ranks))
ranks_dict.sort()

print(ranks_dict[-2])

# Github Link: https://github.com/s-shubham-22/20CE123_CE259_PIP