#R script for BenchMarker using ANOVA test
#Author: Susan Lunn

library(jsonlite)

df <- fromJSON(paste(getwd(), "json.json", sep="/")) 

output <-  data.frame(Script=character(), Time=numeric(), stringsAsFactors=TRUE)

#thanks ryan brown :)
for(i in names(df)) { output <- rbind( output, cbind(rep(i, length(df[[i]])), df[[i]])) }

##FIT ANOVA AND PRINT RESULTS

oneway.test(output[1]~output[2], data=output)

boxplot(data1, xlab="Executables", ylab="Time(means)", col=c("lightblue","lightgreen"))
