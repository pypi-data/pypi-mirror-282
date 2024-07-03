import streamlit as st
import SpectralRes.Data as Dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from scipy import signal
from scipy.interpolate import CubicSpline

def wv_calib():

    st.title('Wavelength Calibration')


    data_location = st.text_input(label = 'Data Location',placeholder = 'Absolute path')
    if st.button('Plot'):
    # if data_location != None:
        data = Dt.read_hdf5(data_location)
        num = int(np.sqrt(len(data['Photons'])))
        fig1 = plt.figure()
        plt.title('Histograms of Calibration phase pix per pix')
        f,a = plt.subplots(num,num)

        axes = a.flatten()
        
        try: 
            if data['Calib']: pass
        except: st.write('No calibration File')
        else:
            calib_photon = np.zeros(shape=(num,num),dtype = object)
            interp = np.zeros(shape=(num,num),dtype = object)
            bin_calib =  np.zeros(shape=(num,num),dtype = object)
            wv = []
            for i in data['Calib'].keys():
                wv.append(eval(i))
            for i in range(num):
                for j in range(num):
                    calib_photon[i,j] = []
                    for k in wv:
                        calib_photon[i,j] = np.concatenate((calib_photon[i,j],data['Calib'][str(k)][str(i)+'_'+str(j)][1]),axis = None)
                    # print(np.shape(calib_photon[i,j]))
                    hist,bin = np.histogram(calib_photon[i,j],bins=100)
                    a,_ = signal.find_peaks(hist,prominence = 200,distance = 5)
                    bin_calib[i,j] = a + bin[0]
                    interp[i,j] = CubicSpline(wv,bin_calib[i,j][::-1])
                    plt.sca(axes[i*num+j])
                    plt.hist(calib_photon[i,j],bins = 100)
                    plt.xticks([], [])
                    plt.yticks([], [])
            st.pyplot(f)


            fig2 = plt.figure()



            t = np.linspace(0.2,1.2,100)
            for i in range(num):
                for j in range(num):
                
            #         # ax2 = a[i,j]
                    plt.subplot(num,num,i*num+j+1)
                    plt.plot(t,interp[i,j](t),c='b')
                    plt.scatter(wv,bin_calib[i,j][::-1],s=7.5,c='r')
                    plt.xticks([], [])
                    plt.yticks([], [])
            # ax1.plot1(t,interp[0,0](t))
            plt.xlim([0.2,1.2])
            
            st.pyplot(fig2)


