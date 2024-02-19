# Python Exception Message
try:
    v = 1/0
except Exception as e:
    print(type(e).__name__, e)

