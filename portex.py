# !/usr/bin/env python3
##########thelinuxuxer-choice#################
#############subodha prabash ##########
###########port scanner ######

# importing the necessary packages
import time
import sys
import os


# Function for implementing the loading animation
def load_animation():
    # String to be displayed when the application is loading
    load_str = "loading Portex..."
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0

    while (counttime != 30):

        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

            # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

            # displaying the resultant string
        sys.stdout.write("\r" + res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

    # for windows OS
    if os.name == "nt":
        os.system("cls")

        # for linux / Mac OS
    else:
        os.system("clear")

    # Driver program


if __name__ == '__main__':
    load_animation()
#####end loding######

# colored text and background
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


import socket
import time
import concurrent.futures
import sys

if len(sys.argv) == 1:
    print(f'\nUsage: "python3 portex.py <IP>"\n(Use "-h" option for more info)')
    sys.exit()
if '-h' in sys.argv or '--help' in sys.argv:
    print('''
Example usage: python3 portex.py 192.168.234.234 -p 1-1000 
-h                     To show this message
-p(optional)           The range of ports to scan. (default: 1-65535)''')
    sys.exit()
min_range, max_range = 1, 65535

ip = sys.argv[1]
if '-p' in sys.argv:
    min_range, max_range = sys.argv[sys.argv.index('-p') + 1].split('-')

banner = '''
          +-------------------------------------------------+
          |               _                                 |
          |              /  \                               |
          |             /|oo \      | P O R T E X | I P |   |
          |            (_|  /_)                             |
          |             _`@/_ \    _   | S C A N N E R |    |
          |            |     | \   \\                       |
          |            | (*) |  \   ))    Secret, XX,  LK   |
          |   ______   |__U__| /  \//                       |
          |  / FIDO \   _//|| _\   /   FidoNet 1:617/1337   |
          | (________) (_/(_|(____/                         |
          |                  (SL)                           |
          +-------------------------------------------------+
         =[ PORTEX v1.0.0.1-dev-subodhaprabash-taj0023      ]
+ -- --  =[ A Multi-Threaded Port-Scanner in python3        ]

Portex tip: Example : python3 portex.py www.example.com -p 1-1000
'''
prCyan(banner)


def scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        print(f"Port {str(port).ljust(4)}     OPEN         {socket.getservbyport(port, 'tcp')}")
    except socket.timeout:
        s.close()


def main():
    prGreen("─"*40)
    print(f"Scanning {str(int(max_range) + 1 - int(min_range))} ports in {ip}")
    prGreen("─"*40)
    print("PORT          STATE        SERVICE")
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = [executor.submit(scanner, i) for i in range(int(min_range), int(max_range) + 1)]
        for f in concurrent.futures.as_completed(results):
            f.result()
    end = time.perf_counter()

    prGreen("─"*40)
    print(f"Scanning Took {round(end - start, 2)}s")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
