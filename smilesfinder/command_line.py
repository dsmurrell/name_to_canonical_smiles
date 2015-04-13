import smilesfinder
import os, sys, csv
from General import *
from URLFetchingHelpers import *
from ConfigParserHelpers import *
import urllib2
from indigo import *
from MyIndigo import *

def main():
    #reload(MyIndigo)
    indigo = Indigo()
    #indigo_inchi = IndigoInchi(indigo)
    mi = MyIndigo.MyIndigo(indigo)

    # read config file
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read("arguments.config")
    inputCSV = ConfigParserHelpers.ConfigSectionMap(config, "IO")['input csv']
    outputCSV = ConfigParserHelpers.ConfigSectionMap(config, "IO")['output csv']
    numMolecules = General.num(ConfigParserHelpers.ConfigSectionMap(config, "Parameters")['number of molecules'])

    writer = csv.writer(open(outputCSV, 'wb'))

    with open(inputCSV, 'U') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        i = 0
        for row in reader:
            id = row[0]
            name = row[1]
            SMILES = ""
            try:
                SMILES = mi.fetchCanonicalSMILESbyName(name)
                print "Fetched SMILES: " + SMILES
            except:
                e = sys.exc_info()[0]
                print e
            writer.writerow([id,name,SMILES])
            i = i+1
            if i>=numMolecules and numMolecules != -1:
                break