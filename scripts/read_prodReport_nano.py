# Quick script to read the number of events and files from prodReport_nano.json produced with HLepRare group 
# python3 read_prodReport_nano.py --dir TTto4Q 

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '--dir', help='path to the dataset directory where the prodReport_nano.json', default="Muon0_Run2023D_v1")
parser.add_argument( '--eos', help='path to the eos HLepRare directory', default="/eos/cms/store/group/phys_higgs/HLepRare/skim_2024_v2/Run3_2023BPix")
args = parser.parse_args()

full_path = args.eos +"/" + args.dir + "/prodReport_nano.json"

with open(full_path, "r") as f:
    prod_dict = json.load(f)

files = prod_dict["outputs"].keys()
n_files = len(files)
n_events = sum([(prod_dict["outputs"][x]["n_selected"] + prod_dict["outputs"][x]["n_not_selected"]) for x in prod_dict["outputs"].keys()])
print( args.dir ,":\n n_files = ", n_files, "\n n_events = ", n_events )

