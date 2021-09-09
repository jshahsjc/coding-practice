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
        for i in range(16):
            pmr_nhg_ingress.append(nhg_name)
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
        key  = str(pmr_nhg_egress[i]) + str(pmr_nhg_egress[i])
        res[k] = i
    return len(res)
