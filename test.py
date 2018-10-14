print("dda module for test import")

import dataanalysis.core as da
#import ddaontology as do

class TestNode(da.DataAnalysis):
    def main(self):
        self.data=dict{'test':'data'}
        open("data-file.txt","w").write("data")
        self.data_file=da.DataFile("data-file.txt")
    
