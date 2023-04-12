import streamlit as stream
import pandas as pd
import numpy as np
import mysql.connector as mysql
import plotly.express as px
#import plotly.graph_objects as go
import json


new_title = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;">PhonePe Pulse Data Visualization</p>'
stream.markdown(new_title, unsafe_allow_html=True)   
add_selectbox = stream.sidebar.selectbox(
    "Select any one",
    ("Transaction", "User")
)
add_selectbox1 = stream.sidebar.selectbox(
    "Select any one",
    ('View Data','View Statistic Plots','View Map')
)

def qwer(g,h,n,m,f):
    r=(g[h][n]).strip('district')
    if r=='east godavari ':
        m.append('East Godavari')
        f()
    elif r=='west godavari ':
        m.append('West Godavari')
        f()
    elif r=='hittoor ':
        m.append('Chittoor')
        f()
    elif r=='ysr ':
        m.append('Cuddapah')
        f()
    elif r=='psr nellore ':
        m.append('Nellore')
        f()
    elif r=='kakulam ':
        m.append('Srikakulam')
        f()
    elif r=='visakhapatnam ':
        m.append('Vishakhapatnam')
        f()
    elif r=='nsukia ':
        m.append('Tinsukia')
        f()
    elif r=='karbi anglong ':
        m.append('Karbi Anglong')
        f()
    elif r=='vasagar ':
        m.append('Sibsagar')
        f()
    elif r=='brugarh ':
        m.append('Dibrugarh')
        f()
    elif r=='hubri ':
        m.append('Dhuburi')
        f()
    elif r=='onitpur ':
        m.append('Sonitpur')
        f()
    elif r=='achar ':
        m.append('Cachar')
        f()
    elif r=='hemaji ':
        m.append('Dhemaji')
        f()
    elif r=='arrang ':
        m.append('Darrang')
        f()
    
    elif r=='upaul ':
        m.append('Supaul')
        f()
    elif r=='ohtas ':
        m.append('Rohtas')
        f()
    elif r=='wan ':
        m.append('Siwan')
        f()
    elif r=='heikhpura ':
        m.append('Sheikhpura')
        f()
    elif r=='arbhanga ':
        m.append('Darbhanga')
        f()
    elif r=='amarhi ':
        m.append('Sitamarhi')
        f()
    elif r=='aran ':
        m.append('Saran')
        f()
    elif r=='pashchim champaran ':
        m.append('Pashchim Champaran')
        f()
    elif r=='kaimur bhabua ':
        m.append('Bhabua')
        f()
    elif r=='amastipur ':
        m.append('Samastipur')
        f()
    elif r=='purbi champaran ':
        m.append('Purba Champaran')
        f()
    elif r=='heohar ':
        m.append('Sheohar')
        f()
    elif r=='handigarh ':
        m.append('Chandigarh')
        f()
    elif r=='hamtari ':
        m.append('Dhamtari')
        f()
    elif r=='urg ':
        m.append('Durg')
        f()
    elif r=='janjgir champa ':
        m.append('Janjgir-Champa')
        f()
    elif r=='urguja ':
        m.append('Surguja')
        f()
    elif r=='antewada ':
        m.append('Dantewada')
        f()
    elif r=='ajnandgaon ':
        m.append('Raj Nandgaon')
        f()
    elif r=='aipur ':
        m.append('Raipur')
        f()
    elif r=='korea ':
        m.append('Koriya')
        f()
    elif r=='north goa ':
        m.append('North Goa')
        f()
    elif r=='outh goa ':
        m.append('South Goa')
        f()
    elif r=='ajkot ':
        m.append('Rajkot')
        f()
    elif r=='he dangs ':
        m.append('The Dangs')
        f()
    elif r=='urat ':
        m.append('Surat')
        f()
    elif r=='panch mahals ':
        m.append('Panch Mahals')
        f()
    elif r=='banas kantha ':
        m.append('Banas Kantha')
        f()
    elif r=='urendranagar ':
        m.append('Surendranagar')
        f()
    elif r=='olan ':
        m.append('Solan')
        f()
    elif r=='maur ':
        m.append('Sirmaur')
        f()
    elif r=='himla ':
        m.append('Shimla')
        f()
    elif r== 'lahul and spiti ':
        m.append('Lahul and Spiti')
        f()
    elif r== 'hamba ':
        m.append( 'Chamba')
        f()
    elif r=='yamunanagar ':
        m.append('Yamuna Nagar')
        f()
    elif r=='onipat ':
        m.append('Sonepat')
        f()
    elif r=='ohtak ':
        m.append('Rohtak')
        f()
    elif r=='ewari ':
        m.append('Rewari')
        f()
    elif r=='ewari ':
        m.append('Rewari')
        f()
    elif r=='gurugram ':
        m.append('Gurgaon')
        f()
    elif r=='a ':
        m.append('Sirsa')
        f()
    elif r=='muzaffarabad ':
        m.append('Kupwara (Muzaffarabad)')
        f()
    elif r=='oda ':
        m.append('Doda')
        f()
    elif r=='nagar ':
        m.append('Srinagar')
        f()
    elif r=='baramulla ':
        m.append('Baramula (Kashmir North)')
        f()
    elif r=='poonch ':
        m.append('Punch')
        f()
    elif r=='ajouri ':
        m.append('Rajauri')
        f()
    elif r=='budgam ':
        m.append('Bagdam')
        f()
    elif r=='anantnag ':
        m.append('Anantnag (Kashmir South)')
        f()
    elif r=='anchi ':
        m.append('Ranchi')
        f()
    elif r=='umka ':
        m.append('Dumka')
        f()
    elif r=='hazaribagh ':
        m.append('Hazaribag')
        f()
    elif r=='mdega ':
        m.append('Simdega')
        f()
    elif r=='araikela kharsawan ':
        m.append('Saraikela Kharsawan')
        f()
    elif r=='hanbad ':
        m.append('Dhanbad')
        f()
    elif r=='hatra ':
        m.append('Chatra')
        f()
    elif r=='eoghar ':
        m.append('Deoghar')
        f()
    
    elif r=='east singhbhum ':
        m.append('Purba Singhbhum')
        f()
    elif r=='west singhbhum ':
        m.append('Pashchim Singhbhum')
        f()
    elif r=='ahebganj ':
        m.append('Sahibganj')
        f()
    
    elif r=='hitradurga ':
        m.append('Chitradurga')
        f()
    elif r=='hikkamagaluru ':
        m.append('Chikmagalur')
        f()
    elif r=='ballari ':
        m.append('Bellary')
        f()
    elif r=='uttara kannada ':
        m.append('Uttar Kannand')
        f()
    elif r== 'bengaluru urban ':
        m.append('Bangalore Urban')
        f()
    elif r=='avanagere ':
        m.append('Davanagere')
        f()
    elif r== 'bagalkote ':
        m.append('Bagalkot')
        f()
    elif r=='bengaluru rural ':
        m.append('Bangalore Rural')
        f()
    elif r=='aichur ':
        m.append('Raichur')
        f()
    elif r=='akshina kannada ':
        m.append('Dakshin Kannad')
        f()
    elif r== 'hamarajanagara ':
        m.append('Chamrajnagar')
        f()
    elif r=='harwad ':
        m.append('Dharwad')
        f()
    elif r== 'hivamogga ':
        m.append('Shimoga')
        f()
    elif r== 'kalaburagi ':
        m.append('Gulbarga')
        f()
    elif r=='hiruvananthapuram ':
        m.append('Thiruvananthapuram')
        f()
    elif r=='pathanamthitta ':
        m.append('Pattanamtitta')
        f()
    elif r=='hrissur ':
        m.append('Thrissur')
        f()
    elif r=='ukki ':
        m.append('Idukki')
        f()
    elif r=='leh ladakh ':
        m.append('Ladakh (Leh)')
        f()
    elif r=='ehore ':
        m.append('Sehore')
        f()
    elif r=='ajgarh ':
        m.append('Rajgarh')
        f()
    elif r=='hi ':
        m.append('Sidhi')
        f()
    elif r=='atia ':
        m.append('Datia')
        f()
    elif r=='ewas ':
        m.append('Dewas')
        f()
    elif r=='aisen ':
        m.append('Raisen')
        f()
    elif r=='heopur ':
        m.append('Sheopur')
        f()
    elif r=='ndori ':
        m.append('Dindori')
        f()
    elif r=='hivpuri ':
        m.append('Shivpuri')
        f()
    elif r=='agar ':
        m.append('Sagar')
        f()
    elif r=='ewa ':
        m.append('Rewa')
        f()
    elif r=='hajapur ':
        m.append('Shajapur')
        f()
    elif r=='kamgarh ':
        m.append('Tikamgarh')
        f()
    elif r=='eoni ':
        m.append('Seoni')
        f()
    elif r=='har ':
        m.append('Dhar')
        f()
    elif r=='east nimar ':
        m.append('East Nimar')
        f()
    elif r=='hhindwara ':
        m.append('Chhindwara')
        f()
    elif r=='ndore ':
        m.append('Indore')
        f()
    elif r=='amoh ':
        m.append('Damoh')
        f()
    elif r=='hahdol ':
        m.append('Shahdol')
        f()
    elif r=='atlam ':
        m.append('Ratlam')
        f()
    elif r=='hhatarpur ':
        m.append('Chhatarpur')
        f()
    elif r=='hane ':
        m.append('Thane')
        f()
    elif r=='handrapur ':
        m.append('Chandrapur')
        f()
    elif r=='mumbai ':
        m.append('Greater Bombay')
        f()
    elif r=='ndhudurg ':
        m.append('Sindhudurg')
        f()
    elif r=='hule ':
        m.append('Dhule')
        f()
    elif r== 'atnagiri ':
        m.append('Ratnagiri')
        f()
    elif r=='angli ':
        m.append('Sangli')
        f()
    elif r== 'gadchiroli ':
        m.append('Garhchiroli')
        f()
    elif r=='atara ':
        m.append('Satara')
        f()
    elif r=='olapur ':
        m.append('Solapur')
        f()
    elif r=='beed ':
        m.append('Bid')
        f()
    elif r=='erchhip ':
        m.append('Serchhip')
        f()
    elif r=='hamphai ':
        m.append('Champhai')
        f()
    elif r=='aiha ':
        m.append('Saiha')
        f()
    elif r=='east garo hills ':
        m.append('East Garo Hills')
        f()
    elif r=='east khasi hills ':
        m.append('East Khasi Hills')
        f()
    elif r=='west jaintia hills ':
        m.append('Jaintia Hills')
        f()
    elif r=='bhoi ':
        m.append('Ri-Bhoi')
        f()
    elif r=='outh garo hills ':
        m.append('South Garo Hills')
        f()
    elif r=='west garo hills ':
        m.append('West Garo Hills')
        f()
    elif r=='west khasi hills ':
        m.append('West Khasi Hills')
        f()
    elif r=='uensang ':
        m.append('Tuensang')
        f()
    elif r=='mapur ':
        m.append('Dimapur')
        f()
        
    elif r== 'ayagada ':
        m.append('Rayagada')
        f()
    elif r== 'ambalpur ':
        m.append('Sambalpur')
        f()
    elif r== 'anugul ':
        m.append('Angul')
        f()
    elif r== 'jajapur ':
        m.append('Jajpur')
        f()
    elif r== 'bargarh ':
        m.append('Baragarh')
        f()
    elif r== 'henkanal ':
        m.append('Dhenkanal')
        f()
    elif r== 'kendujhar ':
        m.append('Keonjhar')
        f()
    elif r== 'eogarh ':
        m.append('Deogarh')
        f()
    elif r== 'undargarh ':
        m.append('Sundargarh')
        f()
    elif r== 'jagatsinghapur ':
        m.append('Jagatsinghpur')
        f()
    elif r== 'balangir ':
        m.append('Bolangir')
        f()
    elif r== 'onepur ':
        m.append('Sonepur')
        f()
    elif r== 'uttack ':
        m.append('Cuttack')
        f()
    elif r== ' muktsar sahib ':
        m.append('Muktsar')
        f()
    elif r==  'fatehgarh sahib ':
        m.append('Fatehgarh Sahib')
        f()
    elif r== 'upnagar ':
        m.append('Rupnagar')
        f()
    elif r== 'angrur ':
        m.append('Sangrur')
        f()
    elif r==  'firozepur ':
        m.append('Firozpur')
        f()
    
    elif r== 'huru ':
        m.append('Churu')
        f()
    elif r== 'ungarpur ':
        m.append('Dungarpur')
        f()
    elif r==  'onk ':
        m.append('Tonk')
        f()
    elif r==  'ausa ':
        m.append('Dausa')
        f()
    elif r==  'hittorgarh ':
        m.append( 'Chittaurgarh')
        f()
    elif r==  'jhunjhunu ':
        m.append('Jhunjhunun')
        f()
    elif r== 'outh ':
        m.append('South Sikkim')
        f()
    elif r== 'west ':
        m.append('West Sikkim')
        f()
    elif r== 'north ':
        m.append('North Sikkim')
        f()
    elif r== 'uchirappalli ':
        m.append('Tiruchchirappalli')
        f()
    elif r== 'amanathapuram ':
        m.append('Ramanathapuram')
        f()
    elif r== 'uddalore ':
        m.append('Cuddalore')
        f()
    elif r=='harmapuri ':
        m.append('Dharmapuri')
        f()
    elif r== 'hanjavur ':
        m.append('Thanjavur')
        f()
    elif r== 'hoothukkudi ':
        m.append('Thoothukudi')
        f()
    elif r=='uvannamalai ':
        m.append('Tiruvannamalai')
        f()
    elif r== 'alem ':
        m.append('Salem')
        f()
    elif r== 'hennai ':
        m.append('Chennai')
        f()
    elif r=='he nilgiris ':
        m.append('Nilgiris')
        f()
    elif r== 'viluppuram ':
        m.append('Villupuram')
        f()
    elif r==  'oimbatore ':
        m.append('Coimbatore')
        f()
    elif r=='heni ':
        m.append('Theni')
        f()
    elif r== 'ndigul ':
        m.append('Dindigul')
        f()
    elif r==  'vaganga ':
        m.append( 'Sivaganga')
        f()
    elif r=='unelveli ':
        m.append('Tirunelveli Kattabo')
        f()
    elif r== 'hiruvarur ':
        m.append( 'Thiruvarur')
        f()
    elif r==  'mphal east ':
        m.append('East Imphal')
        f()
    elif r==  'houbal ':
        m.append('Thoubal')
        f()
    elif r==  'amenglong ':
        m.append('Tamenglong')
        f()
    elif r== 'handel ':
        m.append('Chandel')
        f()
    elif r== 'enapati ':
        m.append('Senapati')
        f()
    elif r== 'hurachandpur ':
        m.append('Churachandpur')
        f()
    elif r== 'mphal west ':
        m.append('West Imphal')
        f()

    #uttarkhand    
    elif r== 'udham singh nagar ':
        m.append('Udham Singh Nagar')
        f()
    elif r== 'hampawat ':
        m.append('Champawat')
        f()
    elif r== 'nainital ':
        m.append('Naini Tal')
        f()
    elif r== 'ehradun ':
        m.append( 'Dehra Dun')
        f()
    elif r== 'hamoli ':
        m.append('Chamoli')
        f()
    elif r== 'pauri garhwal ':
        m.append( 'Pauri Garhwal')
        f()
    elif r== 'ehri garhwal ':
        m.append( 'Tehri Garhwal')
        f()
    elif r== 'udraprayag ':
        m.append( 'Rudra Prayag')
        f()
        
    #westbengal
    elif r== 'outh twenty four parganas ':
        m.append( 'South 24 Parganas')
        f()
    elif r== 'purba bardhaman ':
        m.append( 'Barddhaman')
        f()
    elif r== 'uttar dinajpur ':
        m.append( 'Uttar Dinajpur')
        f()
    elif r== 'paschim medinipur ':
        m.append( 'West Midnapore')
        f()
    elif r== 'akshin dinajpur ':
        m.append( 'Dakshin Dinajpur')
        f()
    elif r== 'purulia ':
        m.append( 'Puruliya')
        f()
    elif r==  'north twenty four parganas ':
        m.append( 'North 24 Parganas')
        f()
    elif r== 'hooghly ':
        m.append( 'Hugli')
        f()
    elif r== 'howrah ':
        m.append( 'Haora')
        f()
    elif r==  'koch bihar ':
        m.append( 'Kochbihar')
        f()
    elif r== 'purba medinipur ':
        m.append( 'East Midnapore')
        f()
    elif r== 'arjiling ':
        m.append( 'Darjiling')
        f()
        
    elif r== 'kanpur nagar ':
        m.append( 'Kanpur')
        f()
    elif r== 'ant kabeer nagar ':
        m.append('Sant Kabir Nagar')
        f()
    elif r== 'budaun ':
        m.append( 'Badaun')
        f()
    elif r== 'hahjahanpur ':
        m.append( 'Shahjahanpur')
        f()
    elif r=='ambedkar nagar ':
        m.append('Ambedkar Nagar')
        f()
    elif r== 'hravasti ':
        m.append( 'Shravasti')
        f()
    elif r== 'gautam buddha nagar ':
        m.append('Gautam Buddha Nagar')
        f()
    elif r== 'kanpur dehat ':
        m.append( 'Kanpur Dehat')
        f()
    elif r== 'hitrakoot ':
        m.append( 'Chitrakoot')
        f()
    elif r=='handauli ':
        m.append('Chandauli')
        f()
    elif r== 'aharanpur ':
        m.append( 'Saharanpur')
        f()
    elif r=='bara banki ':
        m.append('Bara Banki')
        f()
    elif r== 'ultanpur ':
        m.append( 'Sultanpur')
        f()
    elif r=='ae bareli ':
        m.append('Rae Bareli')
        f()
    elif r== 'eoria ':
        m.append( 'Deoria')
        f()
    elif r=='kheri ':
        m.append('Lakhimpur Kheri')
        f()
    elif r== 'ampur ':
        m.append( 'Rampur')
        f()
    elif r=='apur ':
        m.append('Sitapur')
        f()
    elif r== 'onbhadra ':
        m.append( 'Sonbhadra')
        f()
    elif r=='amroha ':
        m.append('Sant Ravi Das Nagar')
        f()
    elif r=='prayagraj ':
        m.append('Siddharth Nagar')
        f()
        
    #tripura
    elif r=='halai ':
        m.append('Dhalai')
        f()
    elif r== 'north tripura ':
        m.append(  'North Tripura')
        f()
    elif r=='West Tripura':
        m.append('Sant Ravi Das Nagar')
        f()
    elif r=='outh tripura ':
        m.append('South Tripura')
        f()

    #andaman
    elif r=='north and middle andaman ':
        m.append('Andaman Islands')
        f()
    elif r=='nicobars ':
        m.append('Nicobar Islands')
        f()
    elif r=='hojai ':
        m.append('Jorhat')
        f()
    elif r=='outh salmara mancachar ':
        m.append('North Cachar Hills')
        f()

    #arunachal
    elif r== 'hanglang ':
        m.append('Changlang')
        f()
    elif r=='east kameng ':
        m.append('East Kameng')
        f()
    elif r=='lower dibang valley ':
        m.append('Lower Dibang Valley')
        f()
    elif r=='east siang ':
        m.append('East Siang')
        f()
    elif r== 'kurung kumey ':
        m.append('Kurung Kumey')
        f()
    elif r=='lower subansiri ':
        m.append('Lower Subansiri')
        f()
    elif r=='papum pare ':
        m.append('Papum Pare')
        f()
    elif r=='upper subansiri ':
        m.append('Upper Subansiri')
        f()
    elif r== 'awang ':
        m.append('Tawang')
        f()
    elif r=='west kameng ':
        m.append('West Kameng')
        f()
    elif r=='upper siang ':
        m.append('Upper Siang')
        f()
    elif r=='ap ':
        m.append('Tirap')
        f()
    elif r=='west siang ':
        m.append('West Siang')
        f()
    elif r=='bang valley ':
        m.append('Upper Dibang Valley')
        f()
    else:
        r=r.strip()
        m.append(r.capitalize())
        f()


