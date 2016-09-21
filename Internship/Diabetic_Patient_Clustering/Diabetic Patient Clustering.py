
# coding: utf-8

# ### Sections

# - [Loading patientLabelNPI.csv](#Loading-patientLabelNPI.csv)
# - [Loading diabetes_all_claims](#Loading-diabetes_all_claims)
# - [Merging diabetes_all_claim and patient_Label_npi](#Merging-diabetes_all_claim-and-patient_Label_npi)
# - [Loading CCS_Codes Description](#Loading-CCS_Codes-Description)
# - [Making summary of CCS_codes for 9K diabetic patients](#Making-summary-of-CCS_codes-for-9K-diabetic-patients)
# - [Clustering](#Performing-Clustering-Using-Cosine-Similarity)
# - [Performance evaluation measures on finalised clusters](#Performance-evaluation-measures-on-finalised-clusters)
# - [Grouping to see patients in each comm-cluster combination](#Grouping-to-see-patients-in-each-comm-cluster-combination)
# - [Adding Gender ,Pcal,Average Age information to community cluster](#Adding-Gender-,-Pcal-,-Average-Age-information-to-community-cluster)
# - [Defining NPI Communities](#Defining-NPI-Communities)
# - [Adding PQI measurement euid-npi-cluster](#Adding-PQI-measurement-euid-npi-cluster)

# # Loading patientLabelNPI.csv

# PatientLabelNPI has the mapping new_euid - comm_npi

# In[2]:

import pandas as pd  
import numpy as np 
import math


# In[3]:

cols=['new_euid','comm_npi']
type ={'new_euid':'str','comm_npi':'int64'}
patient_label_npi=pd.read_csv("../../Data/Diabetic_Patient_Clustering/patientLabelNPI.csv",usecols=cols,dtype=type)


# In[4]:

patient_label_npi.head()


# In[5]:

patient_label_npi.groupby(['comm_npi']).new_euid.nunique()


# In[6]:

patient_label_npi.shape 


# In[7]:

#unique patients in patient_Label_npi
len(patient_label_npi['new_euid'].unique()) 


# In[8]:

#checking distinct euid length
patient_label_npi.groupby(patient_label_npi['new_euid'].str.len()).agg({'new_euid':np.size}) 


# In[9]:

#checking if a patient (euid) is in more than one community
tmp=pd.DataFrame(patient_label_npi.groupby(['new_euid']).comm_npi.nunique())
tmp[tmp['comm_npi']>1].shape  
#No such patients 


# # Loading diabetes_all_claims

# diabetes_all_claims has mapping new_euid - ccs codes

# In[10]:

cols=['new_euid','cli_dx1_ccs','cli_dx2_ccs','cli_dx3_ccs','cli_dx4_ccs'] 
type={'new_euid':'str','cli_dx1_ccs':'str','cli_dx2_ccs':'str','cli_dx3_ccs':'str','cli_dx4_ccs':'str'}
diabetes_all_claims=pd.read_csv("../../Data/Diabetic_Patient_Clustering/diabetes_all_claims.csv",usecols=cols,dtype=type)


# In[11]:

diabetes_all_claims.head() 


# In[12]:

#Total Observation
diabetes_all_claims.shape


# In[13]:

#Total unique patients
len(diabetes_all_claims['new_euid'].unique()) 


# In[14]:

#null observation
diabetes_all_claims.isnull().sum() 


# In[15]:

#checking size of new_euid length
diabetes_all_claims.groupby(diabetes_all_claims['new_euid'].str.len()).agg({'new_euid':np.size}) 


# In[16]:

#stripping front 0
diabetes_all_claims['new_euid']=diabetes_all_claims['new_euid'].map(lambda x:str(x).lstrip('0'))


# In[17]:

#checking size of new_euid length after stripping front 0
diabetes_all_claims.groupby(diabetes_all_claims['new_euid'].str.len()).agg({'new_euid':np.size}) 


# # Merging diabetes_all_claim and patient_Label_npi

# merging both of these files to get the mapping new_euid-comm_npi-ccs codes

# In[18]:

diabetic_patients_comm_ccs=pd.merge(patient_label_npi,diabetes_all_claims) 


# In[19]:

diabetic_patients_comm_ccs.head() 


# In[20]:

#unique diabetic patients after merging
len(diabetic_patients_comm_ccs['new_euid'].unique()) 


# In[21]:

#check on null
diabetic_patients_comm_ccs.isnull().sum() 


# In[39]:

#checking unique values within ccs_code
# df=diabetic_patients_comm_ccs
# cols=df.columns.tolist()
# cols=cols[2:]
# for col in cols:
#     print(diabetic_patients_comm_ccs[col].unique()) ; 


# In[22]:

#filling NA's as 0
diabetic_patients_comm_ccs=diabetic_patients_comm_ccs.fillna(0)


# In[23]:

#checking null count after filling NA's as 0
diabetic_patients_comm_ccs.isnull().sum()


# In[24]:

#checking head
diabetic_patients_comm_ccs.head() 


# In[25]:

del diabetic_patients_comm_ccs['comm_npi']


# # Loading CCS_Codes Description

# In[26]:

ccs_codes=pd.read_csv('../../Data/ccs_code.csv')  #reading ccs code

#Adding 'CCS' ahead of CCS code number
ccs_codes['ccs_code']= "CCS"+ ccs_codes.START.map(str) #Adding CCS Codes 


# In[27]:

