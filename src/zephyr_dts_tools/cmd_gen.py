'''
Created on Oct 5, 2021

@author: mballance
'''
import os
import sys

from devicetree import edtlib

from vte.template_info import TemplateInfo
from zephyr_dts_tools.dts_preprocessor import DtsPreProcessor
from zephyr_dts_tools.dts_root import DtsRoot
from zephyr_dts_tools.edt_loader import EdtLoader
from zephyr_dts_tools.dts_template_engine import DtsTemplateEngine


def gen(args):
#     dts_pp = DtsPreProcessor()
#
#     bindings_dirs = []
#
#     dts_root = DtsRoot()
#     for d in args.dts_root:
#         dts_pp.add_dts_root(d)
#
#         if os.path.isdir(os.path.join(d, "dts", "bindings")):
#             bindings_dirs.append(os.path.join(d, "dts", "bindings"))
#         dts_root.add_root(d)
#
#     with open("tmp.dts.tmp", "w") as fp:    
#         dts_pp.process(args.dts_file, fp)
#
#     vendor_prefixes = {}
#
#     try:
#         edt = edtlib.EDT("tmp.dts.tmp", bindings_dirs,
#             # Suppress this warning if it's suppressed in dtc
#             warn_reg_unit_address_mismatch=True,
#             default_prop_types=True,
#             infer_binding_for_paths=["/zephyr,user"])
#  #           werror=args.edtlib_Werror,
# #            vendor_prefixes=vendor_prefixes)
#     except edtlib.EDTError as e:
#         sys.exit(f"devicetree error: {e}")

    loader = EdtLoader(args.dts_file)
    if args.dts_root is not None:
        loader.dts_root.extend(args.dts_root)

    try:
        edt = loader.load()
    except Exception as e:
        sys.exit(f"failed to load device tree: {e}")
        
    print("edt: %s" % str(edt))
    
    if os.path.isdir(args.template):
        # Create a template from the files in this directory
        template = TemplateInfo("default", args.template)
    else:
        # Load templates and see if the ID exists
        raise Exception("TODO: load template by ID")
        pass
    
    if hasattr(args, "outdir") and args.outdir is not None:
        outdir = args.outdir
    else:
        outdir = os.path.join(os.getcwd(), "tmpdir")
        
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    
    te = DtsTemplateEngine(edt, template, outdir)
    
    te.generate("abc", {})
    
    # for n in edt.nodes:
    #     print("Node: %s" % str(n))
    #     print("  label: %s" % n.label)
    #     for prop in n.props.items():
    #         print("    prop: %s" % str(prop))
    #
    # nodes = []
    # for n in edt.nodes:
    #     if "pss-root-component" in n.props:
    #         nodes.append(n)
    #
    # for n in nodes:
    #     bind_dir = os.path.dirname(n.binding_path)
    #     files = n.props["pss-files"]
    #     print("files: %s (%s)" % (str(files), str(type(files))))
    #     for f in files.val:
    #         ap = os.path.abspath(os.path.join(bind_dir, f))
    #         print("ap: %s" % ap)
    #
    # print("nodes: %s" % str(nodes))

    
    pass