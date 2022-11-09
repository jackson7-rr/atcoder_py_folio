from sys import stdin 
import math
def main():
    a, b, c = map(int, stdin.readline().strip().split())
    if a < c**b:
        #a, b, cが全て正の整数であることから，log2a blog2cと (a,c**b)の大小関係が同じになると推測した．
        #最初は純粋にlog関数を用いたが，10進数を2進数で表現しようとすると有限個の桁で表すことができないために誤差が生じ不正解になるケースがある
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()