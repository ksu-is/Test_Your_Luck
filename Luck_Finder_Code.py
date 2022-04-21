from tkinter import Y


best_luck = 100
worst_luck = 0
kinda_luck = 50
mild_luck = 25
better_luck = 75


def zodiac_luck():
    zodiac = input("What is your Zodiac Sign? (Aries, Leo, Sagittarius, Taurus, Virgo, Capricorn, Gemini, Libra, Aquarius, Cancer, Scorpio, Pisces): ")
    if zodiac == "Aries":
        return (kinda_luck)
    if zodiac == "Taurus":
        return (mild_luck)
    if zodiac == "Gemini":
        return (mild_luck)
    

def month_luck():
    month = str(input("What is the month? (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec): "))

def day_of_week_luck():
    day_of_week = str(input("What is the day of the week? (Sun, Mon, Tue, Wed, Thu, Fri, Sat): "))

def day_luck():
    day = int(input("What is the day of the month? (1-31): "))

def season_luck():
    season = str(input("What is the season? (Spring, Summer, Fall, Winter): "))

def time_luck():
    time = int(input("what is the time? (12 hour scale with no ':' ex. 11:30 is 1130): "))

def task_luck():
    task = str(input("Is your task simple or complex? (simple=buying a lottory ticket/ complex=choosing to buy a house): "))

def feeling_luck():
    feeling = str(input("Are you feeling lucky? (y/n): "))
    
print(zodiac_luck())