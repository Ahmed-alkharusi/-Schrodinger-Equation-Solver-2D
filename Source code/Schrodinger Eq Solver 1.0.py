''' 
@main_author: Ahmed Alkharusi
Esah Bannister has participated in writing the code.

 June 2020 
 
# =============================================================================
# 2D Schrodinger Equation solver
# =============================================================================
          
This code solves the 2D Schrodinger Equation numerically for arbitrary potential well
using the finite difference method.Just paste the photo of the infinite potential well.


How to use the app:
1. Paste the photo of the potential well in the same app file.
The photo should be black and white only.
See the examples provided.

The resolution of the results depends on the resolution of the inputted photo.
Start with 30 by 30 pixels photo to see how long the code will take.

2. Paste the image name in imagename.txt 
3. Select the range of energy values (Results) in energyrange.txt 
4. To load the results into python use
e_vec = np.load('....npy')
e_values = np.load('....npy')



# =============================================================================
# For the detailed explanation please see section 3.1 of the project report
 (link in README.md)
# =============================================================================
'''


import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image
from numpy import array, empty
import numpy.version

try:
    """input_data = [Lowest energy state (to be calculated), Highest energy state,
    1 if the user wants to save the output as a numpy array]"""
    
    input_data = np.genfromtxt('energyrange.txt', comments = '%', skip_header = 1, delimiter = ',')
    imagename = np.loadtxt('imagename.txt', dtype='str', comments = '%', delimiter = ',')

except:
    
    sys.exit('Both data files must be saved in the same folder as the code file!')

#Functions defn~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def general_potential(filename):
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


#Results~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
e_values, e_vec = general_potential(imagename)   

#sorts the e_values and e_vec
idx = e_values.argsort()[::-1]   
e_values = e_values[idx]
e_vec = e_vec[:,idx]

#Plots~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


if input_data[2] == 1:
    """a random number is included so the the results are not overwritten 
    when the code is executed again"""
    np.save('data e values ' + str(np.random.randint(1000)), e_values)
    np.save('data e vectors ' + str(np.random.randint(1000)), e_vec)

    



  

