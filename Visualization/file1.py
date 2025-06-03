import matplotlib.pyplot as plt
x_axis = []
y_axis = []
def bar_graph(table):                   # sudo apt-get install python3-tk
    for i in table:
        # print(i)
        x_axis.append(i[0])
        y_axis.append(i[1])

    plt.figure(figsize=(20,10))
    plt.bar(x_axis,y_axis)
    plt.xlabel('Product Name')
    plt.ylabel('Quantity')
    plt.title('Top 10 Products, having most sales')
    # plt.show()
    plt.savefig('/home/pranav/PycharmProjects/Bigdata92/hive_project'
                '/Result/Analytics1/Mostsales.png')







