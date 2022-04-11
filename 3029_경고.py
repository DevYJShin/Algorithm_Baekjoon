def main():
    h, m, s = map(int, input().split(":"))
return h*3600+m*60+s ## runtime error

now, throw = main(), main()
time = now - throw + 86400 * (now >= throw) # 24h = 86400s
print('%02d:%02d:%02d' %(time//3600, time%3600, time%3600%60))

