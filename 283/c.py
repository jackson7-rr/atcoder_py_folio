from sys import stdin 
s = stdin.readline().strip()
def main(s):
    tz = s.count('00')
    sl = len(s)
    print(sl-tz)
if __name__ == '__main__':
    main(s)