#R script for BenchMarker using ANOVA test
#Author: Susan Lunn

library(jsonlite)

data1 <- fromJSON(paste(getwd(), "json.json", sep="/")) 

##FIT ANOVA AND PRINT RESULTS
boxplot(data1, xlab="Executables", ylab="Time(means)", col=c("lightblue","lightgreen"))
