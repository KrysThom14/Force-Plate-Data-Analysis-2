# Force-Plate-Data-Analysis-2
This was initially part of an assignment I had from grad school (Exercise Science) in my Biomechanics class. This is just a result of me taking a deeper dive into the analysis of the data using Python. This part of the assignment had to do with analyzing a 60sec. recording of someone performing a Double-Leg Quiet Stance on a Force Plate. The primary measurements in question are Center of Pressure (COP) & Force Data. I have the results of the calculations in each section commented out, as well as the calculations themselves so that I can run one at a time...instead of all at once.

### Quick Glimpse Into What The DF Looks Like
* This is just for reference. I primarily used the csv sheet itself to view the data in full.

![Signal4-1](https://user-images.githubusercontent.com/94875597/172924976-2c9b2705-c86c-4999-aac3-60415e92d825.png)


### Calculating Common Aggregates
* The pictures show the calculations for the COP data in the X direction (i.e. Medial/Lateral) and a box plot showing a quick visual summary of the values in that column. This was also done for COP:Y and the forces in the X & Y directions.

![Signal4-2](https://user-images.githubusercontent.com/94875597/172925466-e1f60092-e865-4a53-b06b-8b256a592842.png)

![Signal4-3](https://user-images.githubusercontent.com/94875597/172925496-b8da0fba-a23e-48dc-bb95-eed528006604.png)


### Moving-Point Average
* Only did this because it was part of my original assignment in grad school, and I wanted to see if I could replicate it in python. I created a function that took a 30-point average (i.e. average every 30 rows together) of the COP data and then graphed that. The purpose of this was that it allowed us to better see variations over time. The graph below just shows the data for COP in the medial/lateral direction.

![Signal4-4](https://user-images.githubusercontent.com/94875597/172925797-4a2340ea-7d9c-4876-9b8c-f119d7bdb4bd.png)

![Signal4-5](https://user-images.githubusercontent.com/94875597/172925835-38759f6b-918a-4c41-a231-40539a93f262.png)


### Force Data
* This is a visual of the forces in the anterior/posterior direction over time (no moving-point average).
 
![Signal4-6](https://user-images.githubusercontent.com/94875597/172926345-2c709fa5-6192-473a-91e2-4a991df71f36.png)

![Signal4-7](https://user-images.githubusercontent.com/94875597/172926411-a79e50d0-d5ce-4f0d-a080-cac04782f2e5.png)




