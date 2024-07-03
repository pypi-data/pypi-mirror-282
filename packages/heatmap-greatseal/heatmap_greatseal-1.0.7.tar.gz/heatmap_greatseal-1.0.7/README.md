# Heatmap
Matrix operations and visualization

## Installation
```
pip install heatmap_greatseal
```
## Usage
```
import heatmap_greatseal.heatmap_greatseal as hm
```
You can easily generate custom sized matrix with upper and lower limit. It creates the matrix of h and w size of integers.
```
hm.generate(h,w,min,max)
```
By using grid or gaussian visualization it calculates every cell's value ratio to neighbouring cells' values.  
Grid visualization uses no interpolation and blur:
```
hm.grid_visualize(matrix)
```
However, gaussian visualization creates a heatmap rather than a grid of the matrix using gaussian interpolation:
```
hm.gaussian_visualize(matrix)
```
If you want to create multiple figures at the same time, they will not show simultaneously, unless you give a *False* parameter to every function except the last one called::
```
hm.grid_visualize(matrix, False)
hm.grid_visualize(matrix)
```