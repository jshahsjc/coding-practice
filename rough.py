def _add_policy_map_rule_1():
    pmr_nhg_egress = []
    remote_sites = [ 'ash', 'frc', 'prn' ]
    traffic_classes = [ 'silver', 'platinum', 'bronze' ]
    for site in remote_sites:
        for tc in traffic_classes:
            if tc == 'silver':
                pmr_nhg_egress += ( [ "lspgrp_atn-" + site + "-silver-class" ] * 9 )
            if tc == 'platinum':
                pmr_nhg_egress += ( [ "lspgrp_atn-" + site + "-platinum-class" ] * 5 )
            if tc == 'bronze':
                pmr_nhg_egress += ( [ "lspgrp_atn-" + site + "-bronze-class" ] * 2 )
    ixia_sites = [ ("lspgrp_atn-sc" + str(i)) for i in range( 101, 286 ) ]
    for site in ixia_sites:
        nhg_name = site + '-gold-class'
        for tc in traffic_classes:
            if tc == 'silver':
                pmr_nhg_egress += ( [ site + "-silver-class" ] * 9 )
            if tc == 'platinum':
                pmr_nhg_egress += ( [ site + "-platinum-class" ] * 5 )
            if tc == 'bronze':
                pmr_nhg_egress += ( [ site + "-bronze-class" ] * 2 )
    pmr_dscp = [ 5, 6, 7, 8, 9, 12, 13, 14, 15, 26, 27, 32, 35, 48, 10, 11 ] * 188
    res = {}
    for i in range(3008):
        key  = str(pmr_nhg_egress[i]) + str(pmr_dscp[i])
        res[key] = i
    return len(res)

pmr_bronze = [ 10, 11, 16, 17, 19, 20, 21, 22, 23, 25, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63 ]
pmr_silver = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 40, 41, 42, 43, 44, 45, 46, 47, 49 ]
pmr_platinum = [ 26, 27, 32, 35, 48 ]
pmr_dscp = pmr_bronze + pmr_silver + pmr_platinum
