print("dda module for test import")

import dataanalysis.core as da
#import ddaontology as do

class TestNode(da.DataAnalysis):
    def main(self):
        self.data={'test':'data'}
        with open("data-file.txt","w") as f:
            f.write("data")
        self.data_file=da.DataFile("data-file.txt")
    
