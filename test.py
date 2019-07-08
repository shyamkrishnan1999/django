from disper import cal

def Test_percentage_calculation():
	per=cal(100,10)
	assert per==10
	a="10"
	b="0"
	per=cal(a,b)
	assert per=="Invalid argument"

