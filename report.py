import argparse
import os
import json
import csv
import matplotlib.pyplot as plt

'''
Project Description The project is a script that reads data from one or 
more JSON files and generates a report based on the data. 
The report includes statistics and visualizations of the 
data, such as histograms and scatter plots. The script can 
be configured with command-line arguments, including the 
input directory, the output file name, and the types of 
visualizations to generate.


'''

# python report.py input output --histograms --scatter


def load_data(folder):
    '''
    read folder and extraction file

    Args:
        folder (folder): A path folder.

    Returns:
        return all data in files json
    '''
    
    for root, dirs, files in os.walk(folder):
        data_all = []
        try:
            for filename in files:
                js = filename.split(".")
                if js[1] == "json":
                    with open(root + "/" + filename, "r") as file:
                        data = json.load(file)
                    for i in data:
                        data_all.append(i)
                if js[1] == "csv":
                    with open(root + "/" + filename) as csvFile:
                        csvReade = csv.DictReader(csvFile)
                        for rows in csvReade:
                            data_all.append(rows)
        except FileNotFoundError:
            data = []
            print("The file doesn't exist.")
        except Exception as e:
            print("Error: ", e)
        return data_all


def extraction_key(data, keys):
    '''
    extraction key in data

    Args:
        data (dice): A data of files.
        keys (list): A list of key.

    Returns:
        return all key in files json
    '''

    for value in data:
        for value , key in enumerate(value):
            if key not in keys:
                keys.append(key)
    return keys
    

def Sort_values(data, x, y):
    '''
    Sort values of x , y.

    Args:
        data (dice): A data of files.
        x (str): The first keyword.
        y (str): The second keyword.

    Returns:
        return list of x and list of y.
    '''
    x_ = []
    y_ = []
    for value in data:
        if x in value and y in value:
            x_.append(value[x])
            y_.append(value[y])

    return x_ , y_

def plt_scatter(x, y, x_name, y_name):
    '''
    Draw a set of points in a manner scatter.

    Args:
        x (list): The first a points.
        y (list): The second a points.
        x_name (str): The first keyword.
        y_name (str): The second keyword.

    '''

    plt.scatter(x, y)
    plt.savefig("imags/"+f"{x_name}_{y_name}_scatter.png")
    plt.show()


def plt_histograms(x, y, x_name, y_name):
    '''
    Draw a set of points in a manner histograms.

    Args:
        x (list): The first a points.
        y (list): The second a points.
        x_name (str): The first keyword.
        y_name (str): The second keyword.

    '''

    plt.hist(x, label='x',bins = 35, alpha = 0.7, color = 'blue')
    plt.savefig("imags/"+f"{x_name}_hist.png")
    plt.show()
    plt.hist(y, label='y',bins = 35, alpha = 0.5, color = 'red')
    plt.savefig("imags/"+f"{y_name}_hist.png")
    plt.show()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate graphs based on data from JSON files.')
    parser.add_argument('-in', '--input_dir', help='Path to directory containing input folder.', required=True)
    parser.add_argument('-hg', '--histograms', type= str, help='Generate histograms', nargs=2, metavar=('X', 'Y'))
    parser.add_argument('-s', '--scatter', type= str, help='Generate scatter plots', nargs=2, metavar=('X', 'Y'))
    
    args = parser.parse_args()

    data = load_data(args.input_dir)
    keys = []
    if data == []:
        print("The list empty")
        quit()
    else:
        keys = extraction_key(data, keys)

    
    if args.histograms:
        x = args.histograms[0]
        y = args.histograms[1]
        if x and y:
            if x in keys: 
                x = x
            else:
                print("The value x not found")
                quit()
            if y in keys:
                y = y
            else:
                print("The value y not found")
                quit()
                

            x_name = x
            y_name = y

            x ,y = Sort_values(data, x, y)
            plt_histograms(x, y, x_name, y_name)
    

        else:
            print("Please put the x and y values")
            quit()
    if args.scatter:
        x = args.scatter[0]
        y = args.scatter[1]
        if x and y:
            if x in keys: 
                x = x
            else:
                print("The value x not found")
                quit()
            if y in keys:
                y = y
            else:
                print("The value y not found")
                quit()
            x_name = x
            y_name = y

            x ,y = Sort_values(data, x, y)
            plt_scatter(x, y, x_name, y_name)
            
        else:
            print("Please put the x and y values")
            quit()
