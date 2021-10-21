from plotly.graph_objs import Bar, Layout
from plotly import offline 

from die import Die

die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)

print(results)


# Analyzing the results

frequencies = []

for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)


# Visualize

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]       # actual plotting 


# Configuration
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# Each axis configuration goes into Layout() function
my_layout = Layout(title='Results of rolling one D6 1000 times', 
	xaxis=x_axis_config, 
	yaxis=y_axis_config)

# Putting all together
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')