ccs_codes.head() 


# Making Binary Matrix with new-euid and each of 283 CCS codes as column

# In[28]:

cols=list(ccs_codes['ccs_code'])
cols.insert(0,'new_euid') 
diabetic_patients_binary=pd.DataFrame(columns=cols,index=diabetic_patients_comm_ccs.index) 
diabetic_patients_binary.head()  


# In[29]:

##Code to fill up binary Matrix as per each patients ccs_codes 
for index,row in diabetic_patients_comm_ccs.iterrows(): 
    if(row['cli_dx1_ccs'] !=0): 
        col="CCS" +str(row['cli_dx1_ccs'])
        diabetic_patients_binary.loc[index][col]=1 
        diabetic_patients_binary.loc[index]['new_euid']=row['new_euid']
    if(row['cli_dx2_ccs'] !=0): 
        col="CCS" +str(row['cli_dx2_ccs'])
        diabetic_patients_binary.loc[index][col]=1 
        diabetic_patients_binary.loc[index]['new_euid']=row['new_euid']
    if(row['cli_dx3_ccs'] !=0): 
        col="CCS" +str(row['cli_dx3_ccs']) 
        diabetic_patients_binary.loc[index][col]=1 
        diabetic_patients_binary.loc[index]['new_euid']=row['new_euid']   
    if(row['cli_dx4_ccs'] !=0): 
        col="CCS" +str(row['cli_dx4_ccs']) 
        diabetic_patients_binary.loc[index][col]=1 
        diabetic_patients_binary.loc[index]['new_euid']=row['new_euid'] 
    
    


# In[30]:

print(diabetic_patients_binary.shape)  
print(diabetic_patients_comm_ccs.shape)


# In[31]:

#filling NA's as 0
diabetic_patients_binary=diabetic_patients_binary.fillna(0) 

#Grouping by each patients
diabetic_patients_binary=diabetic_patients_binary.groupby(['new_euid']).sum()
print(diabetic_patients_binary.shape)  


# In[32]:

diabetic_patients_binary.head() 


# In[33]:

## changing all values greater >1 =1
def f1(x):
    if x>=1:
        return 1
    else:
        return 0

diabetic_patients_binary=diabetic_patients_binary.applymap(f1)
diabetic_patients_binary.head()  


# Caveat: After converting to binary we are losing the information how many times a particular ccs for a particular patient was claimed

# In[34]:

print(diabetic_patients_binary.shape) 

# Removing CCS49 i,e Diabetes with no complication
del diabetic_patients_binary['CCS49']  

#Removing Exam/Eval attribute.
del diabetic_patients_binary['CCS256']   

## Removing  CCS Codes which are 0 for all patients
diabetic_patients_binary=diabetic_patients_binary.loc[:,(diabetic_patients_binary!=0).any(axis=0)] 
print(diabetic_patients_binary.shape) 


# # Making summary of CCS_codes for 9K diabetic patients

# In[35]:

df=diabetic_patients_binary
codes_stats=pd.DataFrame(df.sum())
codes_stats.reset_index(inplace=True) 
codes_stats=codes_stats.rename(columns={0:'Total_Patients'})
codes_stats.head() 


# In[36]:

ccs_codes.head() 


# In[37]:

tmp1=ccs_codes[['ccs_code','LABEL']]
codes_stats=pd.merge(tmp1,codes_stats,left_on='ccs_code',right_on='index')
del codes_stats['index'] 
codes_stats=codes_stats.sort_values(['Total_Patients'],ascending=False)
codes_stats['population_percentage']=(codes_stats['Total_Patients']*1.0/8955)*100.0
codes_stats.head() 


# In[ ]:

#Writing summary to csv file
# codes_stats.to_csv("codes_stats.csv")


# In[38]:

##Deduplicating the binary matrix
df=diabetic_patients_binary  
df_new=pd.DataFrame(df.groupby(df.columns.tolist(),as_index=False).size())  
print(df_new.shape)
df_new.reset_index(inplace=True)  
df_new=df_new.rename(columns={0:'Total_Patients'})
df_new.sort_values(['Total_Patients'],ascending=False,inplace=True)
diabetic_patients_binary_ddup=df_new
diabetic_patients_binary_ddup.head() 


# # Performing Clustering Using Cosine Similarity

# In[39]:

cols=diabetic_patients_binary_ddup.columns.tolist()
diabetic_patients_binary_ddup[cols]=diabetic_patients_binary_ddup[cols].astype(float)

##converting binary matrix to IDF (i,e converting 0-1 to IDF)
for index,row in diabetic_patients_binary_ddup.iterrows():
    #print(index)
    for col in cols[:-1]:
         if(row[col]==1):
            fre=codes_stats[codes_stats['ccs_code']==col]['population_percentage']
            fre=(fre*1.0/100).iloc[0]
            #print("frequency is",fre)
            diabetic_patients_binary_ddup.loc[index][col]=np.log(1.0/fre)*1.0 
            #print("code is",col,"frequency is" ,fre,"IDF is",np.log(1.0/fre)*1.0,"Valu
diabetic_patients_binary_ddup.head() 


# In[41]:

print(diabetic_patients_binary_ddup.shape)
#print(clusters.shape) 


# In[42]:

#checking if the conversion happens correctly
print(codes_stats[codes_stats['ccs_code']=='CCS10'])  
print(math.log(1.0/0.4292)) 

print('\n') 