if add_selectbox=='Transaction' and add_selectbox1=='View Data':
   
        option_s = stream.sidebar.selectbox(
        'Select ',
        ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
         'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
         'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
         'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
         'tripura','uttarakhand','uttar_pradesh','west_bengal'))
        option_q = stream.sidebar.selectbox(
        'Select Quarter',
        ("q1","q2","q3","q4"))
        option_y = stream.sidebar.selectbox(
        'Select Year',
        (2018,2019,2020,2021,2022))

        if option_s=='All India':

            mydb=mysql.connect(user="root",password=<password>,
            host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM agg_transaction_details WHERE year="{option_y}" AND quarter="{option_q}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            ptl=[]
            cl=[]
            al=[]
            for i in range(len(db)):
                ptl.append(db[i][3])
                cl.append(db[i][5])
                al.append(db[i][6])

            y2=f'SELECT * FROM top_transaction_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="state"'
            my_cursor.execute(y2)
            db1=my_cursor.fetchall()
            st=[]
            stc=[]
            mstc=[]
            for j in db1:
                st.append(j[4])
                stc.append(j[6])


            def Cr(x):
                if jc>=10000000:
                    k=str(jc)
                    if len(k)<=3:
                        k1=k 
                        x.append(k1+'Cr')
                    elif len(k)==4 or len(k)==5:
                        k1=k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)==6 or len(k)==7:
                        k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)>=8:
                        k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                elif jc<10000000 and jc>=100000:
                    k=str(jc)
                    if len(k)>=6:
                        k1=k[:-5]+','+k[-5:-3]+','+k[-3:]+' Lk'
                        x.append(k1)
                elif jc<100000:
                    k=str(jc)
                    x.append(k1+'k')
            
            for jc in stc:
                Cr(mstc)

            y3=f'SELECT * FROM top_transaction_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="district"'
            my_cursor.execute(y3)
            db2=my_cursor.fetchall()
            dt=[]
            dtc=[]
            mdtc=[]
            for m in db2:
                dt.append(m[4])
                dtc.append(m[6])
            
            for jc in dtc:
                Cr(mdtc)

            y4=f'SELECT * FROM top_transaction_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="pincode"'
            my_cursor.execute(y4)
            db3=my_cursor.fetchall()
            pn=[]
            pnc=[]
            mpnc=[]
            for n in db3:
                pn.append(n[4])
                pnc.append(n[6])
            
            for jc in pnc:
                Cr(mpnc)  

            #formatting transaction count changing int to str
            co=cl
            co1=[]
            for i in co:
                if i>=10000000:
                    k=str(i)
                    if len(k)<=9:
                        k1=k[-9:-7]+","+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        co1.append(k1)
                    elif len(k)>=10:
                        k1=k[:-9]+','+k[-9:-7]+","+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        co1.append(k1)
                elif i<10000000 and i>=100000:
                    k=str(i)
                    k1=k[:-5]+","+k[-5:-3]+','+k[-3:]
                    co1.append(k1)
                elif i<100000: 
                    k=str(i)
                    k1=k[-5:-3]+","+k[-3:]
                    co1.append(k1) 

            
            tc=sum(cl)
            if tc>=10000000:
                k=str(tc)
                if len(k)<=3:
                    k1=k 
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
            elif tc<10000000 and tc>=100000:
                k=str(tc)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                    
            elif tc<100000:
                k=str(tc)
                stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k))

            t=sum(al)
            if t>=10000000:
                k=str(round(t/(10**7)))
                if len(k)<=3:
                    k1=k +' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]+' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]+' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
            elif t<10000000 and t>=100000:
                k=str(round(t/(10**5)))
                if len(k)<=2:
                    k1=k+' Lk'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
            elif t<100000:
                k=str(t)
                stream.write(':blue[Total Payment] '+'₹'+str(k1))

            avg=str(round(sum(al)/sum(cl)))
            stream.write(':blue[Avg. transaction value]'+' '+'₹'+avg[:-3]+','+avg[-3:])
            
            df=pd.DataFrame({'Transaction_type':ptl,'Total count':co1},index=[k for k in range(1,(len(ptl)+1))])
            stream.table(df)
                
            c1,c2=stream.columns([1,3])
            with c1:
                option = stream.radio(
                '**Choose any one**',
                ('State', 'District', 'Pincode'))
            with c2:
                if option=='State':
                    df1=pd.DataFrame({'Top 10 states':st,'Transaction':mstc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df1)
                elif option=='District':
                    df2=pd.DataFrame({'Top 10 districts':dt,'Transaction':mdtc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df2)
                elif option=='Pincode':
                    df3=pd.DataFrame({'Top 10 pincodes':pn,'Transaction':mpnc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df3)
        
        elif  option_s!='All India':
            mydb=mysql.connect(user="root",password=<password>,
            host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM agg_transaction_state_details WHERE year="{option_y}" AND state="{option_s}" AND quarter="{option_q}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            ptl=[]
            cl=[]
            al=[]
            for i in range(len(db)):
                ptl.append(db[i][4])
                cl.append(db[i][6])
                al.append(db[i][7])
           
            def Cr(x):
                if jc>=10000000:
                    k=str(jc)
                    if len(k)<=3:
                        k1=k 
                        x.append(k1+'Cr')
                    elif len(k)==4 or len(k)==5:
                        k1=k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)==6 or len(k)==7:
                        k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)>=8:
                        k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                elif jc<10000000 and jc>=100000:
                    k=str(jc)
                    if len(k)>=6:
                        k1=k[:-5]+','+k[-5:-3]+','+k[-3:]+' Lk'
                        x.append(k1)
                elif jc<100000:
                    k=str(jc)
                    x.append(k+'k')
           



            y3=f'SELECT * FROM top_transaction_state_details WHERE year="{option_y}" AND quarter="{option_q}" AND state="{option_s}" AND top="district"'
            my_cursor.execute(y3)
            db2=my_cursor.fetchall()
            dt=[]
            dtc=[]
            mdtc=[]
            for m in db2:
                dt.append(m[5])
                dtc.append(m[7])
            for jc in dtc:
                Cr(mdtc)

            y4=f'SELECT * FROM top_transaction_state_details WHERE year="{option_y}" AND quarter="{option_q}" AND state="{option_s}" AND top="pincode"'
            my_cursor.execute(y4)
            db3=my_cursor.fetchall()
            pn=[]
            pnc=[]
            mpnc=[]
            for n in db3:
                pn.append(n[5])
                pnc.append(n[7])
            for jc in pnc:
                Cr(mpnc)  

            co=cl
            co1=[]
            for i in co:
                if i>=10000000:
                    k=str(i)
                    if len(k)<=9:
                        k1=k[-9:-7]+","+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        co1.append(k1)
                    elif len(k)>=10:
                        k1=k[:-9]+','+k[-9:-7]+","+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        co1.append(k1)
                elif i<10000000 and i>=100000:
                    k=str(i)
                    k1=k[:-5]+","+k[-5:-3]+','+k[-3:]
                    co1.append(k1)
                elif i<100000 and i>=1000: 
                    k=str(i)
                    k1=k[-5:-3]+","+k[-3:]
                    co1.append(k1) 
                elif i<1000:
                    k=str(i)
                    k1=k[-3:]
                    co1.append(k1)

            
            tc=sum(cl)
            if tc>=10000000:
                k=str(tc)
                if len(k)<=3:
                    k1=k 
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==6:
                    k1=k[-6:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
            elif tc<10000000 and tc>=100000:
                k=str(tc)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k1))
            elif tc<100000:
                k=str(tc)
                stream.write(':blue[All PhonePe transactions (UPI + Cards + Wallets)] '+str(k))

            t=sum(al)
            if t>=10000000:
                k=str(round(t/(10**7)))
                if len(k)<=3:
                    k1=k +' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]+' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]+' Cr'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
            elif t<10000000 and t>=100000:
                k=str(round(t/(10**5)))
                if len(k)<=2:
                    k1=k+' Lk'
                    stream.write(':blue[Total Payment] '+'₹'+str(k1))
            elif t<100000:
                k=str(t)
                stream.write(':blue[Total Payment] '+'₹'+str(k1)+'k')

            avg=str(round(sum(al)/sum(cl)))
            stream.write(':blue[Avg. transaction value]'+' '+'₹'+avg[:-3]+','+avg[-3:])
            
            df=pd.DataFrame({'Transaction_type':ptl,'Total count':co1},index=[k for k in range(1,(len(ptl)+1))])
            stream.table(df)
                
            c1,c2=stream.columns([1,3])
            with c1:
                option = stream.radio(
                '**Choose any one**',
                ('District', 'Pincode'))
            with c2:
                if option=='District':
                    df2=pd.DataFrame({'Top districts':dt,'Transaction':mdtc},index=[k for k in range(1,(len(dt)+1))])
                    stream.table(df2)
                elif option=='Pincode':
                    df3=pd.DataFrame({'Top pincodes':pn,'Transaction':mpnc},index=[k for k in range(1,(len(pn)+1))])
                    stream.table(df3)


