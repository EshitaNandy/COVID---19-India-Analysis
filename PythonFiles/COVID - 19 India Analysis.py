#!/usr/bin/env python
# coding: utf-8

# # CORONAVIRUS ANALYSIS IN INDIA
# 
# ## Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
# 
# - Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  
# - Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.
# 
# - The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).
# 
# - The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. 
# - Protecting oneself and others from infection by washing our hands or using an alcohol based rub frequently and not touching our face. 

# ## To prevent infection and to slow transmission of COVID-19, do the following:
# 
# - Washing our hands regularly with soap and water, or cleaning them with alcohol-based hand rub.
# - Maintaining at least 1.5 metre distance between ourselves and people coughing or sneezing.
# - Avoid touching our face.
# - Covering our mouth and nose when coughing or sneezing.
# - Staying home if we feel unwell.
# - Refrain from smoking and other activities that weaken the lungs.
# - Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people.

# ## Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import sys
import matplotlib as plt
from matplotlib.pyplot import *
import plotly.offline as plo
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import bar_chart_race as bcr
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")
from IPython.display import Video


# # Exploratory Data Analysis and Data Visualization

# ## Importing and Reading the Dataset
# covid_19_india.csv

# In[2]:


data = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\covid_19_india.csv")


# ## Displaying the Dataset

# In[3]:


data.head(10)


# ## Displaying the Dataset Columns

# In[4]:


data.columns


# ## Displaying the Dataset Information

# In[5]:


data.info()


# ## Displaying the Dataset Description

# In[6]:


data.describe()


# ## Checking presence of some null values in the Dataset

# In[7]:


data.isnull().sum()


# ## Changing the Date Format

# In[8]:


data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data.head()


# ## Sorting values of Confirmed Cases in descending order depending on the State/Union Territory

# In[9]:


data3 = pd.pivot_table(data, values=['Confirmed','Deaths','Cured'], index='State/UnionTerritory', aggfunc='max')
data3 = data3.sort_values(by='Confirmed', ascending= False)
data3.style.background_gradient(cmap='Wistia')


# ## Total Cases in India

# In[10]:


print("Total Cases in India:",int(data3['Confirmed'].sum()))


# ## Representation using Bar Chart Plotting

# In[11]:


data4 = [go.Bar(
    x = data3.index,
    y = data3[colname],
    name = colname
)for colname in data3.columns]

fig = go.Figure(data=data4)

plo.iplot(fig)


# ## Confirmed Cases in the topmost five States - Graphical Representation

# In[12]:


def plotly_graph_state(state):
    temp = data[data['State/UnionTerritory']==state]
    trace0 = go.Scatter(
        x = temp.index,
        y = temp['Confirmed'],
        mode = 'lines+markers',
        marker = dict(color='green'),
        name = 'Confirmed Cases in {0}'.format(state)
    )
    layout = go.Layout(
        title = 'Confirmed Cases in {0}'.format(state)
    )
    fig = go.Figure(
        data = [trace0],
        layout = layout
    )
    plo.iplot(fig)


# In[13]:


all_states = list(data3.sort_values(by='Confirmed', ascending= False).index[:5])
for state in all_states:
    plotly_graph_state(state)


# ## Scatter Plotting using Dots depending on various factors 

# In[14]:


sns.relplot(x="Cured", y="Confirmed", hue = "State/UnionTerritory", data=data)


# People are recovering at a faster side

# In[15]:


sns.relplot(x="Confirmed", y="Deaths", hue = "State/UnionTerritory", data=data)


# The death rate is much lower in India

# In[16]:


sns.relplot(x="ConfirmedIndianNational", y="Confirmed", hue = "State/UnionTerritory", data=data)


# Initially most case were detected in Foreign Nationals but as days flew by no. of cases in Indian Nationals turned out to be more and more.

# In[17]:


sns.pairplot(data)


# The scatter plotting is a bit confusing to get the representation. Actually, it provides an overall representation of the whole dataset.

# ## Scatter Plotting using Lines depending on various factors 

# In[18]:


sns.relplot(x='Cured',y='Confirmed', kind='line', hue='State/UnionTerritory',  data=data)


# ## Importing and Reading the Dataset
# AgeGroupDetails.csv

# In[19]:


data1 = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\AgeGroupDetails.csv")


# In[20]:


data1.head(10)


# In[21]:


data1.columns


# ## Representation of the dataset using Pie Chart

# In[22]:


import matplotlib.ticker as ticker
import matplotlib.cm as cm
import matplotlib as mpl
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


labels = list(data1['AgeGroup'])
sizes = list(data1['TotalCases'])
explode = []
for i in labels:
    explode.append(0.05)    
