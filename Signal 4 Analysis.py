# Double-Leg Quiet Stance
# Analysis of raw Force Plate Data - 60sec. @ 1,000Hz

# Import libraries that may be needed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("E:/Biomechanics/Force Plate - Signal 4.csv")
#print(df.head())


# mm = millimeters

cop_x_mean = df['COP:X'].mean()
#print(cop_x_mean)
"244.47mm"
cop_x_median = df['COP:X'].median()
#print(cop_x_median)
"243.88mm"
cop_x_min = df['COP:X'].min()
#print(cop_x_min)
"208.57mm"
cop_x_max = df['COP:X'].max()
#print(cop_x_max)
"288.08mm"
cop_x_range = (df['COP:X'].max()) - (df['COP:X'].min())
#print(cop_x_range)
"79.52mm"
cop_x_std = df['COP:X'].std()
#print(cop_x_std)
"14.34mm"

# ax = plt.subplot()
# plt.boxplot(df['COP:X'], vert = False)
# ax.set_yticklabels(['60sec.'])
# plt.title('Medial/Lateral COP Data Distribution (mm)')
# plt.show()


cop_y_mean = df['COP:Y'].mean()
#print(cop_y_mean)
"315.13mm"
cop_y_median = df['COP:Y'].median()
#print(cop_y_median)
"315.52mm"
cop_y_min = df['COP:Y'].min()
#print(cop_y_min)
"147.33mm"
cop_y_max = df['COP:Y'].max()
#print(cop_y_max)
"489.09mm"
cop_y_range = (df['COP:Y'].max()) - (df['COP:Y'].min())
#print(cop_y_range)
"341.77mm"
cop_y_std = df['COP:Y'].std()
#print(cop_y_std)
"113.81mm"

# ax = plt.subplot()
# plt.boxplot(df['COP:Y'])
# ax.set_xticklabels(['60sec.'])
# plt.title('Anterior/Posterior COP Data Distribution (mm)')
# plt.show()

# N = Newtons

force_x_mean = df['Force:X'].mean()
#print(force_x_mean)
"2.50N"
force_x_median = df['Force:X'].median()
#print(force_x_median)
"2.57N"
force_x_min = df['Force:X'].min()
#print(force_x_min)
"-12.41N"
force_x_max = df['Force:X'].max()
#print(force_x_max)
"14.36N"
force_x_range = (df['Force:X'].max()) - (df['Force:X'].min())
#print(force_x_range)
"26.77N"
force_x_std = df['Force:X'].std()
#print(force_x_std)
"3.90N"

# ax = plt.subplot()
# plt.boxplot(df['Force:X'], vert = False)
# ax.set_yticklabels(['60sec.'])
# plt.title('Medial/Lateral Force Data Distribution (N)')
# plt.show()

force_y_mean = df['Force:Y'].mean()
#print(force_y_mean)
"-4.32N"
force_y_median = df['Force:Y'].median()
#print(force_y_median)
"-4.50N"
force_y_min = df['Force:Y'].min()
#print(force_y_min)
"-60.52N"
force_y_max = df['Force:Y'].max()
#print(force_y_max)
"52.65N"
force_y_range = (df['Force:Y'].max()) - (df['Force:Y'].min())
#print(force_y_range)
"113.17N"
force_y_std = df['Force:Y'].std()
#print(force_y_std)
"31.68N"

# ax = plt.subplot()
# plt.boxplot(df['Force:Y'])
# ax.set_xticklabels(['60sec.'])
# plt.title('Anterior/Posterior Force Data Distribution (N)')
# plt.show()

force_z_mean = df['Force:Z'].mean()
#print(force_z_mean)
"812.54N"
force_z_median = df['Force:Z'].median()
#print(force_z_median)
"811.63N"
force_z_min = df['Force:Z'].min()
#print(force_z_min)
"797.68N"
force_z_max = df['Force:Z'].max()
#print(force_z_max)
"835.19N"
force_Z_range = (df['Force:Z'].max()) - (df['Force:Z'].min())
#print(force_Z_range)
"37.51N"
force_z_std = df['Force:Z'].std()
#print(force_z_std)
"6.33N"


#-----------------------------------------------------------------------------#
"VISUAL COMPARISON BETWEEN CENTER OF PRESSURE (X,Y) DATA"


cop_point_avg = 30
cop_list = []

def point_avg(data):
    data_sum = 0
    count = 0
    for num in data:
        data_sum += num
        count += 1
        if count == cop_point_avg:
            cop_list.append(data_sum / cop_point_avg)
            data_sum = 0
            count = 0
    return cop_list

