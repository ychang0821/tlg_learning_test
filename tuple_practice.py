import time

tuple_record = ('eth0', 'AA:BB:CC:DD:11:22', '192.168.0.1', '5060', 'UDP')

print(tuple_record)

print(tuple_record * 2)

print(tuple_record[0:2])

print(tuple_record[1])

records = ['eth0', 'AA:BB:CC:DD:11:22', '192.168.0.1', '5060', 'UDP']

# list is mutable, tuple is immutable
#tuple_record.
#records.

localTime = time.localtime(time.time())
print(localTime)
print(localTime[0:2])  # year and month
print('The year is {}'.format(localTime[0]))  # the year is ...
print('The minutes is', localTime[4])        # the minute is ...
print('{}/{}/{}'.format(localTime[0],localTime[1],localTime[2]))  # year/month/date

