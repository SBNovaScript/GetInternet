from urllib import request, error
import webbrowser
import threading
import time

searchedItems = 0

def checkinternet():
    try:
        data = request.urlopen("http://www.google.com", timeout=15)
        return 1
    except error.URLError as e:
        return 0


def allowSearching():
    global searchedItems
    connected = 1
    while connected:
        message = input("> ")
        if message == "!quit":
            connected = 0
            searchedItems = -1
        else:
            webbrowser.open("www.google.com/search?q=" + message)
            searchedItems += 1



def printnums():
    global searchedItems
    prev_search = searchedItems
    while searchedItems != -1:
        time.sleep(5)
        if searchedItems > prev_search:
            print("\nLooks like we have searched another item. \n> ", end='')
            prev_search = searchedItems


if __name__ == "__main__":
    print("Checking Google.com ...")
    connected_result = checkinternet()
    if connected_result == 1:
        try:
            print("You are connected!")
            thread1 = threading.Thread(target=allowSearching)
            thread2 = threading.Thread(target=printnums)

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()
        finally:
            print("Done.")

    else:
        print("you are not connected.")

