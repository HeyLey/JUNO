from ROOT import *

rootfile = TFile("eplus_hits_dn_0.root", "r")
lpmt_hits = rootfile.Get("lpmt_hits")

for enum, event in enumerate(lpmt_hits):
  if enum > 2: break
  nHits = int(event.GetLeaf("nHits").GetValue())
  pmtID = []
  hitTime = []
  isDN = []
  for i in range(0, nHits):
    pmtID.append(event.GetLeaf("pmtID").GetValue(i))
    hitTime.append(event.GetLeaf("hitTime").GetValue(i))
#    isDN.append(event.GetLeaf("isDN").GetValue(i))

