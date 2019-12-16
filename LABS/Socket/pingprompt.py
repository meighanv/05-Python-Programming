import subprocess

def main():
    ping()

def ping():
    targ = input('What address would you like to ping?\n')
    count = input(f'How many times would you like to ping {targ}?\n')
    data = subprocess.Popen(['ping', '-c', count, targ ], stdout = subprocess.PIPE)
    output = data.communicate()
    formatted = str(output).split('\n')
    for i in formatted:
        print(i)

main()
