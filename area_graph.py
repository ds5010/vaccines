import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})
df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

xlabel = 'Series_Complete_18PlusPop_Pct'
ylabel = 'Deaths_Per_1e5'



x = df[xlabel]
y = df[ylabel]
area = df['Census2019_18PlusPop'] / 1e4

fig, ax = plt.subplots()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(0,100)
ax.set_ylim(0,500)
fig.set_size_inches(8,8)

scatter = ax.scatter(x, y, s=area, alpha=0.5)

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)", labelspacing=2, borderpad=1); # Haven't figured out how to make the numbers from the legend different
plt.show()
