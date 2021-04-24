import csv
import plotly.express as pe
import numpy as np

def showGraphs():
    with open("data1.csv") as d1:
        df = csv.DictReader(d1)
        figure1 = pe.scatter(df, x = "Temperature", y = "Ice-cream Sales")
        figure1.show()


    with open("data4.csv") as d4:
        df = csv.DictReader(d4)
        figure4 = pe.scatter(df,x = "Coffee in ml", y = "sleep in hours")
        figure4.show()

def getDataSource(pathToFile):
    iceCreamSales=[]
    coldDrinkSales=[]
    Temperature=[]
    with open(pathToFile) as ds1:
        reader = csv.DictReader(ds1)
        for row in reader:
            iceCreamSales.append(float(row['Ice-cream Sales']))
            Temperature.append(float(row['Temperature']))
            coldDrinkSales.append(float(row['Cold drink sales']))
    return{"x": iceCreamSales, "y":Temperature, "z":coldDrinkSales}

def findCorelation(dataSource):
    Corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(Corelation[0,1])

def setUp():
    path = "./data1.csv"
    dataSource = getDataSource(path)
    findCorelation(dataSource)

setUp()
    

#For Coffee (Data set 4)


def getDataSource4(pathToFile):
    Coffee=[]
    Sleep=[]
    with open(pathToFile) as ds4:
        reader = csv.DictReader(ds4)
        for row in reader:
            Coffee.append(float(row['Coffee in ml']))
            Sleep.append(float(row['sleep in hours']))
    return{"x": Coffee, "y":Sleep}

def findCorelation4(dataSource):
    Corelation4 = np.corrcoef(dataSource["x"], dataSource["y"])
    print(Corelation4[0,1])

def setUp4():
    path = "./data4.csv"
    dataSource = getDataSource4(path)
    findCorelation4(dataSource)

setUp4()