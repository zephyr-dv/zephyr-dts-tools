'''
Created on Oct 5, 2021

@author: mballance
'''
import os


class DtsRoot(object):
    
    def __init__(self):
        self.paths = []
        self.arch = None
        
    def add_root(self, path):
        leaves = ["dts_root_path", "include", "dts/common"]
        
        if self.arch is not None:
            leaves.append(os.path.join("dts", self.arch))
        leaves.append("dts")
        
        for l in leaves:
            if os.path.isdir(os.path.join(path, l)):
                self.paths.append(os.path.join(path, l))
        