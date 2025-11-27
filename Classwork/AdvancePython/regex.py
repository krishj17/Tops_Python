import re

# print(re.match("x","xello")) # matches only at starting position of string.
# print(re.match("x","helxo"))

# print(re.search("ll","hello")) # searches anywhere in string. returns first occurance only.

# print(re.findall("ll", "hello hell")) # returns multiple search results.

# a = re.finditer("ll", "hello hell") # returns multiple search result indexes
# for i in a:
#     print(i)

# print(re.sub("ll", "x", "hello hell")) # replaces the string with value provided.

# print(re.split("h", "hello how are you hi")) # splits the string into list or sub strings.


# Regex Example:
# no = "1234567890"
# ans = re.match("^[0-9]{10}$",no)
# print(ans)

# check password (1 lower, 1 upper, 1 number, 1 special, min len 10)
password = "krKshj2asdfd@"
checkpass = re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@\$%&*])[A-Za-z\d!@\$%&*]{10,}$', password)
print(checkpass)
