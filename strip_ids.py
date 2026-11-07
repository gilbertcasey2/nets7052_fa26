import sys, json
nb = json.load(sys.stdin)
for cell in nb.get("cells", []):
    cell.pop("id", None)
json.dump(nb, sys.stdout, indent=1)
