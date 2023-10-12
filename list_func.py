lucky_number = [4, 8, 15, 16, 23, 42]
friend = ["Kevin", "Karen", "jim", "Oscar","Toby", "Elorm"]

friend.append("Creap")
friend.insert(2, "Mark")
friend.remove("Elorm")
friend.pop()
friend.count("Jim")
lucky_number.sort()
lucky_number.reverse()
friend2 = friend.copy()
friend.extend(lucky_number)
friend.clear()
print(friend)