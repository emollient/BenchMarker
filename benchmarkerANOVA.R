#R script for BenchMarker using ANOVA test
#Author: Susan Lunn

library(jsonlite)

data1 <- fromJSON(paste(getwd(), "json.txt", sep="/")) 

out <- lapply(data1, str_length)
data1 <- cbind(data1, out)


#summary(fit)
