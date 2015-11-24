import datetime
now = datetime.datetime.now()
print( now )
months = ('-error-', 'January','February','March','April','May','June', 'July','August','September','October','November','  December')
print( months[now.month] )

for x in months:
    print x
