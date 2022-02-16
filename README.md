# vaccines

Collaborative project to investigate vaccine effectiveness

## CDC data

Download and compress the CDC vaccination data. See Makefile for details (credit to Philip for the makefile).

```
make cdcdata
```

## JHU data

Please refer to this file for a Python script that downloads the JHU data and makes a csv (credit to Bridget for this file).

```
bridget_JHU_merge.py
```

## Processing and visualization

Please refer to this file for a Python script that process the data, cleans it, and generates 3 scatterplots. 

```
vaccine_data_total.py
```

## Results

When you generate a plot using 05/01/2021 as the date, the script shows this plot:

![Outlier](05.01.outlier.png)

Clearly there is some kind of an outlier here, but if we look closer at the cluster of points we get this:

![May](05.01.png)

Running the script again at July 1:

![July](07.01.png)

And November 30:

![November](11.30.21.png)


