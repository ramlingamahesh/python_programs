
#1. Using datetime library
from datetime import datetime
'''
date_string = '06-02-2018'
date_object = datetime.strptime(date_string, '%d-%m-%Y')
print(date_object)'''


# 2. Using external library dateutil – parser   update using this in cmd ‘pip install python-dateutil
'''
from dateutil import parser

date_string = 'feb 06 2018 08:00PM'
date_object = parser.parse(date_string)
print(date_object)
'''


#3. Using external library timestring    ::  ‘pip install timestring’

'''
import timestring

date_string = 'feb 06 2018 08:00PM'
date_object = timestring.Date(date_string)
print(date_object)
'''

#4. Using external library dateparser     ‘pip install dateparser’

import dateparser
date_string = '02/06/2018'
date_object = dateparser.parse(date_string)
print(date_object)