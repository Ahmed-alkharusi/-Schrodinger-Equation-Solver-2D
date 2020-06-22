# The Schrodinger Equation Solver app
This app solves the 2D Schrodinger Equation numerically for arbitrary potential using the finite difference method. Just paste the photo of the infinite potential well.

## For the detailed report see
https://www.researchgate.net/publication/340984532_Scars_in_the_wavefunction_A_study_of_different_potential_wells_using_the_finite_difference_method

## A YouTube tutorial on how to use the app
https://youtu.be/48cgQMdw94g

## How to use the app (summary):
1. Paste the photo of the potential well in the same app file. The photo should be in black and white only. See the example provided.
The resolution of the results depends on the resolution of the inputted photo. Start with 30 by 30 pixels photo to see how long the app will take
2. Paste the image name in imagename.txt 
3.Select the range of energy values (Results) in energyrange.txt 
4. To load the results into python use
e_vec = np.load('....npy')
e_values = np.load('....npy')

## Examples
### The heart potential
![alt text](https://github.com/Ahmed-alkharusi/Schrodinger-Equation-Solver/tree/master/Examplesexample.PNG?raw=true)
### The stadium billiard 
![alt text](https://github.com/Ahmed-alkharusi/Schrodinger-Equation-Solver/blob/master/example5.PNG?raw=true)
### Sinai's billiard
![alt text](https://github.com/Ahmed-alkharusi/Schrodinger-Equation-Solver/blob/master/example1.PNG?raw=true)
### The diamond potential
![alt text](https://github.com/Ahmed-alkharusi/Schrodinger-Equation-Solver/blob/master/example3.PNG?raw=true)

### Also, the app can be used to study the scars in the wavefunction. This is an example,
![alt text](https://github.com/Ahmed-alkharusi/Schrodinger-Equation-Solver/blob/master/example4.PNG?raw=true)

## For more examples, see
https://drive.google.com/drive/folders/1oS9dF2Q94D5c0zO84e2bC_oAiCWi8uA8?usp=sharing
## Authors
@main_author: Ahmed Alkharusi 

Esah Bannister has participated in writing the code and the report. 
esah.bannister@student.manchester.ac.uk
