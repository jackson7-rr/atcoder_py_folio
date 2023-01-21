from sys import stdin 
n = int(stdin.readline().strip())
s = stdin.readline().strip()

def main(n,s):
    print(s.replace('na', 'nya'))
if __name__ == '__main__':
    main(n,s)