elif add_selectbox=='Transaction' and add_selectbox1=='View Statistic Plots':
    #rad2=stream.radio('Select Any One',options=['Transactions','Users'])
    #if rad2=='Transactions':
    option_s = stream.sidebar.selectbox(
    'Select ',
    ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
        'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
        'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
        'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
        'tripura','uttarakhand','uttar_pradesh','west_bengal'))
        
        
    if option_s=='All India': 
        mydb=mysql.connect(user="root",password=<password>,
        host="localhost",database='phonepe')
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_transaction_details '
        my_cursor.execute(y1)
        db=my_cursor.fetchall()

        yl=[]
        ql=[]
        tl=[]
        cl=[]
        al=[]
        for i in range(len(db)):
                yl.append(db[i][1])
                ql.append(db[i][2])
                tl.append(db[i][3])
                cl.append(db[i][5])
                al.append(db[i][6])
        
        stream.subheader('1.Statistics of every type of transactions at each quarter between 2018-22')
        df=pd.DataFrame({'year':yl,'quarter':ql,'transaction_name':tl,'Transactions':cl,'Amount':al})
        fig = px.histogram(df, x="quarter", y="Transactions",
            color='transaction_name', barmode='group',facet_col="year",
            height=400)
        stream.plotly_chart(fig, theme=None, use_container_width=True)
        
        stream.subheader('2.Contribution of each transactions between 2018-22')
        fig1 = px.pie(df, values='Transactions', names='transaction_name')
        stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        stream.subheader('3.Transactions count Vs Transactions amount between    2018-22 ')
        fig2 = px.scatter(df, x="Transactions", y="Amount",  color="transaction_name",hover_data=['quarter',"year"],
                            facet_col='year')
        stream.plotly_chart(fig2, theme=None, use_container_width=True)
        
        def top():
            my_cursor=mydb.cursor()
            y2=f'SELECT * FROM top_transaction_details WHERE top="{t}"'
            my_cursor.execute(y2)
            db2=my_cursor.fetchall()
            
            
            yl1=[]
            ql1=[]
            dl1=[]
            cl1=[]
            sl1=[]
            for j in range(len(db2)):
                yl1.append(db2[j][1])
                ql1.append(db2[j][2])
                dl1.append(db2[j][4])
                cl1.append(db2[j][6])
                
            
            df2=pd.DataFrame({'year':yl1,f'{option_s}':ql1,f'{t}':dl1,'Transactions':cl1})
            stream.subheader(f'4.Contribution of top {t}s between 2018-22')
            fig1 = px.pie(df2, values='Transactions', names=f'{t}',facet_col='year')
            stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        t=stream.radio('**CHOOSE ANY ONE**',options=['state','district','pincode'])
        top()
    
    else:
        mydb=mysql.connect(user="root",password=<password>,
        host="localhost",database='phonepe')
        
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_transaction_state_details WHERE state="{option_s}"'
        my_cursor.execute(y1)
        db=my_cursor.fetchall()

        yl=[]
        ql=[]
        tl=[]
        cl=[]
        al=[]
        for i in range(len(db)):
                yl.append(db[i][1])
                ql.append(db[i][3])
                tl.append(db[i][4])
                cl.append(db[i][6])
                al.append(db[i][7])
            
        
        df=pd.DataFrame({'year':yl,f'{option_s}':ql,'transaction_name':tl,'Transactions':cl,'Amount':al})
        stream.subheader('1.Statistics of every type of transactions at each quarter between 2018-22')
        fig = px.histogram(df, x=f'{option_s}', y="Transactions",
            color='transaction_name', barmode='group',facet_col="year",
            height=400)
        stream.plotly_chart(fig, theme=None, use_container_width=True)
        
        stream.subheader('2.Contribution of each transactions between 2018-22')
        fig1 = px.pie(df, values='Transactions', names='transaction_name')
        stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        stream.subheader('3.Transactions count Vs Transactions amount between    2018-22 ')
        fig2 = px.scatter(df, x="Transactions", y="Amount",  color="transaction_name",hover_data=[f'{option_s}'
                                                                                ,"year"], facet_col='year')
        stream.plotly_chart(fig2, theme=None, use_container_width=True)
        
        
        def top():
            my_cursor=mydb.cursor()
            y2=f'SELECT * FROM top_transaction_state_details WHERE state="{option_s}" AND top="{t}"'
            my_cursor.execute(y2)
            db2=my_cursor.fetchall()
            
            yl1=[]
            ql1=[]
            dl1=[]
            cl1=[]
            sl1=[]
            for j in range(len(db2)):
                yl1.append(db2[j][1])
                ql1.append(db2[j][2])
                dl1.append(db2[j][5])
                cl1.append(db2[j][7])
                sl1.append(db2[j][3])
            
            df2=pd.DataFrame({'year':yl1,f'{option_s}':ql1,f'{t}':dl1,'Transactions':cl1,'state':sl1})
            stream.subheader(f'4.Contribution of top {t}s between 2018-22')
            fig1 = px.pie(df2, values='Transactions', names=f'{t}',facet_col='year')
            stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        t=stream.radio('**CHOOSE ANY ONE**',options=['district','pincode'])
        top()

