name = "Ben"
fav_langauge = "python" 

if name == "Ben":
    if fav_langauge == "python":
        print(f"{name} is a fullstack Web Developer and loves {fav_langauge}.")
    else:
        print("Not Ben Doesn't love python")
else:
    print("Not Ben Doesn't love python")

# WITH TERNARY OPERATOR
print(f"{name} is a fullstack Web Developer and loves {fav_langauge}." if name == "Ben" and fav_langauge == "python" else "Not Ben Doesn't know python")