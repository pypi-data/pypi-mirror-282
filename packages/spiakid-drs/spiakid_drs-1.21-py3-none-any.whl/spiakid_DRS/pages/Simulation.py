import streamlit as st
import numpy as np
import pages.Sim_func.Recons_inter as RI
import pages.Sim_func.Sim_creation as SC
import pages.Sim_func.Wavelength_calib as wv

st.set_page_config(page_title='Observation Simulation',layout = 'wide')

tab1, tab2,tab3 = st.tabs(['Simulation Interface','Reconstruction', 'Wavelength Calibration'])


with tab1:
    SC.Sim()
with tab2:
    RI.Recons()
with tab3:
    wv.wv_calib()
