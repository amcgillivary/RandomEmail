from lxml import html
import requests
import datetime

  
'''Currently not functioning: command line arguments to tell how much time is left'''
# parsing the argument --time_left to return the amount of time left on the address
#parser = argparse.ArgumentParser(description='Getting a random 10 minute email address')
#parser.add_argument('--time_left', help='returns the amount of time left on the address', action="store_true")
#args = parser.parse_args()
#if args.time_left:
#  get_time()

# loading the 10minutemail.com page catching the max connection exceeded error
try:
  page = requests.get('https://www.10minutemail.com/10MinuteMail/index.html?dswid=-6922')
  
  # starting the time when the user's email address is instantiated
  hour = datetime.datetime.now().time().hour
  minute = datetime.datetime.now().time().minute
  second = datetime.datetime.now().time().second
  if hour > 12:
    if second < 10:
      start_time = str(hour-12) + ":" + str(minute) + "." + "0" + str(second) + "pm"
    else:
      start_time = str(hour-12) + ":" + str(minute) + "." + str(second) + "pm"
  else:
    if second < 10:
      start_time = str(hour) + ":" + str(minute) + "." + "0" + str(second) + "am"
    else:
      start_time = str(hour) + ":" + str(minute) + "." + str(second) + "am"
except requests.exceptions.ConnectionError:
  page.status_message = "Connection refused"
  print "Connection Refused"

# saving the HTML in tree form
html_tree = html.fromstring(page.content)

# saving the email address from the tree to a string
email_add = str(html_tree.xpath('//div[@class="mail-address"]/input/@value'))

# printing the user's email
print 'This is your email ', email_add, " created at: ", start_time, ".  You have 10 minutes."

