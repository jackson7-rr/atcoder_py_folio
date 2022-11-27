from sys import stdin 
import re
s = stdin.readline().strip()
t = stdin.readline().strip()
def main(s,t):
    if re.search(t,s):
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main(s,t)