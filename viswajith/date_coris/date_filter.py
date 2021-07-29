import pandas as pd
import glob
import os
import sys

#sys.argv

cwd = os.getcwd()
dm = str(sys.argv[1])
print('--------------- starting execution -----------')
all_files = glob.glob(cwd + "/*.csv")
li = []
ln = len(all_files)
df_old = pd.read_csv(all_files[0])
df_old = df_old[[dm]]
i = 0
for filename in all_files:
    sep = 'date_coris/'
    strip2 = filename.split(sep, 1)[1]
    #sep2 = '.'
    #strip2 = strip.split(sep2, 1)[0]
    globals()['%s' % strip2] = pd.read_csv(filename, index_col=None, header=0)
    df_new = pd.read_csv(all_files[i])
    int_df = pd.merge(df_new, df_old, how ='inner', on =[dm]) 
    df_old = int_df[[dm]]
    print(i)
    i = i + 1
    li.append('%s' % strip2)
    print(['%s' % strip2])
     
print('------------------------------writing-------------------------')
print(ln)
print('-----------------------results, into a folder ---------------------------')

i = 0    
while (i<ln):
    df_print = pd.read_csv(li[0])
    df_print = pd.merge(df_print, df_old, how ='inner', on =[dm])
    df_print.to_csv(cwd + '/results/' + li[i])
    print(i)
    i = i +1
    

print('Done, please check the results')
