'''
Created on Nov 1, 2021

@author: mballance
'''
from vte.template_engine import TemplateEngine
from vte.template_info import TemplateInfo
from devicetree import edtlib

class DtsTemplateEngine(TemplateEngine):
    
    def __init__(self, 
                 edt : edtlib.EDT,
                 template : TemplateInfo, 
                 outdir=None):
        super().__init__(template, outdir)
        self.edt = edt
        
        self.add_func(self.edt_nodes, "edt_nodes")
        
    def init_env(self, env):
        super().init_env(self, env)
        
    def edt_nodes(self):
        return self.edt.nodes
    
    