elif add_selectbox=='Transaction' and add_selectbox1=='View Map':  
    option_s = stream.sidebar.selectbox(
        'Select ',
        ('All India','-'))
    option_q = stream.sidebar.selectbox(
        'Select Quarter',
        ("q1","q2","q3","q4"))
    option_y = stream.sidebar.selectbox(
        'Select Year',
        (2018,2019,2020,2021,2022)) 
    option_choice=stream.sidebar.selectbox(
        'Select Any ',
        ('Statewise','Districtwise')) 
    
    f = open('india_district_geojson.json')
    data = json.load(f)

    mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
    my_cursor=mydb.cursor()
    
    if option_choice=='Districtwise':
        option_s = stream.sidebar.selectbox(
        'Select ',
        ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
         'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
         'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
         'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
         'tripura','uttarakhand','uttar_pradesh','west_bengal'))
        
        def transaction_dist():
            y1=f'SELECT * FROM map_transaction_hover_state_details WHERE year="{option_y}"AND quarter="{option_q}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            y=[]
            cl=[]
            al=[]
            avgl=[]
            for t in range(len(db)):
                
                c=(db[t][6])
                a=(db[t][7])
                avg=(db[t][8])
                def name_1():
                    cl.append(c)
                    al.append(a)
                    avgl.append(avg)
                qwer(db,t,4,y,name_1)
            
            df1=pd.DataFrame({'district':y,'All Transactions':cl,'Total payment value INR':al,
                            'Avg. transaction value INR':avgl})
            fig = px.choropleth_mapbox(df1, geojson=data, locations='district',
                                    color='Total payment value INR',
                                    featureidkey="properties.NAME_2",
                                    color_continuous_scale="Reds",
                                    hover_data=['All Transactions','Avg. transaction value INR'],
                                    mapbox_style="carto-positron",
                                    zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                    opacity=0.5,
                                    )
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
            stream.plotly_chart(fig, use_container_width=True)
    
        def transaction_dist_single():
            y1=f'SELECT * FROM map_transaction_hover_state_details WHERE year="{option_y}" AND quarter="{option_q}" AND state="{option_s}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            y=[]
            cl=[]
            al=[]
            avgl=[]
            for t in range(len(db)):
                
                c=(db[t][6])
                a=(db[t][7])
                avg=(db[t][8])
                def name_1():
                    cl.append(c)
                    al.append(a)
                    avgl.append(avg)
                qwer(db,t,4,y,name_1)
            df1=pd.DataFrame({'district':y,'All Transactions':cl,'Total payment value INR':al,
                            'Avg. transaction value INR':avgl})  
            

            fig = px.choropleth_mapbox(df1, geojson=data, locations='district',
                                    color='Total payment value INR',
                                    featureidkey="properties.NAME_2",
                                    color_continuous_scale="Reds",
                                    hover_data=['All Transactions','Avg. transaction value INR'],
                                    mapbox_style="carto-positron",
                                    zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                    opacity=0.5,
                                    
                                    )
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
            stream.plotly_chart(fig, use_container_width=True)
        
        if option_s=='All India':
            transaction_dist()
        elif option_s!='All India':
             transaction_dist_single()
           

    elif option_choice=='Statewise' and option_s=='All India':
        y1=f'SELECT * FROM map_transaction_hover_details WHERE year="{option_y}"AND quarter="{option_q}"'
        my_cursor.execute(y1)
        db=my_cursor.fetchall()
        
        st=[]
        cl=[]
        al=[]
        avgl=[]
        for t in range(len(db)):
            c=(db[t][5])
            cl.append(c)
            a=(db[t][6])
            al.append(a)
            avg=(db[t][7])
            avgl.append(avg)
            y=(db[t][3])
            if y=='andaman & nicobar islands':
                st.append('Andaman and Nicobar')
            elif y=='andhra pradesh':
                st.append('Andhra Pradesh')
            elif y=='arunachal pradesh':
                st.append('Arunachal Pradesh')
            elif y=='assam':
                st.append('Assam')
            elif y=='bihar':
                st.append('Bihar')
            elif y=='chandigarh':
                st.append('Chandigarh')
            elif y=='chhattisgarh':
                st.append('Chhattisgarh')
            elif y=='dadra & nagar haveli & daman & diu':
                st.append('Dadra and Nagar Haveli')
            elif y=='delhi':
                st.append('Delhi')
            elif y=='goa':
                st.append('Goa')
            elif y=='gujarat':
                st.append('Gujarat')
            elif y=='haryana':
                st.append('Haryana')
            elif y=='himachal pradesh':
                st.append('Himachal Pradesh')
            elif y=='jammu & kashmir':
                st.append('Jammu and Kashmir')
            elif y=='jharkhand':
                st.append('Jharkhand')
            elif y=='karnataka':
                st.append('Karnataka')
            elif y=='kerala':
                st.append('Kerala')
            elif y=='lakshadweep':
                st.append('Lakshadweep')
            elif y=='madhya pradesh':
                st.append('Madhya Pradesh')
            elif y=='maharashtra':   
                st.append('Maharashtra')
            elif y=='manipur':
                st.append('Manipur')
            elif y=='meghalaya':
                st.append('Meghalaya')
            elif y=='mizoram':
                st.append('Mizoram')
            elif y=='nagaland':
                st.append('Nagaland')
            elif y=='odisha':
                st.append('Orissa')
            elif y=='puducherry':
                st.append('Puducherry')
            elif y=='punjab':
                st.append('Punjab')
            elif y=='rajasthan':
                st.append('Rajasthan')
            elif y=='sikkim':
                st.append('Sikkim')
            elif y=='tamil nadu':
                st.append('Tamil Nadu')
            elif y=='tripura':
                st.append('Tripura')
            elif y=='uttar pradesh':
                st.append('Uttar Pradesh')
            elif y=='uttarakhand':
                st.append('Uttaranchal')
            elif y=='west bengal':
                st.append('West Bengal'  )
            else:
                st.append(y)
        f = open('india_states.geojson')
        data = json.load(f)
        df5=pd.DataFrame({'state':st,'Transaction':cl,'Total Payment INR':al,'Average Transaction INR':avgl})
        fig5 = px.choropleth_mapbox(df5, geojson=data, 
                                    locations='state',
                                    color='Transaction',
                                    featureidkey="properties.NAME_1",
                                    color_continuous_scale="Viridis",
                                    hover_data=['state','Total Payment INR','Average Transaction INR'],
                                    mapbox_style="carto-positron",
                                    zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                    opacity=0.5)

        fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
        stream.plotly_chart(fig5, use_container_width=True)

    elif option_choice=='Statewise' and option_s!='All India':
        stream.warning('Irrelevant Selection ! Choose All India')
        
