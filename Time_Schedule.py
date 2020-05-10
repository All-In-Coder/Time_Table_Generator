from datetime import datetime




TIME = [
	"11:00 AM -12:30 PM",
	"2:00 PM - 5:00 PM",
	"5:00 PM - 7:30 PM",
	"8:00 PM - 9:00 PM",
	"10:30 PM - 1:00 AM",
	"1:00 Am - 2:00 AM" 
]



DAY = [
	'MONDAY',
	'TUESDAY',
	'WEDNESDAY',
	'THURSDAY',
	'FRIDAY',
	'SATURDAY',
	'SUNDAY'
]

TOPICS = [
	'String',
	'Trie',
	'Data Science',
	'Bitwise',
	'Codeforces',
	'Codechef',
	'Dynamic Programming',
	'Graph InterviewBit',
	'LeetCode',
	'Python OOPS',
	'Python Project',
	'Tree Data Structure',
	'MOS ALGORITHM,SQRT DECOMPOSITION',
	'CODECHEF AUGUST 2019',
	'CODECHEF JANAURY 2020',
	'DATA Science PROJECT',
	'JAVA',
	'SQL',
	'NODE JS',
	'PYTHON 7 HOURS'
]



def printDAY():
	return(DAY[datetime.weekday(datetime.now())])