print(codes_stats[codes_stats['ccs_code']=='CCS98'])  
print(math.log(1.0/0.6809))  

#Happened Correctly


# In[43]:

#Clustering based on Cosine Metric and Average linkage Method
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram    
from scipy.cluster.hierarchy import cophenet

checkx=diabetic_patients_binary_ddup[1:]
X=pdist(checkx.ix[:,0:len(diabetic_patients_binary_ddup.columns)-1],metric='cosine')

Z = linkage(X,method='average') 
c,cd=cophenet(Z,X)
c 


# In[44]:

##Code to make dendogram

# plt.title('Hierarchical Clustering Dendrogram (truncated)')
# plt.xlabel('Patient Group')
# plt.ylabel(' Cosine distance')
# dendrogram(
#     Z,
#     truncate_mode='level',  # show only the last p merged clusters
#     p=100,  # show only the last p merged clusters
#     show_leaf_counts=True,  # otherwise numbers in brackets are counts
#     leaf_rotation=90.,
#     leaf_font_size=12.,
#     labels=list(checkx.index),
#     show_contracted=True,  # to get a distribution impression in truncated branches
# ) 
# plt.show() 


# In[45]:

#Code for clustering

from scipy.cluster.hierarchy import dendrogram, linkage , fcluster
max_d=0.9
clusters=fcluster(Z,max_d,criterion='distance')
clusters

clusters=pd.DataFrame(clusters)
clusters=clusters.rename(columns = {0:'clusters_id'})  

#concatinating binary ddup with cluster id.
checkx_new=pd.concat([checkx.reset_index(),clusters], axis=1)  
cols = checkx_new.columns.tolist() 
cols = cols[-2:] + cols[:-2] 
checkx_new=checkx_new[cols] 
checkx_new.set_index('index',inplace=True)  
community=checkx_new.groupby(['clusters_id']).Total_Patients.sum().sort_values(ascending=False)
community[:20] 


# In[46]:

### code for adding Z_score and cluster statistics.

def z_score(ccs_code):
    
    p_1=cluster_stats[cluster_stats['ccs_code']==ccs_code]['Total_Patients']*1.0/community[cluster_stats['cluster_id'][0]]
    p_1=p_1.iloc[0]
    p_2=codes_stats[codes_stats['ccs_code']==ccs_code]['Total_Patients']*1.0/8955.0
    p_2=p_2.iloc[0]
    
    n_1 = community[cluster_stats['cluster_id'][0]]*1.0 #cluster Population
    n_2 = 8955.0  #Total Population 
  
    p =(n_1*p_1 + n_2*p_2)*1.0/(n_1 + n_2)
   
    num = (p_1-p_2)*1.0
    deno= math.sqrt(p*(1-p)*( (1.0/n_1) + (1.0/n_2) ))
    
    z=round((num*1.0/deno),2)  
    
    p_values = round((scipy.stats.norm.sf(abs(z))*2),4) #twosided P Tailed test
    
    return(z,p_values)


def clusterstatistic(cluster_id):
    #print(cluster_id)
    cluster=checkx_new[checkx_new['clusters_id']==cluster_id]
   
    cluster=cluster.loc[:,(cluster!=0).any(axis=0)]
    #cluster.head()

    ccs_codes=cluster.columns.tolist()
    ccs_codes=ccs_codes[2:]
    cluster_stats=pd.DataFrame(columns=['cluster_id','CCS_Code','Total_Patients'])
    for code in ccs_codes:
        patients=cluster[cluster[code]!=0].Total_Patients.sum() 
        #print("code is",code,"patients is",patients)
        tmp=pd.DataFrame(index=range(1,2),columns=['cluster_id','CCS_Code','Total_Patients']) 
        tmp.ix[:,0]=cluster_id
        tmp.ix[:,1]=code
        tmp.ix[:,2]=patients 
        cluster_stats=cluster_stats.append(tmp) 

    #cluster_stats.head()

    #cluster_stats=cluster_stats[1:]
    cluster_stats.sort_values(by='Total_Patients',ascending=False,inplace=True)
    #cluster_stats.head()

    cluster_stats['%community']=(cluster_stats['Total_Patients']*1.0/cluster['Total_Patients'].sum())*100.0
    #cluster_stats['%diabetic_population']=(cluster_stats['Total_Patients']*1.0/14845.0)*100.0
    #cluster_stats.head()

    #tmp1.head()

    cluster_stats=pd.merge(tmp1,cluster_stats,left_on='ccs_code',right_on='CCS_Code')
    #cluster_stats.head()

    del cluster_stats['CCS_Code']
    cluster_stats.sort_values(by='Total_Patients',ascending=False,inplace=True)
    return cluster_stats


# In[47]:

community[:20]


# In[49]:

import scipy.stats
cluster_stats=clusterstatistic(47)
cluster_stats['%diabetic_population']=np.nan
cluster_stats['z_score']=np.nan
cluster_stats['p_value']=np.nan
for index,row in cluster_stats.iterrows(): 
    z,p=z_score(row['ccs_code'])
    cluster_stats.loc[index,'%diabetic_population']=codes_stats[codes_stats['ccs_code']==row['ccs_code']] .population_percentage.iloc[0] 
    cluster_stats.loc[index,'z_score']=z
    cluster_stats.loc[index,'p_value']=p  

cluster_stats['sort']=cluster_stats.z_score.abs()
cluster_stats.sort_values(by='sort',ascending=False,inplace=True)
cluster_stats.drop('sort',axis=1,inplace=True)
cluster_stats  ;


