import time
import datetime
from pygame import mixer


def getdate():
    """Function to get time and date for logs"""
    import datetime
    return datetime.datetime.now()


def play_music(string):
    """Function to play music"""
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load(f'{string}.mp3')

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()


def log_activity(string):
    """Function to log activities into the text files"""
    update = ''
    file_open = True
    f = open("Logs.txt", "a")
    if string == 'drank':
        update = "Drank one glass of water\n"
    elif string == 'eydone':
        update = "Eye exercises done\n"
    elif string == 'exdone':
        update = "Physical activity done\n"
    else:
        file_open = False

    if not file_open:
        pass
    else:
        dt = getdate()
        try:
            f.write(f'[{dt}] {update}')
            print('Log successfully updated')
            f.close()
        except Exception as e:
            print(e)


def reminder(string, user_input=None):
    """Function that reminds user, plays music and calls log_activity()"""
    if string == 'water':
        play_music('water')
        print("Time to drink water!")
        user_input = input("Did you drink a glass of water?\nIf yes, then enter the keyword \"drank\" ")
        user_input = user_input.lower()
        while user_input != 'drank':
            user_input = input("Wrong keyword entered! Enter the keyword \"drank\" ")
            user_input = user_input.lower()
        mixer.music.stop()
        log_activity('drank')
    elif string == 'eyes':
        play_music('eyes')
        user_input = input("Did you rest your eyes and do the eye exercise?\nIf yes, then enter keyword \"eydone\" ")
        user_input = user_input.lower()
        while user_input != 'eydone':
            user_input = input("Wrong keyword entered! Enter the keyword \"eydone\" ")
            user_input = user_input.lower()
        mixer.music.stop()
        log_activity('eydone')
    elif string == 'physical':
        play_music('physical')
        user_input = input("Did you stand up and do the stretches?\nIf yes, then enter keyword \"exdone\" ")
        user_input = user_input.lower()
        while user_input != 'exdone':
            user_input = input("Wrong keyword entered! Enter the keyword \"exdone\" ")
            user_input = user_input.lower()
        mixer.music.stop()
        log_activity('exdone')
    else:
        pass


def check_time():
    """Function to check whether present time is within working hours"""
    now = datetime.datetime.now()
    today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)

    if now < today9am:
        time_diff = today9am - now
        print(f"Working hours not yet started. {time_diff} left")
        time.sleep(time_diff.seconds)
        check_time()
    elif now > today5pm:
        print("Working hours over!")
        print("Come back tomorrow at 9 AM")
    elif now == today9am:
        alarm_interval(0)
    elif today9am < now < today5pm:
        time_diff = now - today9am
        x = time_diff.seconds // 900
        time_left = 900 - (time_diff.seconds % 900)
        print(f"Next alarm in {time_left} seconds")
        time.sleep(time_left)
        alarm_interval(x+1)
    else:
        pass


def alarm_interval(n):
    """Function checks for clashes between activities"""
    now = datetime.datetime.now()
    today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)

    # only water reminder, no clashes
    if n % 2 == 0 and (n - 1) % 3 != 0:
        reminder('water')

    # only eyes exercise reminder, no clashes
    elif n % 2 != 0 and (n - 1) % 3 != 0:
        reminder('eyes')

    # water reminder and physical activity reminder coincide
    elif n % 2 == 0 and (n - 1) % 3 == 0:
        reminder('water')
        reminder('physical')

    # eyes exercise reminder and physical activity reminder coincide
    elif n % 2 != 0 and (n - 1) % 3 == 0:
        reminder('eyes')
        reminder('physical')

    else:
        pass

    if now <= today5pm:
        pass
    else:
        print("Work over for the day. Have a nice evening!")
        exit()

    check_time()


def learn_more():
    """Function to print the purpose of the program"""
    print("-> This program is designed to help you take breaks while coding")
    print("-> Reminder to drink 1 glass of water, every thirty minutes, starting from 9 AM")
    print("-> Reminder to exercise the eyes, every thirty minutes, starting from 9:15 AM")
    print("-> Reminder to exercise the body, every forty-five minutes, starting from 9:15 AM")
    print("-> Program runs from 9AM to 5PM only")


def menu():
    """Function acts as a menu for the user"""
    print("----------Healthy Programmer----------")
    try:
        n = int(input("Press 1 to Start\nPress 2 to Learn More\nPress 3 to Quit "))
        if n == 1:
            check_time()
        elif n == 2:
            learn_more()
        else:
            exit()
    except Exception as e:
        print(e)
        menu()


if __name__ == '__main__':
    menu()
