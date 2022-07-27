import pandas as pd

# UNI DATA

#read csv
df = pd.read_csv('./universities-intake-enrolment-and-graduates-by-course.csv')
#remove comma from numbers in graduates column
df['graduates'] = df['graduates'].str.replace(',', '')

#filter out IT course and MF sex
filtered = df[(df.course=="Information Technology") & (df.sex=="MF")]

#save to csv without the first column index
filtered.to_csv('./filtereduni.csv', index=False)

unidf = pd.read_csv('./filtereduni.csv')
print(unidf)
#sum total of uni IT graduates
TotalUni = unidf['graduates'].sum()
print (f"Total Uni graduates: {TotalUni}")
#write total to unidf
unidf.loc['TotalUni'] = pd.Series(unidf['graduates'].sum(), index = ['graduates'])
unidf.to_csv('./finaluni.csv', index=False)

# POLY DATA

df2 = pd.read_csv('./polytechnics-intake-enrolment-and-graduates-by-course.csv')
df2['graduates'] = df2['graduates'].str.replace(',', '')

#filter out IT course and MF sex
filtered2 = df2[(df2.course=="Information Technology") & (df2.sex=="MF")]

#save to csv
filtered2.to_csv('./filteredpoly.csv', index=False)

polydf = pd.read_csv('./filteredpoly.csv')
print(polydf)
TotalPoly = polydf['graduates'].sum()
print (f"Total Poly graduates: {TotalPoly}")
polydf.loc['TotalPoly'] = pd.Series(polydf['graduates'].sum(), index = ['graduates'])
polydf.to_csv('./finalpoly.csv', index=False)

GrandTotal = TotalPoly + TotalUni
print(f"Total IT graduates in Uni and Poly: {GrandTotal}")