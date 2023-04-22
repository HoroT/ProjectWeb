import json

with open("default_points.json", encoding="utf-8") as f:
    d = json.load(f)


def sorter(v):
    if v["name"].split()[-1].isdigit():
        return int(v["name"].split()[-1])
    return 0


nd = sorted(d.get("points"), key=sorter)

with open("default_points.json", "w", encoding="utf-8") as f:
    json.dump({"points": nd}, f, ensure_ascii=False)
