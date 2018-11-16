from utils.save import hits_to_hdf, pos_to_csv, true_info_to_csv

def convert(t1, t2, t3, t4, t5):
    hits_to_hdf(t1, 'lpmt_hits.h5')
    hits_to_hdf(t2, 'spmt_hits.h5')
    pos_to_csv(t4, 'lpmt_pos.csv')
    pos_to_csv(t5, 'spmt_pos.csv')
    true_info_to_csv(t3, 'true_info.csv')