elif add_selectbox=='User' and add_selectbox1=='View Data':
    option_s = stream.sidebar.selectbox(
        'Select ',
        ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
         'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
         'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
         'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
         'tripura','uttarakhand','uttar_pradesh','west_bengal'))
    option_q = stream.sidebar.selectbox(
        'Select Quarter',
        ("q1","q2","q3","q4"))
    option_y = stream.sidebar.selectbox(
        'Select Year',
        (2018,2019,2020,2021,2022))

    if option_s=='All India':

            mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM agg_user_registered_users_details WHERE year="{option_y}" AND quarter="{option_q}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            
            rl=[]
            apl=[]
            for i in range(len(db)):
                rl.append(db[i][3])
                apl.append(db[i][4])
            
            y2=f'SELECT * FROM top_user_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="state"'
            my_cursor.execute(y2)
            db1=my_cursor.fetchall()
            
            st=[]
            stc=[]
            mstc=[]
            for j in db1:
                st.append(j[4])
                stc.append(j[5])
            
            def Cr(x):
                if jc>=10000000:
                    k=str(jc)
                    if len(k)<=3:
                        k1=k 
                        x.append(k1+'Cr')
                    elif len(k)==4 or len(k)==5:
                        k1=k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)==6 or len(k)==7:
                        k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)>=8:
                        k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                elif jc<10000000 and jc>=100000:
                    k=str(jc)
                    if len(k)>=6:
                        k1=k[:-5]+','+k[-5:-3]+','+k[-3:]+' Lk'
                        x.append(k1)
                elif jc<100000:
                    k=str(jc)
                    x.append(k+'k')
            
            for jc in stc:
                Cr(mstc)

            y3=f'SELECT * FROM top_user_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="district"'
            my_cursor.execute(y3)
            db2=my_cursor.fetchall()
            
            dt=[]
            dtc=[]
            mdtc=[]
            for m in db2:
                dt.append(m[4])
                dtc.append(m[5])
            for jc in dtc:
                Cr(mdtc)

            y4=f'SELECT * FROM top_user_details WHERE year="{option_y}" AND quarter="{option_q}" AND top="pincode"'
            my_cursor.execute(y4)
            db3=my_cursor.fetchall()
            pn=[]
            pnc=[]
            mpnc=[]
            for n in db3:
                pn.append(n[4])
                pnc.append(n[5])
            for jc in pnc:
                Cr(mpnc)  

            tc=sum(rl)
            if tc>=10000000:
                k=str(tc)
                if len(k)<=3:
                    k1=k 
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
            elif tc<10000000 and tc>=100000:
                k=str(tc)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y}"] '+' '+str(k1))
            elif tc<100000:
                k=str(tc)
                stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y}"] '+' '+str(k))

            t1=sum(apl)
            if t1==0:
                stream.write(f':blue[PhonePe app opens in "UNAVAILABLE"]')
                
            elif t1>=10000000:
                k=str(t1)
                if len(k)<=3:
                    k1=k 
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
            elif t1<10000000 and t1>=100000:
                k=str(t1)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
            elif t1<100000:
                k=str(tc)
                stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))


            c1,c2=stream.columns([1,3])
            with c1:
                option = stream.radio(
                '**Choose any one**',
                ('State', 'District', 'Pincode'))
            with c2:
                if option=='State':
                    df1=pd.DataFrame({'Top 10 states':st,'Registered Users':mstc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df1)
                elif option=='District':
                    df2=pd.DataFrame({'Top 10 districts':dt,'Registered Users':mdtc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df2)
                elif option=='Pincode':
                    df3=pd.DataFrame({'Top 10 pincodes':pn,'Registered Users':mpnc},index=[1,2,3,4,5,6,7,8,9,10])
                    stream.table(df3)
        
    elif  option_s!='All India':
            mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM agg_user_registered_users_state_details WHERE year="{option_y}"  AND state="{option_s}" AND quarter="{option_q}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()

            
            rl=[]
            apl=[]
            for i in range(len(db)):
                rl.append(db[i][4])
                apl.append(db[i][5])
                
            def Cr(x):
                if jc>=10000000:
                    k=str(jc)
                    if len(k)<=3:
                        k1=k 
                        x.append(k1+'Cr')
                    elif len(k)==4 or len(k)==5:
                        k1=k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)==6 or len(k)==7:
                        k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                    elif len(k)>=8:
                        k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                        x.append(k1+'Cr')
                elif jc<10000000 and jc>=100000:
                    k=str(jc)
                    if len(k)>=6:
                        k1=k[:-5]+','+k[-5:-3]+','+k[-3:]+' Lk'
                        x.append(k1)
                elif jc<100000:
                    k=str(jc)
                    x.append(k+'k')
           
            
            y3=f'SELECT * FROM top_user_state_details WHERE year="{option_y}"  AND quarter="{option_q}" AND state="{option_s}" AND top="district"'
            my_cursor.execute(y3)
            db2=my_cursor.fetchall()
            
            dt=[]
            dtc=[]
            mdtc=[]
            for m in db2:
                dt.append(m[5])
                dtc.append(m[6])
            for jc in dtc:
                Cr(mdtc)

            y4=f'SELECT * FROM top_user_state_details WHERE year="{option_y}"  AND quarter="{option_q}" AND state="{option_s}" AND top="pincode"'
            my_cursor.execute(y4)
            db3=my_cursor.fetchall()
            
            pn=[]
            pnc=[]
            mpnc=[]
            for n in db3:
                pn.append(n[5])
                pnc.append(n[6])
            
            for jc in pnc:
                Cr(mpnc)  
            
            tc=sum(rl)
            if tc>=10000000:
                k=str(tc)
                if len(k)<=3:
                    k1=k 
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y} "]'+' '+str(k1))
            elif tc<10000000 and tc>=100000:
                k=str(tc)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y}"] '+' '+str(k1))
            elif tc<100000:
                k=str(tc)
                stream.write(f':blue[Registered PhonePe users till "{option_q}" "{option_y}"] '+' '+str(k))

            t1=sum(apl)
            
            if t1==0:
                stream.write(f':blue[PhonePe app opens in "UNAVAILABLE"]')
            elif t1>=10000000:
                k=str(t1)
                if len(k)<=3:
                    k1=k 
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==4 or len(k)==5:
                    k1=k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==6 or len(k)==7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)==8 or len(k)==9:
                    k1=k[:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
                elif len(k)>=10 :
                    k1=k[:-9]+','+k[-9:-7]+','+k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
            elif t1<10000000 and t1>=100000:
                k=str(t1)
                if len(k)<=7:
                    k1=k[-7:-5]+','+k[-5:-3]+','+k[-3:]
                    stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))
            elif t1<100000:
                k=str(t1)
                stream.write(f':blue[PhonePe app opens in "{option_q}" "{option_y}" ] '+' '+str(k1))

            c1,c2=stream.columns([1,3])
            with c1:
                option = stream.radio(
                '**Choose any one**',
                ('District', 'Pincode'))
            with c2:
                
                if option=='District':
                    df2=pd.DataFrame({'Top 10 districts':dt,'Registered Users':mdtc},index=[i for i in range(1,len(dt)+1)])
                    stream.table(df2)
                elif option=='Pincode':
                    df3=pd.DataFrame({'Top 10 pincodes':pn,'Registered Users':mpnc},index=[i for i in range(1,len(pn)+1)])
                    stream.table(df3)

