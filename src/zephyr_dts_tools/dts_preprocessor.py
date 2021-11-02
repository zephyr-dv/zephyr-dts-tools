'''
Created on Oct 5, 2021

@author: mballance
'''
import os
import pcpp


class DtsPreProcessor(object):
    
    def __init__(self):
        self.arch = None
        self.incdirs = []
        pass
    
    def add_dts_root(self, path):
        leaves = ["dts_root_path", "include", "dts/common"]
        
        if self.arch is not None:
            leaves.append(os.path.join("dts", self.arch))
        leaves.append("dts")
        
        for l in leaves:
            if os.path.isdir(os.path.join(path, l)):
                self.incdirs.append(os.path.join(path, l))
    
    def process(self, root_dts, out):
        pp = pcpp.Preprocessor()

        pp.define("__DTS__")
        
        for inc in self.incdirs:
            pp.add_path(inc)
            
        with open(root_dts, "r") as fp:
            pp.parse(fp)

        pp.write(out)
        
        