from sys import stdin 
h, m =  map(int, stdin.readline().strip().split())
def main(h,m):
    sh = h
    sm = m
    sh = (h //10)*10 + (m // 10)
    sm = (h % 10)*10 + (m % 10)


    while sh > 23 or sm > 59:
        m += 1
        if m ==60:
            m = 0
            h +=1
            if h == 24:
                h = 0
        sh = h
        sm = m
        sh = (h //10)*10 + (m // 10)
        sm = (h % 10)*10 + (m % 10)
    print(h,m)

if __name__ == '__main__':
    main(h,m)