#Import libraries
import seaborn as sns
import matplotlib.pyplot as Plt 
sns.set_theme(style="ticks", color_codes=True)

#Import data set
boat = sns.load_dataset("titanic")
print(boat)

#Plot basic graph
#count plot with one variable
p =sns.countplot(x= "sex", data=boat)
Plt.show()

#count plot with 2 variables
p =sns.countplot(x= "sex", hue="class", data=boat)
Plt.show()

# plot with titles
p =sns.countplot(x= "sex", hue="class", data=boat)
p.set_title("Basic count plot")
Plt.show()
