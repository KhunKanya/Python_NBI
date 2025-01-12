from datetime import datetime, timedelta
dt = datetime.now()
future = timedelta(days=7)
#calculated date
print(dt + future)
