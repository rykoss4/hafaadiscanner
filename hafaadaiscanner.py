import time, socket


from art import *

# Greeting banner
tprint("HAFA ADAI!", "rnd-med")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input('IP or site: ')
# Scanning has started
target_ip = socket.gethostbyname(target)
print('Examining the guarry:', target_ip)


# This line is the function for scanning ports.
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False


start = time.time()
# This line scans ports 0–8 and indicates if they are open or closed.

for port in range(8):

    if port_scan(port):

        print(f'port {port} is open')
    else:

        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end - start:.2f} seconds')

# Sample end message
tprint("Good-Bye!!", "rnd-med")

