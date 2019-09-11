from datetime import time
tm = "2:30"
print(time(int(tm.split(':')[0]), int('12:30'.split(':')[1])).strftime("#%I:%M %p").lower().replace('m','.m').replace('#0','').replace('#',''))