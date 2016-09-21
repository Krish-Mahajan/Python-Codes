import psycopg2
import os
import csv
import pickle
#os.chdir("C:\\Users\\IBM_ADMIN\\git\\CDPHP\\data\\20151211_SiteIDCommunityDectection")
conn = psycopg2.connect("dbname='capdi' user='kmahajan' host='localhost' password='krishna' port='5434'") ### ask Kun Lin on how to connect and your id password
c=conn.cursor()

sql='SELECT  c.new_euid,svc_npi,svc_prov_tax_id,svc_rel_grp_id,svc_specialty,"CLM_SUBTYP_CD", "CLAIM_ID","GPI04_CLASS_CODE", "COR_PROC_CD_ID",fac_clm_adm_dt, fac_clm_dschg_dt , claim_start_date, c.allow_amt, c.coinsurance_amt, deductible_amt,copay_amt, "GENDER", c.year,yob,  "CLM_LN_PLOS_CD",c."MBR_HM_ADDR_ST_CNTY_CD", cli_dx1, cli_dx2, cli_dx3, cli_dx4, cli_dx1_ccs, cli_dx2_ccs, cli_dx3_ccs, cli_dx4_ccs, c.proc_ccs FROM filtered_claims c JOIN pmpm p ON c.new_euid=p.new_euid WHERE 
( C."MBR_HM_ADDR_ST_CNTY_CD"=\'NY001\' or C."MBR_HM_ADDR_ST_CNTY_CD"=\'NY091\' or C."MBR_HM_ADDR_ST_CNTY_CD"=\'NY093\' or C."MBR_HM_ADDR_ST_CNTY_CD"=\'NY083\' ) 
AND c.year=2014 AND p.year=2014 AND p.month=12 AND c.yob < 1996 AND "SRC_SYS_CD"=\'FCT\';'

c.execute(sql)
item=["new_euid","svc_npi","svc_prov_tax_id","svc_rel_grp_id","svc_specialty","CLM_SUBTYP_CD","CLAIM_ID","GPI04_CLASS_CODE","COR_PROC_CD_ID","fac_clm_adm_dt","fac_clm_dschg_dt","claim_start_date","allow_amt","coinsurance_amt","deductible_amt","copay_amt","GENDER","year","yob","CLM_LN_PLOS_CD","MBR_HM_ADDR_ST_CNTY_CD","cli_dx1","cli_dx2","cli_dx3","cli_dx4","cli_dx1_ccs","cli_dx2_ccs","cli_dx3_ccs","cli_dx4_ccs","proc_ccs"]

row=c.fetchone()
fh=open("all_new.csv",'wb+')
writer=csv.writer(fh)
writer.writerow(item)

while row is not None:
    writer.writerow(list(row))
    row=c.fetchone()

fh.close()











