import pandas as pd
import scipy.stats as stats

# Organize the data into a DataFrame
data = {
    'Treatment': ['A low, B low']*3 + ['A high, B low']*3 + ['A low, B high']*3 + ['A high, B high']*3,
    'Yield': [28, 25, 27, 36, 32, 32, 18, 19, 23, 31, 30, 29]
}

df = pd.DataFrame(data)

# Perform ANOVA
anova_result = stats.f_oneway(
    df[df['Treatment'] == 'A low, B low']['Yield'],
    df[df['Treatment'] == 'A high, B low']['Yield'],
    df[df['Treatment'] == 'A low, B high']['Yield'],
    df[df['Treatment'] == 'A high, B high']['Yield']
)

print(anova_result)