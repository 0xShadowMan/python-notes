star1 = "Bob"

star2 = "Alex"

post = input("Enter your post: ")

star1 = star1.lower()
star2 = star2.lower()
post = post.lower()

if star1 in post:
    print("You have mentioned Bob in your post.")

elif star2 in post:
    print("You have mentioned Alex in your post.")

else:
    print("You have not mentioned any star in your post.")