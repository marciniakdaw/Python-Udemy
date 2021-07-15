print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1=name1.lower()
name2=name2.lower()

t_letter_number=name1.count("t")+name2.count("t")
r_letter_number=name1.count("r")+name2.count("r")
u_letter_number=name1.count("u")+name2.count("u")
e_letter_number=name1.count("e")+name2.count("e")

true_resoult=(t_letter_number+r_letter_number+u_letter_number+e_letter_number)*10

l_letter_number=name1.count("l")+name2.count("l")
o_letter_number=name1.count("o")+name2.count("o")
v_letter_number=name1.count("v")+name1.count("v")

love_resoult=l_letter_number+o_letter_number+v_letter_number+e_letter_number

total_score=true_resoult+love_resoult

if total_score <10 or total_score>90:
  print(f"Your score is {total_score}%, you go together like coke and mentos.")
elif total_score >40 and total_score < 50:
  print(f"Your score is {total_score}%, you are alright together.")
else:
  print(f"Your score is {total_score}%.")
