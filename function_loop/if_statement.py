is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male or Tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not Tall")
