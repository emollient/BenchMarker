#R script for BenchMaker
#Author: Susan Lunn

##TODO: parse JSON file, do the stats

library(jsonlite)

data1 <- fromJSON(paste(getwd(), "json.txt", sep="/"))

#cycle through all the execs in data1
names(data1)
data1$bash.sh
data1$bash2.sh

#stats it!

t.test(data1$bash.sh, data1$bash2.sh)






