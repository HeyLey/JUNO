from utils.read_data import read_hits, read_pos, read_true_info
import pandas as pd
import tables

def hits_to_csv(t, name):
    nHits, pmtID, hitTime, isDN = read_hits(t)
    df = pd.DataFrame(columns=['nHits', 'pmtID', 'hitTime', 'isDN'], index=[0])
    for i in range(0, 1):
        n = nHits[i]
        for j in range(0, n):
            df2 = pd.DataFrame({ 'nHits': n, 'pmtID': pmtID[i][j], 
                                'hitTime': hitTime[i][j], 'isDN': isDN[i][j]
                             })
            df.append(df2)
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