# In[199]:

#Code  to save all clusters to worksheets
# d=0.9
# writer = pd.ExcelWriter('../../Data_Created/Diabetic Clustering/clusters-'+str(d)+'.xlsx',engine='xlsxwriter')
# for cluster_id in community[community>80].index:
#     community_patients=community[cluster_id]
#     cluster_stats=clusterstatistic(cluster_id)
#     cluster_stats['%diabetic_population']=np.nan
#     cluster_stats['z_score']=np.nan
#     cluster_stats['p_value']=np.nan
#     for index,row in cluster_stats.iterrows(): 
#         z,p=z_score(row['ccs_code'])
#         cluster_stats.loc[index,'%diabetic_population']=codes_stats[codes_stats['ccs_code']==row['ccs_code']] .population_percentage.iloc[0] 
#         cluster_stats.loc[index,'z_score']=z
#         cluster_stats.loc[index,'p_value']=p  

#     cluster_stats['sort']=cluster_stats.z_score.abs()
#     cluster_stats.sort_values(by='sort',ascending=False,inplace=True)
#     cluster_stats.drop('sort',axis=1,inplace=True)
#     cluster_stats.to_excel(writer,sheet_name=str(int(community_patients)),index=False)
# writer.save()
      


# # Performance evaluation measures on finalised clusters

# In[50]:

final_clusters=[40,47,25,32,21,37,39,34,26,38,28,16] 
checkx_new.head() 


# In[51]:

checkx_new['Total_Patients'].sum() 


# ## Mapping cluster_id back  to patient's euid & Comm NPI
# 

# In[52]:

checkx_new.shape 


# In[53]:

diabetic_imp_clusters=checkx_new[checkx_new['clusters_id'].isin(final_clusters)] 


# In[54]:

diabetic_imp_clusters.head() 


# In[55]:

diabetic_imp_clusters['Total_Patients'].sum() 


# ### changing all values greater !0 to 1(back to binary)

# In[56]:

def f1(x):
    if x!=0:
        return 1
    else:
        return 0
cols=diabetic_imp_clusters.columns.tolist()
cols=cols[2:]
diabetic_imp_clusters[cols]=diabetic_imp_clusters[cols].applymap(f1)
diabetic_imp_clusters.head() 


# In[57]:

print(diabetic_imp_clusters.shape)
print(diabetic_patients_binary.shape) 


# In[58]:

diabetic_patients_binary[:3] 


# In[60]:

#del diabetic_patients_binary['index']
diabetic_imp_clusters[:3]


# ## Merging with patient_label npi to get euid-npi_comm_cluster mapping

# In[61]:

diabetic_patients_binary.reset_index(inplace=True)
cols=diabetic_imp_clusters.columns.tolist()
common_cols=cols[2:] 
diabetic_euid_cluster=pd.merge(diabetic_imp_clusters,diabetic_patients_binary,on=common_cols,how='inner')


# In[62]:

diabetic_euid_cluster.head() 
#so now we have mapping of euid-cluster id


# In[63]:

diabetic_euid_cluster.shape


# In[64]:

#Total patients in finalised 12 cluster
len(diabetic_euid_cluster['new_euid'])


# In[65]:

#checking to see if clusters are mapped correctly
diabetic_euid_cluster.groupby(diabetic_euid_cluster['clusters_id']).new_euid.nunique()


# In[66]:

#Extracting EUID-Cluster_id just
euid_cluster=diabetic_euid_cluster[['new_euid','clusters_id']]
euid_cluster[:2] 


# In[121]:

euid_cluster[:5] 


# In[68]:

patient_label_npi[:2]


# In[69]:

#Now generating euid-npi-cluster_id mapping
euid_npi_cluster=pd.merge(patient_label_npi,euid_cluster,how='inner',on='new_euid') 


# In[70]:

euid_npi_cluster.shape 


# In[71]:

euid_npi_cluster.head() 


# In[72]:

#Checking patients in each community
euid_npi_cluster.groupby(['comm_npi']).new_euid.nunique() 


# # Grouping to see patients in each comm-cluster combination

# In[73]:

euid_npi_cluster_grouped=pd.DataFrame(euid_npi_cluster.groupby(['comm_npi','clusters_id']).new_euid.nunique().sort_values(ascending=False))
euid_npi_cluster_grouped.reset_index(inplace=True) 
euid_npi_cluster_grouped_pivot= euid_npi_cluster_grouped.pivot(index='comm_npi',columns='clusters_id',values='new_euid')
euid_npi_cluster_grouped_pivot['Total_Patients']=euid_npi_cluster_grouped_pivot.sum(axis=1) 
euid_npi_cluster_grouped_pivot.loc['Total']=euid_npi_cluster_grouped_pivot.sum()
euid_npi_cluster_grouped_pivot 


# In[845]:

#writing to csv
# euid_npi_cluster_grouped_pivot.to_csv("patient_number_distribution.csv")


# ## 1) Distribution of diabetic patients cluster within each NPI community

# In[901]:

comm_clust=euid_npi_cluster_grouped_pivot
comm_clust_new=(comm_clust.ix[:6,:12].div(comm_clust['Total_Patients'],axis=0))*100
comm_clust_new=comm_clust_new.round(1) 
comm_clust_new=pd.concat([comm_clust_new,comm_clust['Total_Patients']],axis=1)  
comm_clust_new=comm_clust_new.drop(['Total'])
comm_clust_new=comm_clust_new.append(comm_clust.loc['Total'])


