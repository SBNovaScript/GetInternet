from urllib import request, error
import webbrowser
import threading
import time
import argparse

searchedItems = 0

def checkinternet():
    try:
        data = request.urlopen("http://www.google.com", timeout=15)
        return 1
    except error.URLError as e:
        return 0


def allowSearching(browser):
    global searchedItems
    connected = 1
    while connected:
        message = input("> ")
        if message == "!quit":
            connected = 0
            searchedItems = -1
        else:
            if browser != "yahoo":
                webbrowser.open("www.{}.com/search?q={}".format(browser,message))
            else:
                webbrowser.open("www.search.yahoo.com/search?q={}".format(message))




def printnums():
    global searchedItems
    prev_search = searchedItems
    while searchedItems != -1:
        time.sleep(1)
        if searchedItems > prev_search:
            print("\nLooks like we have searched another item. \n> ", end='')
            prev_search = searchedItems


def argparser():
    parser = argparse.ArgumentParser(description="Search tool.")
    parser.add_argument("-w",  type=str, default="google", help="Your desired web browser. google/bing/yahoo/duck")
    args = parser.parse_args()
    return args.w

if __name__ == "__main__":
    user_args = argparser()

    print("Checking Google.com ...")
    connected_result = checkinternet()
    if connected_result == 1:
        print("You are connected!")
        print(user_args)
        try:
            thread1 = threading.Thread(target=allowSearching, args=(user_args,))
            thread2 = threading.Thread(target=printnums)

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()
        finally:
            print("Done.")

    else:
        print("you are not connected.")

