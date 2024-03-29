# prisma_luminance_data
An archive of historical luminance data for the Prisma BOLD screen affiliated with the Carnegie Mellon University Brain Imaging Data Generation &amp; Education (BRIDGE) Center.


This repository contains luminance data for the BOLD32 screen associated with the Prisma MRI scanner at the Carnegie Mellon University BRIDGE Center under varying light conditions and color gun intensities. <br><br>
Each data file contains luminance data (cd/m^2) recorded with an LS-150 Minolta luminance meter while ambient lighting was 25%, 50%, and 100% of the maximum (as of 6/26/19). <br><br>

For example, ``` 100p_lum_data.csv ``` contains luminance data for red, green, blue, and all three color gun intensities under maximum lighting conditions, with a column for each color gun and a row for each set of measured luminance values:

bw | red | green | blue 
------------ | ------------- | ------------- | -------------
 1.415 | 1.432 |  1.269 | 1.276
...| ... | ... | ...


<br>

``` measure_luminance.py ``` varies color gun intensities with the option of automated measurement. <br>
``` plot_luminance_color.ipynb ``` plots luminance as a function of color gun intensity. 



