from utils.read_data import read_hits, read_pos, read_true_info
import pandas as pd
import tables

def hits_to_hdf(t, name):
    nHits, pmtID, hitTime, isDN = read_hits(t)
    
    dt_list = []
    for i in tqdm(range(len(nHits))):
        n = nHits[i]
        
        df2 = pd.DataFrame({
            'event': i,
            'pmtID': pmtID[i], 
            'hitTime': hitTime[i], 
            'isDN': isDN[i]
                             
        }) 
        dt_list.append(df2)
    
    pd.concat(dt_list).to_hdf(name, index=False, key='df', mode='w')


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