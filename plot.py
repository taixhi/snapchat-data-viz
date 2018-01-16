import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

def plot(snaps_count):
	font = {'family' : 'Helvetica',
        'weight' : 'bold',
        'size'   : 7}
	plt.rc('font', **font)
	plt.barh(range(len(snaps_count)), list(snaps_count.values()), align='center', alpha=0.5)
	plt.yticks(range(len(snaps_count)), list(snaps_count.keys()))
	plt.xlabel('Snaps Sent/Reveived')
	plt.title('Snaps Sent/Reveived per user in the past month')
	plt.axis('tight')
	plt.show()