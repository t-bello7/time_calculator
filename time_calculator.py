def add_time(start, duration, optional=''):
  optional = optional.capitalize()
  days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday']

  # get the indexes 
  index_day = 0
  if optional in days_of_the_week:
    index_day = days_of_the_week.index(optional)
  index_col_start =  start.index(':')
  index_col_duration = duration.index(':')

  #calculate the addition 
  check_ending = start.strip('1234567890: ')
  start = start.strip(' AMP')


  start_hours = int(start[0:index_col_start])
  start_mins = int(start[index_col_start+1:]) 
  duration_hours = int(duration[0:index_col_duration])
  duration_mins = int(duration[index_col_duration+1:])

  duration_total_mins = (duration_hours * 60) + duration_mins
  result_min = start_mins + duration_total_mins
 
  result_hours = (result_min // 60) + start_hours 

  #check format
  
  count_day = 0
  
  if result_hours == 12 and check_ending == 'AM':
    check_ending = 'PM'
  elif check_ending == 'PM' and result_hours == 12:
    check_ending = 'AM'
    index_day += 1

  if result_hours > 12:
    result_hours = result_hours - 12
    cur = result_hours
    if check_ending == 'PM':
      check_ending = 'AM'
      index_day += 1
      count_day += 1
    elif check_ending == 'AM':
      check_ending = 'PM'
 
  while result_hours >= 24:
    count_day += 1 
    if index_day >= 6:
      index_day = 0
    else:
      index_day += 1 
    while cur > 12:
      cur = cur - 12
      if check_ending == 'PM':
        check_ending = 'AM'
      elif check_ending == 'AM':
        check_ending = 'PM'
    result_hours = result_hours - 24
  if result_hours == 0 and check_ending == 'AM':
    result_hours = 12
    check_ending = 'PM'
  elif result_hours == 0 and check_ending == 'PM':
    result_hours = 12
    check_ending = 'AM'
  result_min = (result_min % 60)
  if len(str(result_min)) == 1:
    result_min = '0' + str(result_min)

  if result_hours > 12:
    result_hours = result_hours - 12
    if check_ending == 'PM':
      check_ending = 'AM'
      index_day += 1
      count_day += 1
    elif check_ending == 'AM':
      check_ending = 'PM'
  day = days_of_the_week[index_day]
  

  if optional == '' and count_day == 0 :
    answer = f'{result_hours}:{result_min} {check_ending}'
  elif optional == '' and count_day == 1:
    answer = f'{result_hours}:{result_min} {check_ending} (next day)'
  elif optional == '' and count_day != 1:
    answer = f'{result_hours}:{result_min} {check_ending} ({count_day} days later)'
  elif optional != '' and count_day == 0:
    answer = f'{result_hours}:{result_min} {check_ending}, {day}'
  elif optional != '' and count_day == 1:
    answer = f'{result_hours}:{result_min} {check_ending}, {day} (next day)'
  elif optional != '' and count_day != 1:
    answer = f'{result_hours}:{result_min} {check_ending}, {day} ({count_day} days later)'
  
  return answer


