import time
import random
import datetime
import sys

print("The current time is ", time.time())
# begin_time = time.time()
# time.sleep(1)
# end_time = time.time()
# print("Finish at ", end_time - begin_time)

# reflect to original time execute of program
l_with_numbers = [random.randint(1, 100) for _ in range(30)]
print(sys.getsizeof(l_with_numbers))
print(f'{time.perf_counter():.2f}')

# human readable time
time_now = time.time()
print(time.ctime(time_now + 20))

now = time.localtime()
print(now.tm_hour, ':', now.tm_min)
print(time.strftime('%H:%M:%S', now))

check = time.strptime('19,34,00', '%H,%M,%S')
print(time.strftime("%H:%M:%S", check))
print(time.tzname)
