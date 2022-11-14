from sys import stdin 
on = ['H', 'D', 'C', 'S']
tw = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
def main():
    n = int(stdin.readline().strip())
    s = [stdin.readline().strip() for _ in range(n)]
    seen = set()
    for i in range(n):
        if s[i][0] not in on:
            print('No')
            exit()
        elif s[i][1] not in tw:
            print('No')
            exit()
        elif s[i] in seen:
             print('No')
             exit()
        seen.add(s[i])
    print('Yes')
if __name__ == '__main__':
    main()