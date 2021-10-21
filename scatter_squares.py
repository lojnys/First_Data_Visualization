import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

#x_values = [n for n in range(1, 6)]
#y_values = [x**2 for x in x_values]

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

ax.scatter(x_values, y_values, c='red', s=10)  
#parameter s is for size of the points
#parameter c is for color of the points

#labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1100000]) # domain: [0, 1100], range: [0, 1100000]
 

plt.show()

'''
plt.savefig('squares_plot.png', bbox_inches='tight')

if want to directly save the graph into an image
'''