''' 
@main_author: Ahmed Alkharusi
Esah Bannister has participated in writing the code.

 June 2020 
 
# =============================================================================
# 2D Schrodinger Equation solver
# =============================================================================



# =============================================================================
# For the detailed explanation please see section 3.1 of the project report
 (link in README.md)
# =============================================================================
'''
# =============================================================================
# IMPORTANT!
# If you are executing the code using Spyder IDE do the following:
#     1. Tools -> Preferences -> Run;
#     2. under Console select Execute in an external system terminal;
#     3. make sure that you have kivy installed
# 
#     otherwise; you might have some problems when tring to execute the :
#     code in the existing console.
# 
# =============================================================================
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image
from numpy import array, empty
import numpy.version

class MainWindow(Screen):
    energy_min = ObjectProperty(None)
    energy_max = ObjectProperty(None)
    picture_name = ObjectProperty(None)
    current = ""
    
    def general_potential(self,filename):
        """ input: filename is a string.
            
            returns an array [e_values, e_vec] such that v[:,i] is the e_vec of
            the e_values[i]
        
        """
        
        #~~~~~~~~~~~~~~~for circular potentail
        temp=Image.open(str(filename))
        temp=temp.convert('1')      # Convert to black & white (just in case the image is not B&W)
        bool_photo_matrix = array(temp)             # Creates an array, white pixels=True and black pixels=False
        binary_photo_matrix = empty((bool_photo_matrix.shape[0], bool_photo_matrix.shape[1]),None)    #New array with same size as A
        
        global M,N 
        N = len(bool_photo_matrix[:,0])   #Points in x-axis 
        
        M = len(bool_photo_matrix[0])
        for i in range(len(bool_photo_matrix)):
            for j in range(len(bool_photo_matrix[i])):
                if bool_photo_matrix[i][j]==True:
                    binary_photo_matrix[i][j]=0
                else:
                    binary_photo_matrix[i][j]=1
        
                   
        global position_mesh
        position_mesh = binary_photo_matrix
        position_mesh = np.transpose(position_mesh)
        
    # =============================================================================
    #     global unflattened_position_mesh # plot this to check the answer and compare it with the input photo
    #     unflattened_position_mesh = position_mesh
    # =============================================================================
        position_mesh = np.matrix.flatten(position_mesh)
         
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
        No_points = M*N
        x_intervals = np.linspace(0,1,M)
        increment = np.absolute(x_intervals[0]-x_intervals[1])
        
        """ This constructs the Hamiltonian using the position_mesh, which was constructed using the
        input photo, for the detailed explanation please see section 3.1 of the project report (link in README.md)"""
        global Hamiltonian
        Hamiltonian = np.zeros(pow(No_points,2)).reshape(No_points,No_points)
        
        # j = row and i = col. 
        for j in range(No_points):
            
            if position_mesh[j] != 0:                  
                for i in range(No_points):
                    
                    if j <= len(position_mesh):
                        if i == j + 1 and i%N!=0 and position_mesh[j+1] != 0:
                            Hamiltonian[j][i]=-1/pow(increment,2) 
                        
                        if i == j - 1 and j%N !=0 and position_mesh[j-1] != 0:
                            Hamiltonian[j][i]=-1/pow(increment,2) 
                            
                        if i == j - N and position_mesh[j-N]: 
                            Hamiltonian[j][i]=-1/ pow(increment,2)
                        
                        if i == j + N and position_mesh[j+N]: 
                            Hamiltonian[j][i]=-1/ pow(increment,2)
                    
                    if i == j:
                        Hamiltonian[j][i]=4/ pow(increment,2)
                        
        e_values, e_vec = np.linalg.eig(Hamiltonian)
        
        return [e_values, e_vec]
        
    def runButton(self):
        
        global energy_min, energy_max, picture_name
        energy_min = self.energy_min.text 
        energy_max = self.energy_max.text 
        picture_name = self.picture_name.text 
        
        #Results~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        try:
             
            t = MainWindow()
            e_values, e_vec = t.general_potential(picture_name)  
            #sort  
            idx = e_values.argsort()[::-1]   
            e_values = e_values[idx]
            e_vec = e_vec[:,idx]
                
                #Plots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            input_data = [int(energy_min), int(energy_max)]
            for i in range(int(input_data[1])):
                if i >= input_data[0]:
                    figi, axi = plt.subplots(1, 1)
                    plot = plt.imshow( np.transpose( pow( np.absolute( e_vec[:,i].reshape(M,N) ) ,2)),cmap='magma', interpolation ='gaussian' ) #check this carefully and M, N
            
                    plt.setp(axi, xticks=[], yticks=[])
                    divider = make_axes_locatable(axi)
                    cax = divider.append_axes("right", size="3%", pad=0.1)
                    cbar = figi.colorbar(plot, ax=axi, extend='both', cax=cax)
                    cbar.minorticks_on()
                    cbar.ax.tick_params(labelsize=5,pad=0.1)
                    
                    if i == 0:
                        axi.set_title('The ground excited state',fontsize=12)
                        
                    elif i == 1:
                        axi.set_title('The 1$^{st}$ excited state',fontsize=12)
                        
                    elif i == 2:
                        axi.set_title('The 2$^{nd}$ excited state',fontsize=12)
                        
                    elif i == 3:
                        axi.set_title('The 3$^{rd}$ excited state',fontsize=12)
                        
                    else:
                        axi.set_title(str(i)+'$^{th}$ excited state',fontsize=12)   
                        
                    plt.savefig( str(i)+'.pdf')
                        
            plt.show()
    
            print(energy_min, energy_max, picture_name)
            self.reset()
            runSuccess()
        except:
            runFail()
        
    def how(self):
        self.reset()
        interface.current = "how"
        
    def about(self):
        self.reset()
        interface.current = "about"
        
    def reset(self):
        self.energy_min.text=""
        self.energy_max.text=""
        self.picture_name.text=""
        
    
        
class HowWindow(Screen):
    
    def goMain(self):

        interface.current = "main"
        

        
class AboutWindow(Screen):
    def goMain(self):

        interface.current = "main"
        
        
class WindowManager(ScreenManager):
    pass

def runSuccess():
    pop = Popup(title='Successful!',
                  content=Label(text='WARNING! For an average PC, the app will take \na very long time for high resolution photo ( > 70 * 70 pixels). \n\nThe pdf plots are saved in the app directory.\n \nThanks for trying out the Schrodinger app!'
                                , font_size=19),
                  size_hint=(None, None), size=(600,600))
    pop.open()
def runFail():
    pop = Popup(title='Failed!',
                  content=Label(text="""Please check that: \n1) the photo is saved in the same app directory;\n2) Lowest energy state < Highest energy state;\n3) the filename extension (e.g. .png or .jpg) \n is included in the name of the potential""", font_size=19),
                  size_hint=(None, None), size=(600, 600))
    pop.open()



kv = Builder.load_file("schrodinger.kv")
interface = WindowManager() 

screens = [MainWindow(name="main"),HowWindow(name="how"), AboutWindow(name="about")] 

for screen in screens:
    interface.add_widget(screen)

interface.current ="main"
class Schrodinger(App):           #inheritance
    def build(self):
        return interface

if __name__ == "__main__":
    Schrodinger().run()
    

#Functions defn~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
