"""
@Date: 09/09/2017
@author: Xinya Li (xinya.li@pnl.gov)
@Project: Demeter-W V1.0

License:  BSD 2-Clause, see LICENSE and DISCLAIMER files
Copyright (c) 2017, Battelle Memorial Institute

"""
import csv
import numpy

def getHeader(filename):
    try:
        #f = open(filename, "r")
        f = open(filename, "rU")
        reader = csv.reader(f, delimiter=",")
        try:
            header = reader.next()
            if len(header) < 2:
                header = None
            return header
        finally:
            f.close()
    except IOError:
        pass

def getContent(filename, headerNum):
    try:
        f = open(filename, "rU")
        reader = csv.reader(f, delimiter=",")
        data = []
        try:
            for i in range(0,headerNum):
                reader.next() # skip header

            # Skip the empty line
            for row in reader:
                if len(row) > 0:   
                    row = row
                    data.append(row)
            return data
        finally:
            f.close()
    except IOError:
        pass

def getContentArray(filename, headerNum):
    try:
        f = open(filename, "rU")
        data = numpy.genfromtxt(f, delimiter=",", skip_header = headerNum, filling_values="0")
        return data
        f.close()
    except IOError:
        pass
     
def getContentNum(filename, headerNum, row0, nrow):
    try:
        count = 0
        f = open(filename, "rU")
        reader = csv.reader(f, delimiter=",")
        data = []
        try:
            for i in range(0,headerNum + row0):
                reader.next() # skip header

            # Skip the empty line
            for row in reader:
                if len(row) > 0:
                    row = row
                    data.append(row)
                    count = count + 1
                    if count > nrow:
                        break                    
            return data
        finally:
            f.close()
    except IOError:
        pass
    
        
def getColumn(filename, headerNum, column):
    try:
        f = open(filename, "rU")
        reader = csv.reader(f, delimiter=",")
        data = []
        try:
            for i in range(0,headerNum):
                reader.next() # skip header

            # Skip the empty line
            for row in reader:
                if len(row) > 0:
                    row = row
                    data.append(row[column])
            return data
        finally:
            f.close()
    except IOError:
        print "Fail to open file: ",filename
        pass

def getColumnNum(filename, headerNum, column):
    data = getColumn(filename, headerNum, column)
    column = []
    for i in range(0,len(data)):
        column.append(float(data[i]))
    return column
    
def getNumeric(filename, headerNum, column):
    data = getColumn(filename, headerNum, column)
    return numpy.array(data,dtype='f')

def getNumericRow(filename, headerNum, row):
    content = getContent(filename, headerNum)
    data = content[row]
    return numpy.array(data[row:],dtype='f')