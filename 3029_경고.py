h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

now = h1*60*60 + m1*60 + s1
throw = h2*60*60 + m2*60 + s2

time = throw - now if throw > now else throw - now + 24 * 60 * 60 
# 86400 = 60 * 60 * 24 

h = time // 60 * 60 # 1 hour -> 60m * 60s
m = time // 60 % 60 
s = time % 60

print("%02d:%02d:%02d" % (h, m, s)) 