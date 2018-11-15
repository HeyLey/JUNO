import uproot

def read_hits(hits):
    nHits = hits.get('nHits').array()
    pmtID = hits.get('pmtID').array()
    hitTime = hits.get('hitTime').array()
    isDN = hits.get('isDN').array()

    return nHits, pmtID, hitTime, isDN


def read_pos(pos):
    pmt_id = pos.get('pmt_id').array() 
    pmt_x = pos.get('pmt_x').array() 
    pmt_y = pos.get('pmt_y').array() 
    pmt_z = pos.get('pmt_z').array() 

    return pmt_id, pmt_x, pmt_y, pmt_z


def read_true_info(true_info):
    evtID = true_info.get('evtID').array()  
    E = true_info.get('E').array() 
    x = true_info.get('x').array() 
    y = true_info.get('y').array() 
    z = true_info.get('z').array() 
    R = true_info.get('R').array() 

    return evtID, E, x, y, z, R