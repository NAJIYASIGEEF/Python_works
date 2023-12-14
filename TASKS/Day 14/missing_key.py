# 3. Write a program to handling missing keys
given_keys = {"department": "cs","college":"abc","semester": 8}

missing_keys = ["college","subjects","fee","department"]


for key in missing_keys:
    value = given_keys.get(key, "The key is missing")
    print(f"The value for key '{key}' is: {value}")