# In[902]:

comm_clust_new


# In[848]:

#Writing this to csv
# comm_clust_new.to_csv("cluster_within_community_patients.csv")


# ## 2) Distribution of NPI comm within each cluster

# In[903]:

clust_comm=euid_npi_cluster_grouped_pivot
clust_comm_new=(clust_comm.ix[:6,:12]/(clust_comm.loc['Total']))*100.0
clust_comm_new=clust_comm_new.round(2)
clust_comm_new=clust_comm_new.append(clust_comm.loc['Total'])
del clust_comm_new['Total_Patients']
clust_comm_new=pd.concat([clust_comm_new,clust_comm['Total_Patients']],axis=1) 
clust_comm_new  


# In[905]:

#writing to csv
# clust_comm_new.to_csv("community_within_cluster.csv")


# ### Adding pmpm_cost to euid-comm-cluster mapping

# In[906]:

# reading data from pmpm_cost
type={'new_euid':'str','cost':'float','months':'float'}
pmpm_cost=pd.read_csv("../../Data/Diabetic_Patient_Clustering/pmpm_cost.csv",dtype=type)


# In[907]:

pmpm_cost.head()


# In[908]:

pmpm_cost.dtypes


# ### Checking length of euid columns

# In[909]:

pmpm_cost.groupby(pmpm_cost['new_euid'].str.len()).agg({'new_euid':np.size})


# ### Cleaning the front 0's from euid 

# In[910]:

pmpm_cost['new_euid'] = pmpm_cost['new_euid'].map(lambda x: str(x).lstrip('0'))
pmpm_cost.groupby(pmpm_cost['new_euid'].str.len()).agg({'new_euid':np.size})


# ### Checking if new_euid is unique in pmpm_cost

# In[853]:

print(pmpm_cost.shape[0])
print(len(pmpm_cost['new_euid'].unique()))  

#it is


# ### Merging with euid-comm_npi-cluster

# In[911]:

euid_npi_cluster[:2] 


# In[912]:

euid_npi_cluster_cost=pd.merge(euid_npi_cluster,pmpm_cost,how='inner')
print(patient_label_npi.shape)
print(euid_npi_cluster_cost.shape) 
euid_npi_cluster_cost.head() 


# ### Adding average monthly cost of each patient 

# In[913]:

euid_npi_cluster_cost['AvgMonthlyCost']=euid_npi_cluster_cost['cost']/euid_npi_cluster_cost['months']
euid_npi_cluster_cost.drop(['cost','months'],axis=1,inplace=True)
euid_npi_cluster_cost=euid_npi_cluster_cost.round(2)
euid_npi_cluster_cost[:2] 


# ### Grouping to see Avg Monthly Cost metrics across comm-clusters 

# In[914]:

euid_npi_cluster_cost_grp=euid_npi_cluster_cost.groupby(['comm_npi','clusters_id']).agg({'new_euid':np.size,'AvgMonthlyCost':np.sum})
euid_npi_cluster_cost_grp.reset_index(inplace=True)
euid_npi_cluster_cost_grp[:2]  


# ### Pivoting for Total patients across patients & communities

# In[915]:

clust_comm= euid_npi_cluster_cost_grp.pivot(index='comm_npi',columns='clusters_id',values='new_euid')
clust_comm['Total_Patients']=clust_comm.sum(axis=1) 
clust_comm.loc['Total']=clust_comm.sum()
clust_comm 


# ### Pivoting for Avg Monthly cost across community-cluster

# In[921]:

euid_npi_clst_cost_grp_piv= euid_npi_cluster_cost_grp.pivot(index='comm_npi',columns='clusters_id',values='AvgMonthlyCost')
comm_clst_cost=euid_npi_clst_cost_grp_piv
comm_clst_cost.loc['AvgMonthCost_clst']=comm_clst_cost.sum()
comm_clst_cost['AvgMonthCost_comm']=comm_clst_cost.sum(axis=1)
comm_clst_cost  


# In[917]:

# writing to csv
# comm_clst_cost.to_csv("community_cluster_cost_distribution.csv")


# ## 1). Cost Distribution of NPI communities across patient clusters

# In[918]:

comm_clst_cost_new=(comm_clst_cost.ix[:6,:12].div(comm_clst_cost['AvgMonthCost_comm'],axis=0))*100
comm_clst_cost_new=comm_clst_cost_new.round(1) 
comm_clst_cost_new=pd.concat([comm_clst_cost_new,comm_clst_cost['AvgMonthCost_comm']],axis=1)  
comm_clst_cost_new=comm_clst_cost_new.drop(['AvgMonthCost_clst'])
comm_clst_cost_new=comm_clst_cost_new.append(comm_clst_cost.loc['AvgMonthCost_clst'])
comm_clst_cost_new=pd.concat([comm_clst_cost_new,clust_comm['Total_Patients']],axis=1)  
comm_clst_cost_new=comm_clst_cost_new.drop(['Total'])
comm_clst_cost_new=comm_clst_cost_new.append(clust_comm.loc['Total']) 


# In[919]:

comm_clst_cost_new 


# In[920]:

#writing to csv
# comm_clst_cost_new.to_csv("cost_communities_across_clusters.csv")


# ## 2). Cost Distribution of clusters across NPI communities 

# In[922]:

