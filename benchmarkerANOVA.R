#R script for BenchMarker using ANOVA test
#Author: Susan Lunn

library(jsonlite)

data1 <- fromJSON(paste(getwd(), "json.json", sep="/")) 

boxplot(data1, col=c("lightblue","lightgreen"))
stripchart(data=data1,vertical=T,pch=16,method="jitter",cex=0.5,add=T)
