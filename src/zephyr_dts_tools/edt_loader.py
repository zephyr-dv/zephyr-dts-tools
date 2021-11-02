'''
Created on Nov 1, 2021

@author: mballance
'''
import os

from devicetree import edtlib

from zephyr_dts_tools.dts_preprocessor import DtsPreProcessor
from zephyr_dts_tools.dts_root import DtsRoot


class EdtLoader(object):
    
    def __init__(self, dts_file):
        self.dts_file = dts_file
        self.dts_root = []
        pass
    
    def load(self) -> edtlib.EDT:
        dts_pp = DtsPreProcessor()
        
        bindings_dirs = []
    
        dts_root = DtsRoot()
        for d in self.dts_root:
            dts_pp.add_dts_root(d)
        
            if os.path.isdir(os.path.join(d, "dts", "bindings")):
                bindings_dirs.append(os.path.join(d, "dts", "bindings"))
            dts_root.add_root(d)

        with open("tmp.dts.tmp", "w") as fp:    
            dts_pp.process(self.dts_file, fp)
            
        vendor_prefixes = {}
        
        edt = edtlib.EDT("tmp.dts.tmp", bindings_dirs,
            # Suppress this warning if it's suppressed in dtc
            warn_reg_unit_address_mismatch=True,
            default_prop_types=True,
            infer_binding_for_paths=["/zephyr,user"])
        
        # Perform cursory validation
        unbound = []
        for n in edt.nodes:
            if n.path.find('@') != -1 and not n.binding_path:
                unbound.append(n.path)
                
        if len(unbound) > 0:
            raise Exception("No binding for node(s): %s" % " ".join(unbound))
        
        return edt
