#서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

import datetime

d = datetime.datetime.now()
print (d.strftime("%Y-%m-%d"))