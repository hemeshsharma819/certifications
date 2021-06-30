#!/usr/bin/env python
# coding: utf-8

# In[1]:


def madlib() :
    print("Hey there! This is Hemesh, I've prepared a madlib for you from Harry Potter and the Philosopher's Stone.\n    I hope you'll enjoy this little game and also refer it to your friends.")
    
    a = input("If you want to start this game then type 1 : ")
    
    if a == '1' :
    
        my_name = input("\n\nEnter your name : ")
        teacher = input("Enter any of your unfavourite teacher's name : ")
        jerk = input("Enter name of the guy you don't like : ")
        friend1 = input('Enter name of your friend : ')
        friend2 = input("Enter name of your another friend : ")
        f_friend = input("Enter name of your female friend : ")
        personality = input("Enter name of a personality : ")
        my_team = input("Enter your team's name : ")
        other_team = input("Enter name of other team : ")
        jerk_f1 = input("Enter jerk's friend's name : ")
        jerk_f2 = input("Another friend of that jerk : ")
        mystery_man = input("Now tell the name of a mysterious man : ")
    
        print(f'''\n\n{my_name} finds it hard to forget the image of his parents. Quidditch practice continues on even harder and it is revealed that {teacher} will referee the next match. {jerk} performs a leg-locker curse on {friend1}, and to cheer him up, {my_name} tells {friend1} he is "Worth twelve of {jerk}." {my_name} suddenly remembers that he read the name {personality} on a chocolate frog card,        which reminds {f_friend} that she had seen the name in a book she picked up from the library, and the team discover that he was a famous alchemist who is the only known maker of the Philosopher's Stone, whose powers include turning any metal to gold and producing the Elixir of Life, a potion that can make the drinker immortal.
        The {my_team} versus {other_team} Quidditch match arrives and {teacher}, who referees the match, is predictably biased, while on the stands {friend2} and {friend1} get into a scuffle with {jerk}, {jerk_f1}, and {jerk_f2} after {jerk} made some rude comments towards the players of their house's team as well as both of them. {my_name} catches the snitch and wins the match under five minutes, though {friend2} did not see this due to fighting {jerk}, and {friend1} is sent to the hospital wing due to the injuries he sustained from fighting both {jerk_f1} and {jerk_f2}. Later, {my_name} notices and follows {teacher} into the Forbidden Forest by broomstick where he meets {mystery_man} and they speak of the Philosopher's Stone. {my_name} thinks that {teacher} is trying to force {mystery_man} to help him get the stone so he can get rich, to the alarm of both {friend2} and {f_friend} who fear {mystery_man} will talk.''')
        
        
    else :
        print("It was nice talking to you.\nGood bye and take care.")
        
madlib()


# In[ ]:




