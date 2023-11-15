import testpy

def sum(a,b):
	return a-b

def test_sum():
	assert  sum(2,3) == 5
	assert  sum('space', 'line') =='spaceline'
