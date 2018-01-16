from collections import OrderedDict
from operator import itemgetter
from bs4 import BeautifulSoup
from helpers import *
from plot import *
from snap import *


# Constants
snap_hitory_html = "mydata/snap_history.html"

# Make bs4 history object for parsing
with open(snap_hitory_html) as fp:
	history = BeautifulSoup(fp, "html.parser")

# Arrays of Snap objects with sender/recepient details etc.
received_snaps = []
sent_snaps = []

def snaps_from_table_rows(table):
	snaps = []
	for row in table:
		data = row.find_all('td')
		if len(data) == 4:
			snaps.append(Snap(data[0].contents[0].strip('\n').strip(' ').strip('\n'),
									   data[1].contents[0].strip('\n').strip(' ').strip('\n'),
									   data[2].contents[0].strip('\n').strip(' ').strip('\n'),
									   data[3].contents[0].strip('\n').strip(' ').strip('\n')))
	return snaps

# Mutate received_snaps
received_snaps = snaps_from_table_rows(history.table.tbody.find_all('tr'))
sent_snaps = snaps_from_table_rows(history.find_all('table')[1].tbody.find_all('tr'))

received_snaps_count = {}
sent_snaps_count = {}

# Create "counts" dictionary where {username: received_snaps_count}
print('NUMBER OF SNAPS RECEIVED:')
print(len(received_snaps))
for snap in received_snaps:
	if snap.sender in received_snaps_count:
		received_snaps_count[snap.sender]+= 1
	else:
		received_snaps_count[snap.sender] = 1

# Create "sent_counts" dictionary where {username: sent_snaps_count}
print('NUMBER OF SNAPS SENT:')
print(len(sent_snaps))
for snap in sent_snaps:
	if snap.recepient in sent_snaps_count:
		sent_snaps_count[snap.recepient]+= 1
	else:
		sent_snaps_count[snap.recepient] = 1

# Prints received and sent snaps
print("TOTAL SNAPS SENT AND RECEIVED")
print(sort_by_highest_value(merge(received_snaps_count,sent_snaps_count)))
plot(merge(received_snaps_count,sent_snaps_count))

