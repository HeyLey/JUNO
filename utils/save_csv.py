from utils.read_data import read_hits, read_pos, read_true_info
import pandas as pd
import tables

spmt_nHits, spmt_pmtID, spmt_hitTime, spmt_isDN = read_hits(t2)
spmt_nHits, spmt_pmtID, spmt_hitTime, spmt_isDN = read_hits(t2)

def hits_to_csv(t, name):
    nHits, pmtID, hitTime, isDN = read_hits(t)
    df = pd.DataFrame({ 'nHits': nHits, 'pmtID': pmtID, 
                        'hitTime': hitTime, 'isDN': isDN
                     })
    df.to_csv(name, index=False)


def pos_to_csv(t, name):
    pmt_id, pmt_x, pmt_y, pmt_z = read_pos(t)
    df = pd.DataFrame({ 'pmt_id': pmt_id, 'pmt_x': pmt_x, 
                        'pmt_y': pmt_y, 'pmt_z': pmt_z
                     })
    df.to_csv(name, index=False)


def true_info_to_csv(t, name):
    evtID, E, x, y, z, R = read_true_info(t)
    df = pd.DataFrame({ 'evtID': evtID, 'E': E, 'x': x,
                        'y': y, 'z': z, 'R': R
                     })
    df.to_csv(name, index=False)