elif add_selectbox=='User' and add_selectbox1=='View Statistic Plots':
    option_s = stream.sidebar.selectbox(
    'Select ',
    ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
        'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
        'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
        'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
        'tripura','uttarakhand','uttar_pradesh','west_bengal'))
        
     
      
    if option_s=='All India': 
        mydb=mysql.connect(user="root",password=<password>,
        host="localhost",database='phonepe')
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_user_details '
        my_cursor.execute(y1)
        db=my_cursor.fetchall()

        yl=[]
        ql=[]
        bl=[]
        cl=[]
        for i in range(len(db)):
                yl.append(db[i][1])
                ql.append(db[i][2])
                bl.append(db[i][3])
                cl.append(db[i][4])
                
        
        df=pd.DataFrame({'year':yl,'quarter':ql,'brand':bl,'count':cl})
        stream.subheader('1.Brand preferred by registered users between 2018-22')
        fig = px.histogram(df, x="quarter", y="count",
            color='brand', barmode='group',facet_col="year",
            height=400)
        stream.plotly_chart(fig, theme=None, use_container_width=True)
        
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_user_registered_users_details '
        my_cursor.execute(y1)
        db1=my_cursor.fetchall()
        yl1=[]
        ql1=[]
        rl1=[]
        ol1=[]
        for i in range(len(db1)):
                yl1.append(db1[i][1])
                ql1.append(db1[i][2])
                rl1.append(db1[i][3])
                ol1.append(db1[i][4])
        df1=pd.DataFrame({'year':yl1,'quarter':ql1,'Registered Users':rl1,'App opens':ol1})
        stream.subheader('2.Registered Users Vs App opens between 2018-22 ')
        fig2 = px.scatter(df1, x='Registered Users', y='App opens',  color='quarter',
                            facet_col='year')
        stream.plotly_chart(fig2, theme=None, use_container_width=True)
        
        def top():
            my_cursor=mydb.cursor()
            y2=f'SELECT * FROM top_user_details WHERE top="{t}"'
            my_cursor.execute(y2)
            db2=my_cursor.fetchall()
            
            
            yl1=[]
            ql1=[]
            dl1=[]
            cl1=[]
            sl1=[]
            for j in range(len(db2)):
                yl1.append(db2[j][1])
                ql1.append(db2[j][2])
                dl1.append(db2[j][4])
                cl1.append(db2[j][5])
                
            
            df2=pd.DataFrame({'year':yl1,f'{option_s}':ql1,f'{t}':dl1,'Registered Users':cl1})
            stream.subheader(f'3.Registered Users of top {t}s between 2018-22')
            fig1 = px.pie(df2, values='Registered Users', names=f'{t}',facet_col='year')
            stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        t=stream.radio('**CHOOSE ANY ONE**',options=['state','district','pincode'])
        top()
    
    else:
        mydb=mysql.connect(user="root",password=<password>,
        host="localhost",database='phonepe')
        
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_user_state_details WHERE state="{option_s}"'
        my_cursor.execute(y1)
        db4=my_cursor.fetchall()

        yl4=[]
        ql4=[]
        bl4=[]
        rl4=[]
        
        for i in range(len(db4)):
                yl4.append(db4[i][1])
                ql4.append(db4[i][3])
                bl4.append(db4[i][4])
                rl4.append(db4[i][5])
              
            
        stream.subheader(f'Brand preferred by registered users at {option_s} between 2018-22')
        df4=pd.DataFrame({'year':yl4,f'{option_s}':ql4,'brand':bl4,'Registered Users':rl4})
        
        fig = px.histogram(df4, x=f'{option_s}', y="Registered Users",
            color='brand', barmode='group',facet_col="year",
            height=400)
        stream.plotly_chart(fig, theme=None, use_container_width=True)
        
        my_cursor=mydb.cursor()
        y1=f'SELECT * FROM agg_user_registered_users_state_details WHERE state="{option_s}"'
        my_cursor.execute(y1)
        db1=my_cursor.fetchall()
        yl1=[]
        ql1=[]
        rl1=[]
        ol1=[]
        for i in range(len(db1)):
                yl1.append(db1[i][1])
                ql1.append(db1[i][3])
                rl1.append(db1[i][4])
                ol1.append(db1[i][5])
        df1=pd.DataFrame({'year':yl1,'quarter':ql1,'Registered Users':rl1,'App opens':ol1})
        stream.subheader('2.Registered Users Vs App opens between 2018-22 ')
        fig2 = px.scatter(df1, x='Registered Users', y='App opens',  color='quarter',
                            facet_col='year')
        stream.plotly_chart(fig2, theme=None, use_container_width=True)
        
        def top():
            my_cursor=mydb.cursor()
            y2=f'SELECT * FROM top_user_state_details WHERE state="{option_s}" AND top="{t}"'
            my_cursor.execute(y2)
            db2=my_cursor.fetchall()
            
            
            yl1=[]
            ql1=[]
            dl1=[]
            cl1=[]
            sl1=[]
            for j in range(len(db2)):
                yl1.append(db2[j][1])
                ql1.append(db2[j][2])
                dl1.append(db2[j][5])
                cl1.append(db2[j][6])
                
            
            df2=pd.DataFrame({'year':yl1,f'{option_s}':ql1,f'{t}':dl1,'Registered Users':cl1})
            stream.subheader(f'3.Registered Users of top {t}s in {option_s} between 2018-22')
            fig1 = px.pie(df2, values='Registered Users', names=f'{t}',facet_col='year')
            stream.plotly_chart(fig1, theme=None, use_container_width=True)
        
        t=stream.radio('**CHOOSE ANY ONE**',options=['district','pincode'])
        top()
        
