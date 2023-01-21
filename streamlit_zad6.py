import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import datetime
import time


with st.sidebar:
     selected = option_menu(
         menu_title='Menu strony', # wymagane
         options = ['Ankieta', 'Staty'], # wymagane
         icons= ['airplane-engines-fill', 'buildings-fill'],
         menu_icon = 'cast',
         default_index=0 # na której stronie będziemy na starcie
     )
 
     if selected == 'Ankieta':
         st.title(f'Otwarta zakładka {selected}')
         default_index=1
     if selected == 'Staty':
         st.title(f'Otwarta zakładka {selected}')
         default_index=2


if default_index == 1:
    st.title("Ankieta")

    imie = st.text_input("Proszę podać imię", "Miejsce na tekst...")
    nazwisko = st.text_input("Proszę podać nazwisko", "Miejsce na tekst...")
    if st.button("Zapisz"):
        a = imie+" "+nazwisko
        result = 'Zapisano dane: ' + a
        st.success(result)

if default_index == 2:

    st.title("Staty")

    data = st.file_uploader("Wczytaj plik CSV", type=['csv'])
    if data is not None:
        with st.spinner("Waiting..."):
            time.sleep(1)
            st.success("Finished!")
        df = pd.read_csv(data)
        st.dataframe(df.head(5))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        plot_data = df[selected_column_names]

        st.area_chart(plot_data)
        st.line_chart(plot_data)