comm_clst_cost_new=(comm_clst_cost.ix[:6,:12]/(comm_clst_cost.loc['AvgMonthCost_clst']))*100.0
comm_clst_cost_new=comm_clst_cost_new.round(1) 
#comm_clst_cost_new=pd.concat([comm_clst_cost_new,comm_clst_cost['AvgMonthCost_comm']],axis=1)  
#comm_clst_cost_new=comm_clst_cost_new.drop(['AvgMonthCost_clst']) 
comm_clst_cost_new=comm_clst_cost_new.append(comm_clst_cost.loc['AvgMonthCost_clst'])
del comm_clst_cost_new['AvgMonthCost_comm']
comm_clst_cost_new=pd.concat([comm_clst_cost_new,comm_clst_cost['AvgMonthCost_comm']],axis=1)  
comm_clst_cost_new=pd.concat([comm_clst_cost_new,clust_comm['Total_Patients']],axis=1)  
comm_clst_cost_new=comm_clst_cost_new.drop(['Total']) 
comm_clst_cost_new=comm_clst_cost_new.append(clust_comm.loc['Total'])  


# In[923]:

# Writing to csv
#comm_clst_cost_new


# In[924]:

comm_clst_cost_new.to_csv("cost_cluster_across_communities.csv")


# # Adding Gender ,Pcal,Average Age information to community cluster

# In[939]:

#Reading pmpm to get pcal score
cols=['new_euid','pcal']
type= {'new_euid':'str','pcal':'str'}
pmpm=pd.read_csv("../../Data/pmpm.csv",usecols=cols,dtype=type)


# In[940]:

pmpm.head()


# In[941]:

#checking new_euid length
pmpm.groupby(pmpm['new_euid'].str.len()).agg({'new_euid':np.size})


# In[942]:

pmpm['new_euid']=pmpm['new_euid'].map(lambda x:str(x).lstrip('0'))


# In[943]:

pmpm.groupby(pmpm['new_euid'].str.len()).agg({'new_euid':np.size})


# In[944]:

##Merging with euid_npi_cluster
euid_npi_cluster[:2]


# In[945]:

euid_npi_cluster_pcal=pd.merge(euid_npi_cluster,pmpm,how='inner')


# In[947]:

euid_npi_cluster_pcal[:2]


# In[948]:

euid_npi_cluster_pcal.isnull().sum() 
#perfect (all patients mapped to pcal)


# In[950]:

#Reading Diabetes all claims to get gender,age information
cols=['new_euid','GENDER','yob']
type={'new_euid':'str','GENDER':'str'}
diab_all_claims=pd.read_csv("../../Data/Diabetic_Patient_Clustering/diabetes_all_claims.csv",usecols=cols,dtype=type)


# In[961]:

diab_all_claims[:2]


# In[953]:

diab_all_claims.dtypes


# In[964]:

#stripping front 0's 
diab_all_claims['new_euid']=diab_all_claims['new_euid'].map(lambda x:str(x).lstrip('0'))


# In[954]:

#Adding age
diab_all_claims['Age']=2014-diab_all_claims['yob']+1


# In[958]:

diab_all_claims.head()
diab_all_claims=diab_all_claims[['new_euid','GENDER','Age']]


# In[965]:

### Merging with euid_npi_cluster_pcal
euid_npi_cluster_pcal_demo=pd.merge(euid_npi_cluster_pcal,diab_all_claims) 


# In[966]:

euid_npi_cluster_pcal_demo.head()


# In[968]:

euid_npi_cluster_pcal_demo.isnull().sum()
##Perfect


# In[971]:

#dropping duplicates
df=euid_npi_cluster_pcal_demo
df=df.drop_duplicates()


# In[972]:

df.shape


# In[973]:

df.isnull().sum()


# In[974]:

df.head()


# ### Pivoting for gender distribution across community-cluster

# In[975]:

##Agregating gender count across comm-cluster 
df_female=df.groupby(['comm_npi','clusters_id','GENDER']).size()
df_female.head()


# In[978]:

df_female=pd.DataFrame(df_female)
df_female.reset_index(inplace=True)
df_female.head()


# In[979]:

##Dropping male  
df_female=df_female[df_female['GENDER']=='F']
df_female=df_female.rename(columns = {0:'Total_Female'})
df_female.head()


# In[980]:

df_female_pivot= df_female.pivot(index='comm_npi',columns='clusters_id',values='Total_Female')


# In[981]:

df_female_pivot.head()


# In[986]:

## Rearranging columns as per decreasing avg monthly cost per patient.
cols=[47,34,37,25,16,21,38,32,39,28,26,40]
df_female_pivot=df_female_pivot[cols]
df_female_pivot.head()


# In[987]:

df_female_pivot.to_csv("df_female_pivot.csv")


# ### Pivoting for age,pcal distribution across community-cluster

# In[988]:

df.head()


# In[994]:

df.dtypes


# In[995]:

df['pcal']=df['pcal'].astype(float)


# In[996]:

df_age_pcal=df.groupby(['comm_npi','clusters_id']).agg({'Age':np.sum,'pcal':np.sum})


# In[998]:

df_age_pcal.reset_index(inplace=True)
df_age_pcal.head()


# In[999]:

df_pcal_pivot= df_age_pcal.pivot(index='comm_npi',columns='clusters_id',values='pcal')
df_age_pivot= df_age_pcal.pivot(index='comm_npi',columns='clusters_id',values='Age')
## Rearranging columns as per decreasing avg monthly cost per patient.
cols=[47,34,37,25,16,21,38,32,39,28,26,40]
df_pcal_pivot=df_pcal_pivot[cols] 
df_age_pivot=df_age_pivot[cols]


