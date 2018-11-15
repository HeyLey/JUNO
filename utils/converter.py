from utils.save_csv import hits_to_csv, pos_to_csv, true_info_to_csv

def convert(t1, t2, t3, t4, t5):
    hits_to_csv(t1, 'lpmt_hits')
    hits_to_csv(t2, 'spmt_hits')
    pos_to_csv(t4, 'lpmt_hits')
    pos_to_csv(t5, 'spmt_hits')
    true_info_to_csv(t3, 'true_info')