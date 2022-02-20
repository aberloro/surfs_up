# surfs_up
 Use SQLite, Python to analyze climate for surf n shake shop

## Overview of Project

### Background

A potential investor has asked for weather analysis prior to backing a proposed Surf N Shake Shop. [Phase1](https://github.com/aberloro/surfs_up/blob/main/Phase1/climate_analysis.ipynb) of this project showed the average precipitation per day over the previous year was an acceptable 0.18 inches at the proposed location, and that most days of the year (325 of 365) had a favorable temperature of over 67 degrees F. 

### Purpose
The purpose of this project is to expand upon Phase1 by digging deeper into the temperature data of June and December in Oahu to see if the proposed business is sustanable year-round. 

### Deliverables
  1. Determine Summary Statistics for June
  2. Determine Summary statistics for December
  3. Written README.md report of the statistical analysis

### Resources
 - Data Sources: hawaii.sqlite
 - Technology: SQLite, SQLAlchemy, VS Code, Jupyter Notebook 6.4, Python 3.7

 ## Results
 Theree are three major differences in the June vs December temperature data:
   1. The average temperature is lower in December: 71 degrees vs 75 in June.
   2. The minimum temperate in significantly lower in December: 56 degrees vs 64 in June.
   3. The maximum temperature is slightly lower in December: 83 degrees vs 85 in June.

   ![Jun_Dec_Temp_Stats](https://user-images.githubusercontent.com/93740725/154869183-5673da73-d0b0-4fce-89f0-1b3dac30ad9a.png)


 ## Summary
 ### Conclusions
December is a cooler month than June, but only by about 4 degrees on average.  A daily temperature averge of 71 degrees in Decemebr still makes for nice surfand shake weather.  Both months share a similar max temp, in the mid 80s, but looker for lower lows in December where we can expect fewer busy days based on minimum temps.

 ### Additional Analysis
It would be helpful for investors to see precipitation data for June and December in addition to the temperature data.  

  1. Look for an average of 0.14 inches and a max of 4.43 inches of rain in June.
  2. Expect an average of 0.22 inches and a max of 6.42 inches of rain in December. 
  3. Plots of average daily rain show that year over year amounts are relatively consistent, with the exception of an extremly wet season in June of 2011. 

June Precipitation Stats and Plot:

![June_Precip](https://user-images.githubusercontent.com/93740725/154869217-4a3b4123-c19c-4aa6-95a0-c86403fe3a51.png)


December Precipitation Stats and Plot:

![December_Precip](https://user-images.githubusercontent.com/93740725/154869235-57443ba1-7469-4f3e-a792-c27be8e4794b.png)
