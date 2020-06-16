# Schrodinger-Eq-Solver-1.0
for the detailed report see

https://www.researchgate.net/publication/340984532_Scars_in_the_wavefunction_A_study_of_different_potential_wells_using_the_finite_difference_method

'''Copyright: @main_author: Ahmed Alkharusi  Esah Bannister has participated in writing the code.  13th April 2020 2D Schrodinger Equation solver 
This code solves the 2D Schrodinger Equation numerically for arbitrary potential using the finite difference method. Just paste the photo of the infinite potential well.
Have fun!

How to use the app:
1. Paste the photo of the potential well in the same app file. The photo should be black and white only. See the example provided.
The resolution of the results depends on the resolution of the inputted photo. Start with 30 by 30 pixels photo to see how long the app will take
2. Paste the image name in imagename.txt 
3.Select the range of energy values (Results) in energyrange.txt 
4. To load the results into python use
e_vec = np.load('....npy')
e_values = np.load('....npy')'''
