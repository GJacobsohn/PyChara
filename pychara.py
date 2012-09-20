""" Main Module of PyChara """
__author__ = 'gabriel'


from optparse import OptionParser
from pychara.parser import Parser
import os

def cmdline_options():
    """ Definition of the Cmd Line Options """
    options = OptionParser()
    options.add_option("-f","--file",dest = "filename")
    options.add_option("-r","--recursive", action="store_true",dest="recursive")
    options.add_option("-m","--metric", action="append", dest="metrics")
    options.add_option("-o","--output", dest="output", default="output.xml")
    return options


def main():
    """ Main Function of PyChara """
    options = cmdline_options()
    (options, args) = options.parse_args()
    parser = Parser()
    filename = os.path.basename(options.filename)
    path = os.path.dirname(options.filename) or "."
    parser.add_visitor(options.metrics)
    parser.parse_files(path,filename,options.recursive)

if __name__ == "__main__":
    main()