# import matplotlib.pyplot as plt
# import numpy as np

# xpoint = np.array([0,6])
# ypoint = np.array([0,250])

# plt.plot(xpoint, ypoint)
# plt.show()

#------

# xpoint = np.array([5,6,5])
# ypoint = np.array([5,250,66])

# plt.plot(xpoint, ypoint, 'o')
# plt.show()

#----------

# xpoint = np.array([3,5,7,2,5,8])

# plt.plot(xpoint)
# plt.plot(xpoint, 'o')
# plt.show()

#----------
# xpoint = np.array([3,5,7,2,5,8])

# # plt.plot(xpoint, marker = 'o')
# plt.plot(xpoint, marker = '*')
# plt.show()
#-----------

# xpoint = np.array([3,5,7,2,5,8])  # lines and point colors

# plt.plot(xpoint, 'o:g')
# plt.show()

#------

# xpoint = np.array([3,5,7,2,5,8])

# plt.plot(xpoint, marker = 'o', ms=10, mec = 'r', mfc = 'b')  #point border color and inside the color
# plt.show()

#--------

# xpoint = np.array([3,5,8])

# plt.plot(xpoint, linestyle = "dotted")
# plt.show()

#--------

# xpoint = np.array([3,5,8])

# plt.plot(xpoint, marker = 'o',c = 'blue' , linewidth = '20.5')

# plt.show()
#-----------

# y1 = np.array([3,5,6,4,8])   #  drawing multiple lines
# y2 = np.array([8,7,5,6,4])
# y3 = np.array([4,3,6,5,2])
# plt.plot(y1)
# plt.plot(y2)
# plt.plot(y3)
# plt.show()

#------------

# x = np.array([12,23,34,45,56])
# y = np.array([45,43,23,23,56])

# plt.plot(x,y)
# plt.xlabel("roll no")
# plt.ylabel("Marks")
# plt.title("Student result")
# plt.show()

#----------

# x = np.array([12,23,34,45,56])
# y = np.array([45,43,23,23,56])

# font1 = {'family': 'serif', 'color':'black', 'size':'20'}
# font2 = {"family": 'serif', 'color': 'darkred', 'size':'20'}

# plt.plot(x,y)
# plt.xlabel("roll no", fontdict=font2)
# plt.ylabel("Marks", fontdict=font1)
# plt.title("Student result",fontdict=font1, loc='left')
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()

#------

# x1 = np.array([0,1,2,3,4])
# y1 = np.array([20,40,50,60,90])

# plt.subplot(1,2,1)
# plt.plot(x1,y1)

# plt.grid()

# x2 = np.array([0,1,2,3,4])
# y2 = np.array([80,80,70,40,60])

# plt.subplot(1,2,2)
# plt.plot(x2,y2)

# plt.grid()

# plt.show()

#---------

#plot1

# x1 = np.array([0,1,2,3,4])
# y1 = np.array([20,40,50,60,90])

# plt.subplot(1,2,1)
# plt.plot(x1,y1)
# plt.plot("Sales")

# #plot2

# x2 = np.array([0,1,2,3,4])
# y2 = np.array([80,80,70,40,60])

# plt.subplot(1,2,2)
# plt.plot(x2,y2)
# plt.plot("Income")

# plt.suptitle("shop")


# plt.show()

#-----------

# x = np.array([3,4,5,2,5,6,7])  #dot diagram
# y = np.array([7,8,9,4,5,6,3])

# plt.scatter(x,y)
# plt.show()

# #------------

# x = np.array([1,2,3,4,5,6,7])  #dot diagram
# y = np.array([7,8,9,4,5,6,3])
# plt.scatter(x,y,color = "hotpink", cmap='viridis')

# x = np.array([1,2,3,4,5,6,7])
# y = np.array([7,5,6,8,5,4,3])
# plt.scatter(x,y,color="green", cmap='viridis')

# plt.colorbar()
# plt.show()

#-------

# x = np.array(["A","B","C","D","E","F","G"])  #BAR diagram
# y = np.array([7,8,9,4,5,6,3])

# plt.bar(x,y,width=0.2) #vertical
# plt.barh(x,y, height=0.3)  #horizontal

# plt.show()

# -----

# x = np.random.normal(170,50,120)  #histrogram
# plt.hist(x)
# plt.show()

#---  piechart

# x = np.array([2,6,5,2,4])
# mylabels = ["Apple","Banana","Mango","Cherry","ganna"]
# myexplode = [0.2,0.1,0.2,0.4,0.3]
# plt.pie(x, labels=mylabels, startangle=180)  #startangle point
# plt.pie(x,labels=mylabels, explode=myexplode)  #explode point
# plt.pie(x, labels=mylabels)

# plt.legend(title = "Five Fruits:")

# plt.show()

