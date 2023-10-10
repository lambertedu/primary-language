lucky_number = [4, 8, 15, 16, 23, 42]
friend = ["Kevin", "Karen", "jim", "Oscar","Toby"]
friend.extend(lucky_number)
friend.append("Creap")
friend.insert(2, "Mark")
friend.remove("Elorm")
friend.clear()
friend.pop()
friend.count("Jim")
friend.sort()
lucky_number.reverse()
friend2 = friend.copy()
print(friend)