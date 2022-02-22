# DS5010 Spring 2022
## **Tim Moriarity**
### Vaccine Effectiveness

Packages:
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


Loading CDC Data into Pandas Dataframe:
```
url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})
```

Examine Dataframe:
```
df.head(10)
```
