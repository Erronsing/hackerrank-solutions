twelve_time = raw_input()
split_time = twelve_time.split(':')
hour = int(split_time[0])
ampm = twelve_time[-2:]
if ampm == 'PM' and hour!=12:
    hour = int(hour)+12
    if hour == 24:
        hour = '00'
        split_time[0] = hour
    else:
    	split_time[0] = str(hour)
elif ampm =='AM' and hour==12:
	hour = '00'
	split_time[0] = hour
#split_time[0]=str(hour)
new_time=':'.join(split_time)[:-2]
print new_time