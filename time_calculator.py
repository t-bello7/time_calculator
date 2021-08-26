def add_time(start, duration, optional=''):
  optional = optional.capitalize()
  days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']

  #calculate the addition 
  check_ending = start.strip('1234567890:')
  start = start.strip(' AMP')

  index_col_start =  start.index(':')
  index_col_duration = duration.index(':')

  start_hours = int(start[0:index_col_start])
  start_mins = int(start[index_col_start+1:]) 
  duration_hours = int(duration[0:index_col_duration])
  duration_mins = int(duration[index_col_duration+1:])

  duration_total_mins = (duration_hours * 60) + duration_mins
  result_min = start_mins + duration_total_mins
 
  result_hours = (result_min // 60) + start_hours 

  #check format
  count = 0
  if result_hours > 12:
    result_hours = result_hours - 12
    count += 1

 
  while result_hours >= 24:
    count += 1 
    result_hours = result_hours - 24
  if result_hours == 0:
    result_hours = 12
  result_min = (result_min % 60)

  if optional == '' and count == 0:
    answer = f'{result_hours}:{result_min} {check_ending}'
  else:
    answer = f'{result_hours}:{result_min} {check_ending}, {optional} ({count} days later)'
  return answer

print(add_time('3:00 PM', "3:10"))
print(add_time('11:30 AM', "2:32", "Monday"))
print(add_time('11:43 AM', "00:20"))
print(add_time('10:10 PM', "3:30"))
print(add_time('11:43 PM', "24:20", "tueSday"))
print(add_time('6:30 PM', "205:12"))