# In[1000]:

df_pcal_pivot[:2]


# In[1001]:

df_age_pivot[:2]


# In[1002]:

##Rounding to 2 digit
df_pcal_pivot=df_pcal_pivot.round(1)


# In[1003]:

#Writing to csv files
# df_pcal_pivot.to_csv("df_pcal_pivot.csv")
# df_age_pivot.to_csv("df_age_pivot.csv")


# # Defining NPI Communities

# ## Subtask 1: NPI-Community : speciality

# ### Mapping NPI  to NPI-Speciality

# In[1092]:

#Reading diabetic_all_claims only with necessary songs. 
cols=['svc_npi','svc_prov_tax_id','svc_specialty']
types={'svc_npi':'str','svc_prov_tax_id':'str','svc_specialty':'str'}
diabetic_all_claims=pd.read_csv("../../Data/Diabetic_Patient_Clustering/diabetes_all_claims.csv",usecols=cols,dtype=types)


# In[1093]:

diabetic_all_claims.head() 


# In[1094]:

diabetic_all_claims.dtypes


# In[1095]:

diabetic_all_claims.isnull().sum()


# In[1096]:

### Removing all observation where svc_npi='<NA>'
diabetic_all_claims=diabetic_all_claims[diabetic_all_claims['svc_npi']!='<NA>']


# In[1097]:

### Removing null observation
diabetic_all_claims=diabetic_all_claims[diabetic_all_claims['svc_npi'].notnull()]
diabetic_all_claims.isnull().sum()


# In[1098]:

diabetic_all_claims.shape


# In[1099]:

diabetic_all_claims.info() 


# In[1100]:

###Dropping duplicates 
diabetic_all_claims=diabetic_all_claims.drop_duplicates() 
diabetic_all_claims.shape


# In[1047]:

## Unique provider ID
len(diabetic_all_claims['svc_npi'].unique())


# In[1101]:

#Taking most frequent speciality of svc_npi 
from scipy import stats
npi_speciality=diabetic_all_claims[['svc_npi','svc_specialty']].groupby(['svc_npi']).agg(lambda x:stats.mode(x['svc_specialty'])[0])
npi_speciality.reset_index(inplace=True)


# In[1056]:

npi_speciality.head()


# In[1061]:

npi_speciality.shape


# ### Mapping NPI_speciality to NPI-Community_Label

# In[1057]:

#readinf Label from nodeList
nodeList=pd.read_csv("../../Data/Diabetic_Patient_Clustering/nodeList(Cut).csv")


# In[1058]:

nodeList.head()


# In[1063]:

nodeList.dtypes


# In[1064]:

npi_speciality.dtypes


# In[1066]:

##Changing NodeList Id to string
nodeList['Id']=nodeList['Id'].astype('str')


# In[1067]:

#merging to get npi-npi_community-svc_specialty mapping
comm_npi_speciality=pd.merge(nodeList,npi_speciality,left_on="Id",right_on="svc_npi",how="inner")


# In[1069]:

### All comm_npi_speciality mapped
comm_npi_speciality.shape


# In[1070]:

comm_npi_speciality.head()


# In[1071]:

del comm_npi_speciality['Id']


# In[1072]:

comm_npi_speciality.head()


# In[1075]:

#grouping to check major speciality of each label
comm_speciality_summary=comm_npi_speciality.groupby(['Label','svc_specialty']).agg({'svc_npi':np.size})


# In[1076]:

comm_speciality_summary.reset_index(inplace=True)


# In[1077]:

comm_speciality_summary.head()


# In[1081]:

comm_speciality_summary=comm_speciality_summary.sort_values(['Label','svc_npi'],ascending=[False,False])


# In[1082]:

#writing to_csv
# comm_speciality_summary.to_csv("comm_speciality_summary.csv")


# ## Subtask2: NPI-Community:Major Hospital

# In[1083]:

#Reading hospital name from tin_name file provided in Data Dictionary (i,e tax_id:tin name mapping)
tin_name=pd.read_csv("../../Data/Diabetic_Patient_Clustering/tin_name.csv")


# In[1084]:

tin_name.head()


# In[1085]:

tin_name.shape


# In[1086]:

tin_name.dtypes


# In[1102]:

diabetic_all_claims.head()


# In[1103]:

npi_speciality_tin_name=pd.merge(diabetic_all_claims,tin_name,left_on='svc_prov_tax_id',right_on='START')


# In[1104]:

npi_speciality_tin_name.head()


# In[1107]:

npi_speciality_tin_name=npi_speciality_tin_name.drop(['svc_prov_tax_id','svc_specialty','START'],axis=1)


# In[1108]:

npi_speciality_tin_name.head()


# In[1115]:

pd.DataFrame(npi_speciality_tin_name.groupby(['svc_npi']).LABEL.nunique());


# In[1111]:

### Merging with community label 
comm_npi_speciality_tin_name=pd.merge(nodeList,npi_speciality_tin_name,left_on="Id",right_on="svc_npi",how="inner")


# In[1112]:

comm_npi_speciality_tin_name.head()


# In[1116]:

len(comm_npi_speciality_tin_name['svc_npi'].unique())


# In[1117]:

comm_npi_speciality_tin_name.shape


# In[1118]:

