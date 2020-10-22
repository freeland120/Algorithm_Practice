import sys

a, b, c = map(int, sys.stdin.readline().split(':'))
d, e, f = map(int, sys.stdin.readline().split(':'))

first_time = a*3600+b*60+c
second_time = d*3600+e*60+f
"3".zfill(5)
if first_time == second_time:
    print('00:00:01')
elif first_time > second_time:
    time = 24*60*60-first_time+second_time
    print(str(time//3600).zfill(2), ':', str((time-(3600*(time//3600)))//60).zfill(2), ':', str(time%60).zfill(2), sep='')
else:
    time = second_time - first_time
    print(str(time//3600).zfill(2), ':', str((time-(3600*(time//3600)))//60).zfill(2), ':', str(time%60).zfill(2), sep='')