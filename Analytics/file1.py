# Top 10 products which most sales in quantity wise

from hive_project.connection import hiveConnection
def Most_sales():
    try:
        c = hiveConnection()
        hql = f'''select productname,sum(quantity)as Total_sales_qty from
            products join sales on products.productid = sales.productid
            group by productname order by Total_sales_qty desc limit 10'''
        c.execute(hql)
        Result_table = c.fetchall()
        # print(Result_table)
        path = ("/home/pranav/PycharmProjects/Bigdata92/hive_project/Result"
                "/Analytics1/Result1.txt")
        with open(path,'w')as myfile:
            for i in Result_table:
                myfile.writelines(f"{i}\n")
        return Result_table
    except Exception as e:
        print('Errro in Most Sales query (Analytics1) : ',e)

print(Most_sales())