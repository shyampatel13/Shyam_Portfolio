import pymysql
import csv

f = open("/Users/shyampatel/Desktop/Projects/Videogame Sales Data/vgsales.csv", "r")
fString = f.read()

# convert string to list
fList = []
for line in fString.split('\n'):
    fList.append(line.split(','))

# open connection to database
db = pymysql.connect(host="127.0.0.1", user="root", password="cowboys13", port=3306, database='videogamedb')

# prepare a cursor onject using cursor() method
cursor = db.cursor()

# Drop table if it already exists using execute() method
cursor.execute("DROP TABLE IF EXISTS VGsales")

# Create column nams from the first line in fList
Ranking = fList[0][0]; Title = fList[0][1]; Platform = fList[0][2]; Released = fList[0][3]; Genre = fList[0][4]; Publisher = fList[0][5];
NA_Sales = fList[0][6]; EU_Sales = fList[0][7]; JP_Sales = fList[0][8]; Other_Sales = fList[0][9]; Global_Sales = fList[0][10]

# Create VGsales table // place a comma after each new column except the last
queryCreateVGsalesTable = """create TABLE VGsales(
                            {} varchar(240) not null,
                            {} varchar(240) NOT NULL ,
                            {} varchar(240) NOT NULL,
                            {} varchar(240) not null,
                            {} varchar(240) NOT NULL,
                            {} varchar(240) NOT NULL,
                            {} varchar(240) not NULL,
                            {} varchar(240) not NULL,
                            {} varchar(240) not NULL,
                            {} varchar(240) not NULL,
                            {} varchar(240) not NULL
                            )""".format(Ranking, Title, Platform, Released, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales)

cursor.execute(queryCreateVGsalesTable)
for i in range(len(fList)-1):
    insert_query = """insert INTO VGsales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    insert_value = [fList[i][0], fList[i][1], fList[i][2], fList[i][3], fList[i][4], fList[i][5], fList[i][6],
    fList[i][7], fList[i][8], fList[i][9], fList[i][10]]
    cursor.execute(insert_query, insert_value)
    db.commit()
    # To check which rows were inserted
    print(fList[i][0])
    print('Row Complete')
db.close()
