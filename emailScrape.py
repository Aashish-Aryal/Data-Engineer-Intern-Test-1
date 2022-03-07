import json
import re

# read file with context manager to a string
with open(
    "websiteData.txt", encoding="utf8"
) as f:  # Unicode Transformation Format 8-bit
    f_content = f.read()

# extract email from the string to a list
email_list = re.findall(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", f_content
)
l = len(email_list)

# occurance
occ = []
for i in range(l):
    c = 0
    for j in range(l):
        if email_list[i] == email_list[j]:
            c += 1
    occ.insert(i, c)

# find the type of the email
email_type = []
for k in range(l):
    username = email_list[k].split("@")  # split the username of the email
    if username[0].count(".") > 0:
        email_type.insert(k, "Human")
    elif len(username[0]) < 8:
        email_type.insert(k, "Non-Human")
    else:
        email_type.insert(
            k,
            "Type not defined because length of the username is not less than 8 and is not 'Human'.",
        )

result = {
    email_list[i]: {"Occurance": occ[i], "EmailType": email_type[i]} for i in range(l)
}

json_result = json.dumps(result)
with open(
    "result.json", "w", encoding="utf8"
) as r:  # Unicode Transformation Format 8-bit
    r_content = r.write(json_result)
