import pyautogui as pg
import webbrowser as wb
import time as t

points = 0 

show = pg.prompt ("What is your favorite show? ")

if show == "The Flash":
    wb. open ("https://www.youtube.com/watch?v=Act0SdlYPWE")
    points +=4
    t.sleep(3)
    pg.alert ("that is a really good show!")
elif show == "The Office":
    wb. open ("https://www.youtube.com/watch?v=KRxPEiHxfgg")
    points +=3
    t.sleep(3)
    pg.alert ("I love dwight")
elif show == "Parks and rek":
    wb. open ("https://www.youtube.com/watch?v=hYM-FbO9yk0")
    points +=3
    t.sleep(3)
    pg.alert ("I don't like that show")
elif show == "Black-ish":
    wb. open ("https://www.youtube.com/watch?v=BOTq38k6Aiw")
    points +=2
    t.sleep(3)
    pg.alert ("cool")
elif show == "Arrow":
    wb. open ("https://www.youtube.com/watch?v=MBPclPXz9p0")
    points +=3
    t.sleep(3) 
    pg.alert ("that shows dying")
elif show == "family guy":
    wb. open ("https://www.youtube.com/watch?v=_hI0H0tDh4w")
    points +=3
    t.sleep(4)
    pg.alert ("that show is funny")
else:
    pg.alert ("Your favore show is " + show)
youtuber = pg. prompt ("what is your favorite youtuber? ")

t. sleep(5)

if youtuber == "Lazarbeam":
    wb. open ("https://www.youtube.com/watch?v=VzyR_oo8KjQ")
    points +=5
    t.sleep(3)
    pg.alert ("That's is a great guy ")
elif youtuber == "Lachlen":
    wb. open ("https://www.youtube.com/user/CraftBattleDuty")
    points +=3
    t.sleep(3)
    pg.alert ("that guy is trash")
elif youtuber == "Muselk":
    wb. open ("https://www.youtube.com/watch?v=4KDDENLH3CU")
    points +=1
    t.sleep(3)
    pg.alert ("that guy is old")
elif youtuber == "Ali-a":
    wb. open ("https://www.youtube.com/watch?v=y98De45A94Y")
    points +=1,000
    t.sleep(3)
    pg.alert ("wow")
elif youtuber == "cee-day":
    wb. open ("https://www.youtube.com/watch?v=LM8SWrSOgRY")
    points+=3
    t.sleep(3)
    pg.alert ("your cool")
elif youtuber == "Click":
    wb. open ("https://www.youtube.com/channel/UCELEYV16ItX8pNkg8EuVY7g")
    points+=1
    t.sleep(3)
    pg.alert ("your silly")
else:
    pg.alert ("your favorite game is " + youtuber)
food = pg. prompt ("what is your favorite food? ")

t.sleep(5)

if food == "Pizza":
    wb. open ("https://www.youtube.com/watch?v=lpvT-Fciu-4")
    points+=13
    t.sleep(3)
    pg.alert ("That is a great food ")
elif food == "burger":
    wb. open ("https://www.youtube.com/watch?v=UyPOv-jGNYo")
    points+=14
    t.sleep(3)
    pg.alert ("that food is ok")
elif food == "hot dog":
    wb. open ("https://www.youtube.com/watch?v=pY7hFRg2jvw")
    points+=10
    t.sleep(3)
    pg.alert ("that food is nice")
elif food == "Ice cream":
    wb. open ("https://www.youtube.com/watch?v=5t-IKxx9ttU")
    points+=15
    t.sleep(3)
    pg.alert ("wow")
elif food == "Sushi":
    wb. open ("https://www.youtube.com/watch?v=RW7Rzas5mKI")
    points+=1
    t.sleep(3)
    pg.alert ("ew")
elif food == "Hamburger":
    wb. open ("https://www.youtube.com/watch?v=iM_KMYulI_s")
    points+=8
    t.sleep(3)
    pg.alert ("cool")
else:
    pg.alert ("your favorite food is " + food)
    
movie = pg. prompt ("what is your favorite movie? ")

t.sleep(5)

if movie == "iron man":
    wb. open ("https://www.youtube.com/watch?v=8hYlB38asDY")
    points+=5
    t.sleep(3)
    pg.alert ("that is a really good movie!")
elif movie == "deadpool 2":
    wb. open ("https://www.youtube.com/watch?v=D86RtevtfrA")
    points+=7
    t.sleep(3)
    pg.alert ("I love doug")
elif movie == "Captain America":
    wb. open ("https://www.youtube.com/watch?v=bmWLLempSyI")
    points+=5
    t.sleep(3)
    pg.alert ("I love that movie")
elif movie == "deadpool":
    wb. open ("https://www.youtube.com/watch?v=Sy8nPI85Ih4")
    points+=4
    t.sleep(3)
    pg.alert ("cool")
elif movie == "Iron man 2":
    wb. open ("https://www.youtube.com/watch?v=PcpXmZnJCcM")
    points+=7
    t.sleep(3)
    pg.alert ("that movies is boring")
elif movie == "Avengers Infinity war":
    wb. open ("https://www.youtube.com/watch?v=weeyScuKLqM")
    points+=2,000
    t.sleep(3)
    pg.alert ("that movie is awsome")
else:
    pg.alert ("Your favore movie is " + movie)

t.sleep(5)

subject = pg. prompt ("what is your favorite subject? ")

if subject == "recess":
    wb. open ("https://www.youtube.com/watch?v=4-bMk0067Dk")
    points+=0
    t.sleep(3)
    pg.alert ("that is not a subject!")
elif subject == "Math":
    wb. open ("https://www.youtube.com/watch?v=-wkr_vf18cw")
    points+=2
    t.sleep(3)
    pg.alert ("I love math")
elif subject == "English":
    wb. open ("https://www.youtube.com/watch?v=s1yAmsnC18s")
    points+=1
    t.sleep(3)
    pg.alert ("I don't like english")
elif subject == "Science":
    wb. open ("https://www.youtube.com/watch?v=2L0ZHxcoWhM")
    points+=2
    t.sleep(3)
    pg.alert ("cool")
elif subject == "Latin":
    wb. open ("https://www.youtube.com/watch?v=_enn7NIo-S0")
    points+=7
    t.sleep(3)
    pg.alert ("that subject is dying")
elif subject == "history":
    wb. open ("https://www.youtube.com/watch?v=xuCn8ux2gbs")
    points+=5
    t.sleep(3)
    pg.alert ("that subject is nice")
else:
    pg.alert ("Your favore subject is " + subject)


pg.alert(points)
