# Assignment 6 - Data Munging

This branch demonstrates my idea for using dataframe.join to create our plotting data without writing any intermediate files.

### vaccines.py
This file is relatively simple; once the dataframe is created the only munging necessary are to filter by the end date date and remove missing data.

The resulting dataframe is printed below:

```
Total vaccine rows, cols: (1404601, 52)
Total 11/30/2021 rows, cols: (3283, 2)
Valid 11/30/2021 rows, cols: (3221, 2)
       Series_Complete_18PlusPop_Pct  Census2019_18PlusPop
FIPS
19093                           59.1                5173.0
06015                           46.3               21990.0
20207                           48.9                2465.0
08109                           40.2                5381.0
29161                           48.1               35235.0
...                              ...                   ...
37141                           56.9               49058.0
51191                           62.4               44077.0
42113                           48.5                5428.0
55091                           54.7                5768.0
36103                           82.0             1167503.0

[3221 rows x 2 columns]
```

### deaths.py
Since the JHU data is showing deaths as a cumulative number, if we want the change during some interval, we need to subtract the difference in deaths between the start and end of the interval.

This file takes care of retreiving the data for each data and formatting the dataframe in readit(), then performs the subtraction operation in deaths_sample

The resulting dataframe is printed below:

```
       Deaths
FIPS
00060     0.0
00066   124.0
00069     1.0
00078    60.0
01001    47.0
...       ...
90053     1.0
90054     0.0
90055     0.0
90056     0.0
99999     0.0
```
the FIPS with only 2 digits are US territories, the FIPS starting with 9---- are unspecified are not specified in the census.


### combinedata.py

This file is short enough that it should get rolled into another program, in my opinion. The outputs of vaccines.py and deaths.py are both index by FIPS and the default dataframe.join() behavior will join their columns by matching indices. 

The resulting dataframe is printed below:

```
Total vaccine rows, cols: (1404601, 52)
Total 11/30/2021 rows, cols: (3283, 2)
Valid 11/30/2021 rows, cols: (3221, 2)
       Deaths  Series_Complete_18PlusPop_Pct  Census2019_18PlusPop
FIPS
01001    47.0                           45.3               42904.0
01003   278.0                           55.9              175680.0
01005    21.0                           49.0               19604.0
01007    30.0                           38.2               17837.0
01009    53.0                           35.8               44571.0
...       ...                            ...                   ...
72145     0.0                           83.1               41052.0
72147     0.0                           83.2                6882.0
72149     0.0                           89.5               17539.0
72151     0.0                           76.9               26493.0
72153     0.0                           82.8               27554.0

[3194 rows x 3 columns]
```