plt.figure(figsize= (15,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=9, explode =explode)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('India - Age Group wise Distribution',fontsize = 20)
plt.axis('equal')  
plt.tight_layout()


# ## Importing and Reading the Dataset
# HospitalBedsIndia.csv

# In[24]:


data2 = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\HospitalBedsIndia.csv")


# In[25]:


data2.head(10)


# In[26]:


data2.columns


# ## Analysing the various factors present in the Dataset using Visual / Graphical Representation

# In[27]:


data4 = pd.pivot_table(data2, values=['TotalPublicHealthFacilities_HMIS','NumPrimaryHealthCenters_HMIS','NumCommunityHealthCenters_HMIS','NumSubDistrictHospitals_HMIS','NumDistrictHospitals_HMIS'], index='State/UT', aggfunc='max')
data4 = data4.sort_values(by='TotalPublicHealthFacilities_HMIS',ascending= False)
data4.style.background_gradient(cmap='Wistia')


# In[28]:


labels = list(data2['State/UT'])
sizes = list(data2['TotalPublicHealthFacilities_HMIS'])
explode = []
for i in labels:
    explode.append(0.05)    
plt.figure(figsize= (15,10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=9, explode =explode)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('India - Hospital Bed wise Distribution',fontsize = 20)
plt.axis('equal')  
plt.tight_layout()


# In[29]:


sns.pairplot(data2)


# ## Importing and Reading the Dataset
# StatewiseTestingDetails.csv

# In[30]:


data5 = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\StatewiseTestingDetails.csv")
data5.head()


# In[31]:


data5.columns


# In[32]:


data6=data5.drop(['Date'],axis='columns')  
data6.head()


# In[33]:


data6 = pd.pivot_table(data6, values=['TotalSamples'], index='State', aggfunc='max')
data6 = data6.sort_values(by='State',ascending= True)
data6.style.background_gradient(cmap='Wistia')


# In[34]:


matplotlib.rcParams["figure.figsize"] = (20,10)
plt.hist(data6,rwidth=0.8)
plt.xlabel("State")
plt.ylabel("TotalSamples")


# ## Importing and Reading the Dataset
# - For Indian Coordinates - longitude and latitude values of all states </br>
# - Covid19 Analysis - Name of State / UT	Total Confirmed cases	Active	Cured/Discharged/Migrated	Deaths

# In[35]:


ic = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\datasets_555917_1128483_Indian Coordinates.csv")
ic.head()


# In[36]:


cc = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\datasets_555917_1128483_Covid cases in India.csv")
cc.head()


# ## Map Plotting

# In[37]:


df_full = pd.merge(ic,cc,on='Name of State / UT')
map = folium.Map(location=[20, 80], zoom_start=1,tiles='Stamen Toner')

for lat, lon, value, name in zip(df_full['Latitude'], df_full['Longitude'], df_full['Active'], df_full['Name of State / UT']):
    folium.CircleMarker([lat, lon],
                        radius=value*0.002,
                        popup = ('<strong>State</strong>: ' + str(name).capitalize() + '<br>'
                                '<strong>Active Cases</strong>: ' + str(value) + '<br>'),
                        color='red',
                        
                        fill_color='red',
                        fill_opacity=0.3 ).add_to(map)
map


# In[38]:


get_ipython().run_cell_magic('HTML', '', "<div class='tableauPlaceholder' id='viz1588697469217' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;44&#47;44JW7JNG3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;44JW7JNG3' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;44&#47;44JW7JNG3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1588697469217');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1477px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>")


# ## Bar Plotting depending on the Map Data

# In[39]:


f, ax = plt.subplots(figsize=(12, 8))
data8 = df_full[['Name of State / UT','Total Confirmed cases','Cured/Discharged/Migrated','Deaths']]
data8.sort_values('Total Confirmed cases',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Total Confirmed cases", y="Name of State / UT", data=data8,
            label="Total", color="r")

sns.set_color_codes("muted")
sns.barplot(x="Cured/Discharged/Migrated", y="Name of State / UT", data=data8,
            label="Recovered", color="g")


# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 10000), ylabel="",
       xlabel="Cases")
sns.despine(left=True, bottom=True)


# ## How the Coronavirus cases are rising?

# In[40]:


import pandas as pd
data9 = pd.read_excel(r'D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\datasets_555917_1128483_per_day_cases.xlsx',sheet_name='India')
data9.head()


# In[41]:


# Rise in COVID-19 cases in India
fig = go.Figure()
fig.add_trace(go.Scatter(x=data9['Date'], y=data9['Total Cases'],
                    mode='lines+markers',name='Total Cases'))

fig.add_trace(go.Scatter(x=data9['Date'], y=data9['New Cases'], 
                mode='lines',name='New Cases'))

        
    
fig.update_layout(title_text='Trend of Coronavirus Cases in India(Cumulative cases)',plot_bgcolor='rgb(250, 242, 242)')

fig.show()


# New COVID-19 cases reported daily in India

import plotly.express as px
fig = px.bar(data9, x="Date", y="New Cases", barmode='group',
             height=400)
fig.update_layout(title_text='New Coronavirus Cases in India per day',plot_bgcolor='rgb(250, 242, 242)')

fig.show()


# In[42]:


fig = px.bar(data9, x="Date", y="Total Cases", color='Total Cases', orientation='v', height=600,
             title='Confirmed Cases in India', color_discrete_sequence = px.colors.cyclical.mygbm)

fig.update_layout(plot_bgcolor='rgb(250, 242, 242)')
fig.show()


# In[43]:


from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=2,
    specs=[[{}, {}],
           [{"colspan": 2}, None]],
    #subplot_titles=("India")
)
fig.add_trace(go.Scatter(x=data9['Date'], y=data9['Total Cases'],
                    marker=dict(color=data9['Total Cases'], coloraxis="coloraxis")),
              2, 1)

fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False,title_text="Trend of Coronavirus cases")

fig.update_layout(plot_bgcolor='rgb(250, 242, 242)')
fig.show()


# ## Importing and Reading the Dataset
# IndividualDetails.csv

# In[44]:


data10 = pd.read_csv(r"D:\DATA SCIENCE\Covid19 analysis\557629_1323860_bundle_archive\IndividualDetails.csv")
data10.head()


# In[45]:


sns.countplot(y='gender', data=data10)
plt.show()


# In[46]:


data10 = data10.detected_state.value_counts()
sns.barplot(y = data10.index, x = data10, orient='h');


# # Stay Home Stay Safe
