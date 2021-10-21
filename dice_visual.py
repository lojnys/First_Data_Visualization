from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two Dice

die_1 = Die()
die_2 = Die()

# we want to make a list of result (sum of two dice)

results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = []

for value in range(2, max_result+1):    
# Because the lowest value possible is 2 and the maximum value is max_result
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize 

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': "Frequency Result"}
my_layout = Layout(title='Results of rolling two D6 1000 times',
	xaxis=x_axis_config,
	yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')