#!/bin/python3

import sys
from datetime import datetime

time = input().strip()
originalTime = datetime.strptime(time, "%I:%M:%S%p")
newTime = datetime.strftime(originalTime, "%H:%M:%S")
print(newTime)