import json
with open(r"Data\Emoji.json", encoding="utf8") as F:
    JF = F.read()
    Json = json.loads(JF)
    GET = Json["default"]
    MEDIA = GET["Media"]
print(MEDIA["Prev"])
