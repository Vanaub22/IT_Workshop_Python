# Write a script in Python for Normal Data Point clustering
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
x=list(map(int,input('Enter the x-coordinates for the scatter plot separated by spaces:').split()))
y=list(map(int,input('Enter the y-coordinates for the scatter plot separated by spaces:').split()))
# I am putting the following points as input
# x=[1,2,3,4,5,6,7]
# y=[-1,-2,-3,0,9,7,5]
plt.scatter(x,y)
plt.title('Scatter plot for user-input data:')
plt.show() #displaying thee generated scatter plot
kmeans = KMeans(n_clusters=int(input('Enter the number of clusters:')))
# I am putting the number of clusters as 2 for the above data
kmeans.fit(list(zip(x,y)))
plt.scatter(x, y, c=kmeans.labels_)
plt.title('Scatter plot after assigning points to clusters:')
plt.show() #displaying the scatter plot after assigning the points to clusters