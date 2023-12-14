insta_users={"mohanlal","prithvi","dq","vijay","fahad","lalu","sureshgopi"}
mohanlal_following={"prithvi","vijay","lalu"}

dq_friends={"prithvi","fahad","sureshgopi","lalu"}

suggestions=insta_users.difference(mohanlal_following)
# print(diff)

suggestions.remove("mohanlal")
# print(suggestions)

mutual_frieinds=mohanlal_following.intersection(dq_friends)
# print(mutual_frieinds)



