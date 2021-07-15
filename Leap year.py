year = int(input("Which year do you want to check? "))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print(f"The {year} is leap year.")
    else:
      print(f"The {year} isn't leap year.")
  else:
    print(f"The {year} is leap year.")
else:
  print(f"The {year} isn't leap year.")