cop_x_30 = point_avg(df['COP:X'])
#print(cop_x_30)

# ax = plt.subplot()
# plt.plot(cop_x_30, range(len(cop_x_30)))
# plt.xlabel('Medial/Lateral Movement (mm)')
# plt.ylabel('Time')
# plt.title('Center of Pressure M/L Displacement (1000Hz)')
# ax.set_yticks([0.0, (5/60) * float(len(cop_x_30)),
#               (10/60) * float(len(cop_x_30)), (15/60) * float(len(cop_x_30)),
#               (20/60) * float(len(cop_x_30)), (25/60) * float(len(cop_x_30)),
#               (30/60) * float(len(cop_x_30)), (35/60) * float(len(cop_x_30)),
#               (40/60) * float(len(cop_x_30)), (45/60) * float(len(cop_x_30)),
#               (50/60) * float(len(cop_x_30)), (55/60) * float(len(cop_x_30)),
#                (1.0) * float(len(cop_x_30))])
# ax.set_yticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.', '25sec.',
#                     '30sec.', '35sec.', '40sec.', '45sec.', '50sec.', '55sec.',
#                     '60sec.'])
# plt.show()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

"Now we will do the same for the y-axis"


cop_y_30 = point_avg(df['COP:Y'])
#print(cop_y_30)

# ax = plt.subplot()
# plt.plot(range(len(cop_y_30)), cop_y_30)
# plt.xlabel('Time')
# plt.ylabel('Anterior/Posterior Movement (mm)')
# plt.title('Center of Pressure A/P Displacement (1000Hz)')
# ax.set_xticks([0.0, (5/60) * float(len(cop_y_30)),
#               (10/60) * float(len(cop_y_30)), (15/60) * float(len(cop_y_30)),
#               (20/60) * float(len(cop_y_30)), (25/60) * float(len(cop_y_30)),
#               (30/60) * float(len(cop_y_30)), (35/60) * float(len(cop_y_30)),
#               (40/60) * float(len(cop_y_30)), (45/60) * float(len(cop_y_30)),
#               (50/60) * float(len(cop_y_30)), (55/60) * float(len(cop_y_30)),
#                (1.0) * float(len(cop_y_30))])
# ax.set_xticklabels(['0sec.', '5sec.', '10sec.', '15sec.', '20sec.', '25sec.',
#                     '30sec.', '35sec.', '40sec.', '45sec.', '50sec.', '55sec.',
#                     '60sec.'], rotation = 30)
# plt.show()


#-----------------------------------------------------------------------------#
"VISUALIZATION OF FORCE (X,Y,Z) DATA"

"""Due to the nature of the negative(-) numbers in this data set, taking a
30-point average would not give us the most accurate data"""

force_x = df['Force:X']

# ax = plt.subplot()
# plt.plot(force_x, range(len(force_x)))
# plt.xlabel('Medial/Lateral Forces (N)')
# plt.ylabel('Time')
# plt.title('Medial/Lateral Force Production (1,000Hz)')
# ax.set_yticks([0.0, (10/60) * float(len(force_x)),
#               (20/60) * float(len(force_x)), (30/60) * float(len(force_x)),
#               (40/60) * float(len(force_x)), (50/60) * float(len(force_x)),
#                (1.0) * float(len(force_x))])
# ax.set_yticklabels(['0sec.', '10sec.', '20sec.', '30sec.', '40sec.',
#                     '50sec.', '60sec.'])
# plt.show()


            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

force_y = df['Force:Y']

# ax = plt.subplot()
# plt.plot(range(len(force_y)), force_y)
# plt.xlabel('Time')
# plt.ylabel('Anterior/Posterior Forces (N)')
# plt.title('Anterior/Posterior Force Production (1,000Hz)')
# ax.set_xticks([0.0, (10/60) * float(len(force_y)),
#               (20/60) * float(len(force_y)), (30/60) * float(len(force_y)),
#               (40/60) * float(len(force_y)), (50/60) * float(len(force_y)),
#                (1.0) * float(len(force_y))])
# ax.set_xticklabels(['0sec.', '10sec.', '20sec.', '30sec.', '40sec.',
#                     '50sec.', '60sec.'])
# plt.show()

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

"""When it comes to measuring the Z Force during a quiet stance, it is usually
only useful when performing more complex calculations. But we can use it to
determine the weight of the individual that this data was taken from."""

weight_kg = force_z_mean / 9.81  # 9.81 = Force from gravity
# weight_kg = 82.83kg

weight_lbs = weight_kg * 2.2
# weight_lbs = 182.22lbs.
