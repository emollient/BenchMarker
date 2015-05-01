#R script for BenchMaker using paird t-test
#Author: Susan Lunn


library(jsonlite)

data <- fromJSON(paste(getwd(), "json.json", sep="/"))
exec1 <-data[[1]]
exec2 <-data[[2]]
par(mfrow=c(1,2))
 
#FirstGraph
s<-seq(length(exec1))
par(bty="l")
boxplot(exec1,exec2,main="Difference in means",xlab="exec1, exec2",ylab="Time",col=c("lightblue","lightgreen"))
stripchart(list(exec1,exec2),vertical=T,pch=16,method="jitter",cex=0.5,add=T)
#segments(rep(0.95,length(exec1))[s],exec1[s],rep(2,length(exec1))[s],exec2[s],col=1,lwd=0.5)
#Secondgraph
#Confidenceintervals eitherparametric (t.test) or non-parametric (wilcox.text)
#Why is R so hard :(
res<-wilcox.test(exec2,exec1,paired=T,conf.int=T)
print(res)
 

