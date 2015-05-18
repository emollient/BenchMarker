# BenchMarker
Statistically Robust Benchmarking


###Statistics
With 2 executables, paired t-test is used and a boxplot is generated.

With >2 executables, ANOVA test is used. 


#### paired t-test
A paired t-test is used to compare two population means where you have two samples
in which observations in one sample can be paired with observations in the other sample.
It is used to determine if two sets of data are significantly different from one another.

#### ANOVA test
ANOVA is similar to t-tests, but is used to find variance among means of greater than two
datasets.



##Installation
```
pip install -r requirements.txt
```

##Command line args
```
python benchmarker.py -exec foo1 -exec foo2 -arg foo2arg -arg foo2arg1
```


![graphs](Rplots.pdf)


