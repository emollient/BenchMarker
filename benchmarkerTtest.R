#R script for BenchMaker using paird t-test
#Author: Susan Lunn


library(jsonlite)

data1 <- fromJSON(paste(getwd(), "json.json", sep="/"))
df = data.frame(data1)
exec1 <- data1[[1]]
exec2 <- data1[[2]]
btwn <- t.test(exec1, exec2)
print(btwn)
 
#FirstGraph
s<-seq(length(exec1))
par(bty="l")
boxplot(exec1,exec2,main="Difference in means",xlab="exec1, exec2",ylab="Time",col=c("lightblue","lightgreen"))
stripchart(list(exec1,exec2),vertical=T,pch=16,method="jitter",cex=0.5,add=T)
