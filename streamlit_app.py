import streamlit as st
import pandas as pd


st.title('Bulk Loading Log')
carNum = st.text_input('Car Number: ')
compNum = st.text_input('Comp Number: ')
blendNum = st.text_input('Blend Number: ')
siloNum = st.text_input('Silo Number: ')
dateStart = st.text_input('Date/Time Started: ')
dateEnd = st.text_input('Date/Time End: ')
opName = st.text_input('Operator Name: ')
comments = st.text_input('Comments: ')

if (st.button('Save')):
    with open('Z:\\Public\\BulkLoadingLog\\Bulk_Loading_Log.csv', 'a', newline='') as fd:
        fd.writelines(carNum + ',' + compNum + ',' + blendNum + ',' + siloNum + ','
                    + dateStart + ',' + dateEnd + ',' + opName + ',' + comments + '\n')