comm_speciality_tin_name_summary=comm_npi_speciality_tin_name.groupby(['Label','LABEL']).agg({'svc_npi':np.size})


# In[1119]:

comm_speciality_tin_name_summary.head()


# In[1122]:

comm_speciality_tin_name_summary.reset_index(inplace=True)
comm_speciality_tin_name_summary=comm_speciality_tin_name_summary.sort_values(['Label','svc_npi'],ascending=[True,False])


# In[1123]:

comm_speciality_tin_name_summary.head()


# In[1124]:

# comm_speciality_tin_name_summary.to_csv("comm_tin_name_summary.csv")


# In[1125]:

comm_speciality_summary.head()


# In[1131]:

speciality_summary=comm_speciality_summary.groupby(['svc_specialty']).agg({'svc_npi':np.sum})


# In[1133]:

speciality_summary=speciality_summary.sort_values('svc_npi',ascending=False)


# In[1134]:

# speciality_summary.to_csv("speciality_summary.csv")


# # Adding PQI measurement euid-npi-cluster

# In[74]:

euid_npi_cluster.head()


# In[75]:

euid_pqi=pd.read_csv("../../data/PQI/euid_pqi.csv",dtype={'new_euid':'str','CLAIM_ID':'str'})


# In[76]:

euid_pqi.head()


# In[77]:

euid_pqi.shape


# In[78]:

len(euid_pqi['new_euid'].unique())


# In[79]:

euid_pqi.dtypes


# In[80]:

# Merging euid_npi_cluster information with pqi
euid_npi_cluster_pqi=pd.merge(euid_npi_cluster,euid_pqi,on="new_euid",how="left")


# In[82]:

euid_npi_cluster_pqi.head()


# In[89]:

len(euid_npi_cluster_pqi['new_euid'].unique())


# In[90]:

len(euid_npi_cluster_pqi[euid_npi_cluster_pqi['CLAIM_ID'].isnull()].new_euid.unique())


# In[91]:

6489-5764
#So only 725 patients have PQI 


# In[92]:

euid_npi_cluster_pqi.shape


# In[94]:

euid_npi_cluster_pqi=euid_npi_cluster_pqi.drop_duplicates()


# In[95]:

euid_npi_cluster_pqi.shape


# ### Distribution of  725 patients across community-cluster

# In[96]:

euid_npi_cluster_pqi_725=euid_npi_cluster_pqi[euid_npi_cluster_pqi['CLAIM_ID'].notnull()]
euid_npi_cluster_pqi_725.head()


# In[97]:

euid_npi_cluster_pqi_725_grp=euid_npi_cluster_pqi_725.groupby(['comm_npi','clusters_id']).agg({'new_euid':pd.Series.nunique})
euid_npi_cluster_pqi_725_grp.reset_index(inplace=True)
euid_npi_cluster_pqi_725_grp[:2]  


# In[118]:

euid_npi_cluster_pqi_725_claim_grp=euid_npi_cluster_pqi_725.groupby(['comm_npi','clusters_id']).agg({'CLAIM_ID':pd.Series.nunique})
euid_npi_cluster_pqi_725_claim_grp.reset_index(inplace=True)
euid_npi_cluster_pqi_725_claim_grp[:2]  


# In[120]:

clust_comm_claim= euid_npi_cluster_pqi_725_claim_grp.pivot(index='comm_npi',columns='clusters_id',values='CLAIM_ID')
clust_comm_claim['Total_Claims']=clust_comm_claim.sum(axis=1) 
clust_comm_claim.loc['Total_Claims']=clust_comm_claim.sum()
clust_comm_claim.to_csv("clust_comm_claim.csv")


# In[ ]:




# In[98]:

clust_comm= euid_npi_cluster_pqi_725_grp.pivot(index='comm_npi',columns='clusters_id',values='new_euid')
clust_comm['Total_Patients']=clust_comm.sum(axis=1) 
clust_comm.loc['Total']=clust_comm.sum()
clust_comm 


# In[99]:

# clust_comm.to_csv("725_cluster_community_distribution.csv")


# ### Analyzing PQI 1

# In[100]:

euid_npi_cluster_pqi_725.head()


# In[116]:

euid_npi_cluster_pqi_725_PQI=euid_npi_cluster_pqi_725[euid_npi_cluster_pqi_725['TAPQ08']!=0.0].groupby(['comm_npi','clusters_id']).agg({'CLAIM_ID':pd.Series.nunique,'new_euid':pd.Series.nunique})
euid_npi_cluster_pqi_725_PQI.reset_index(inplace=True) 

##Pivoting for claim
clust_comm_claim= euid_npi_cluster_pqi_725_PQI.pivot(index='comm_npi',columns='clusters_id',values='CLAIM_ID')
clust_comm_claim['Total_claims']=clust_comm_claim.sum(axis=1) 
clust_comm_claim.loc['Total_claims']=clust_comm_claim.sum()
clust_comm_claim.to_csv("claim_pqi8.csv")

 
##Pivoting for new_euid 
clust_comm_euid= euid_npi_cluster_pqi_725_PQI.pivot(index='comm_npi',columns='clusters_id',values='new_euid')
clust_comm_euid['Total_patients_with_claims']=clust_comm_euid.sum(axis=1) 
clust_comm_euid.loc['Total_patients_with_claims']=clust_comm_euid.sum()
clust_comm_euid.to_csv("euid_pqi8.csv") 


# In[ ]:



