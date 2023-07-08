def main():
    t = int(input())
    while t > 0:
        n = int(input())
        s = input()
        dif = set()
        used = {}
        for i in range(n):
            dif.add(s[i])
        ans = n + len(dif)
        print(ans)
        t -= 1

if __name__ == "__main__":
    main()