elif add_selectbox=='User' and add_selectbox1=='View Map':  
    option_s = stream.sidebar.selectbox(
        'Select ',
        ('All India','andaman','andhra_pradesh','arunachal_pradesh','assam','bihar','chandigarh','chhattisgarh',
         'dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana','himachal_pradesh','jammu_kashmir',
         'jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya_pradesh','maharashtra','manipur',
         'meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil_nadu','telangana',
         'tripura','uttarakhand','uttar_pradesh','west_bengal'))
    option_y = stream.sidebar.selectbox(
        'Select Year',
        (2018,2019,2020,2021,2022)) 
    option_q = stream.sidebar.selectbox(
        'Select Quarter',
        ('q1','q2','q3','q4')) 
    option_choice=stream.sidebar.selectbox(
        'Select Any ',
        ('Statewise','Districtwise'))
    
    f = open('india_district_geojson.json')
    data = json.load(f)
    
    def reg_plot(x1,x2):
            mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM map_user_hover_state_details WHERE year="{option_y}"AND state="{option_s}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()
            y_1=[]
            reg=[]
            aop=[]
            for t in range(len(db)):
                a=(db[t][x1])
                avg=(db[t][x2])
                def name_2():
                    reg.append(a)
                    aop.append(avg)
                qwer(db,t,3,y_1,name_2)
            
            df1=pd.DataFrame({'district':y_1,'Registered Users':reg,f'App Opens in {option_y} {option_q}':aop,
                            })  
            

            fig = px.choropleth_mapbox(df1, geojson=data, locations='district',
                                    color='Registered Users',
                                    featureidkey="properties.NAME_2",
                                    color_continuous_scale="Reds",
                                    hover_data=['Registered Users',f'App Opens in {option_y} {option_q}'],
                                    mapbox_style="carto-positron",
                                    zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                    opacity=0.5,
                                    
                                    )
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
            stream.plotly_chart(fig, use_container_width=True)
    
    def user_dist_single():
        if option_q=='q1':    
            reg_plot(4,5)
        elif option_q=='q2':    
            reg_plot(6,7)
        elif option_q=='q3':    
            reg_plot(8,9)
        elif option_q=='q4':    
            reg_plot(10,11)
            
    def reg_plot_1(x1,x2):
            mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM map_user_hover_state_details WHERE year="{option_y}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()
            
            y_1=[]
            reg=[]
            aop=[]
            for t in range(len(db)):
                a=(db[t][x1])
                avg=(db[t][x2])
                def name_2():
                    reg.append(a)
                    aop.append(avg)
                qwer(db,t,3,y_1,name_2)
            
            df1=pd.DataFrame({'district':y_1,'Registered Users':reg,f'App Opens in {option_y} {option_q}':aop,
                            })  
            

            fig = px.choropleth_mapbox(df1, geojson=data, locations='district',
                                    color='Registered Users',
                                    featureidkey="properties.NAME_2",
                                    color_continuous_scale="Reds",
                                    hover_data=['Registered Users',f'App Opens in {option_y} {option_q}'],
                                    mapbox_style="carto-positron",
                                    zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                    opacity=0.5,
                                    
                                    )
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
            stream.plotly_chart(fig, use_container_width=True)
    
    def user_dist_all():
        if option_q=='q1':    
            reg_plot_1(4,5)
        elif option_q=='q2':    
            reg_plot_1(6,7)
        elif option_q=='q3':    
            reg_plot_1(8,9)
        elif option_q=='q4':    
            reg_plot_1(10,11)
    
    def reg_plot_state(x1,x2):
            
            f = open('india_states.geojson')
            data = json.load(f)
            mydb=mysql.connect(user="root",password=<password>,host="localhost",database='phonepe')
            my_cursor=mydb.cursor()
            y1=f'SELECT * FROM map_user_hover_details WHERE year="{option_y}"'
            my_cursor.execute(y1)
            db=my_cursor.fetchall()
            st=[]
            reg=[]
            aop=[]
            for t in range(len(db)):
                a=(db[t][x1])
                reg.append(a)
                avg=(db[t][x2])
                aop.append(avg)
                y=(db[t][2])
                if y=='andaman & nicobar islands':
                    st.append('Andaman and Nicobar')
                elif y=='andhra pradesh':
                    st.append('Andhra Pradesh')
                elif y=='arunachal pradesh':
                    st.append('Arunachal Pradesh')
                elif y=='assam':
                    st.append('Assam')
                elif y=='bihar':
                    st.append('Bihar')
                elif y=='chandigarh':
                    st.append('Chandigarh')
                elif y=='chhattisgarh':
                    st.append('Chhattisgarh')
                elif y=='dadra & nagar haveli & daman & diu':
                    st.append('Dadra and Nagar Haveli')
                elif y=='delhi':
                    st.append('Delhi')
                elif y=='goa':
                    st.append('Goa')
                elif y=='gujarat':
                    st.append('Gujarat')
                elif y=='haryana':
                    st.append('Haryana')
                elif y=='himachal pradesh':
                    st.append('Himachal Pradesh')
                elif y=='jammu & kashmir':
                    st.append('Jammu and Kashmir')
                elif y=='jharkhand':
                    st.append('Jharkhand')
                elif y=='karnataka':
                    st.append('Karnataka')
                elif y=='kerala':
                    st.append('Kerala')
                elif y=='lakshadweep':
                    st.append('Lakshadweep')
                elif y=='madhya pradesh':
                    st.append('Madhya Pradesh')
                elif y=='maharashtra':   
                    st.append('Maharashtra')
                elif y=='manipur':
                    st.append('Manipur')
                elif y=='meghalaya':
                    st.append('Meghalaya')
                elif y=='mizoram':
                    st.append('Mizoram')
                elif y=='nagaland':
                    st.append('Nagaland')
                elif y=='odisha':
                    st.append('Orissa')
                elif y=='puducherry':
                    st.append('Puducherry')
                elif y=='punjab':
                    st.append('Punjab')
                elif y=='rajasthan':
                    st.append('Rajasthan')
                elif y=='sikkim':
                    st.append('Sikkim')
                elif y=='tamil nadu':
                    st.append('Tamil Nadu')
                elif y=='tripura':
                    st.append('Tripura')
                elif y=='uttar pradesh':
                    st.append('Uttar Pradesh')
                elif y=='uttarakhand':
                    st.append('Uttaranchal')
                elif y=='west bengal':
                    st.append('West Bengal'  )
                else:
                    st.append(y)
            
            df5=pd.DataFrame({'state':st,'Registered Users':reg,f'App Opens in {option_y} {option_q}':aop,
                            })  
            

            
            fig5 = px.choropleth_mapbox(df5, geojson=data, 
                                        locations='state',
                                        color='Registered Users',
                                        featureidkey="properties.NAME_1",
                                        color_continuous_scale="Viridis",
                                        hover_data=['state','Registered Users',f'App Opens in {option_y} {option_q}'],
                                        mapbox_style="carto-positron",
                                        zoom=3, center = {"lat": 20.5937, "lon":78.9629},
                                        opacity=0.5)

            fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
            stream.plotly_chart(fig5, use_container_width=True)
    
    def user_state():
        if option_q=='q1':    
            reg_plot_state(3,4)
        elif option_q=='q2':    
            reg_plot_state(5,6)
        elif option_q=='q3':    
            reg_plot_state(7,8)
        elif option_q=='q4':    
            reg_plot_state(9,10)  
    if option_s!='All India' and option_choice=='Districtwise':
        user_dist_single()
    elif option_s=='All India' and option_choice=='Districtwise':
        user_dist_all()   
    elif option_choice=='Statewise' and option_s=='All India':
        user_state()
    elif option_choice=='Statewise' and option_s!='All India':
        stream.warning(f'Irrelevant Selection ! Select "All India" and Select "Districtwise" to get geo-visualization of {option_s}' )
         
            
                


        
                
                
            
            
       
