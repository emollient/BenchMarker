#R script for BenchMaker using paird t-test
#Author: Susan Lunn


library(jsonlite)

data <- fromJSON(paste(getwd(), "json.txt", sep="/"))
exec1 <-data[[1]]
exec2 <-data[[2]]
#generatingsomedata
 
#Settinguptwoscreens
par(mfrow=c(1,2))
 
#FirstGraph
s<-seq(length(exec1))
par(bty="l")
boxplot(exec1,exec2,main="Rawdata",xlab="exec1, exec2",ylab="Time",col=c("lightblue","lightgreen"))
stripchart(list(exec1,exec2),vertical=T,pch=16,method="jitter",cex=0.5,add=T)
segments(rep(0.95,length(exec1))[s],exec1[s],rep(2,length(exec1))[s],exec2[s],col=1,lwd=0.5)
#Secondgraph
#Confidenceintervals eitherparametric (t.test) or non-parametric (wilcox.text)
res<-wilcox.test(exec2,exec1,paired=T,conf.int=T)
 
stripchart(exec2-exec1,vertical=T,pch=16,method="jitter",main="Difference",ylab="Difference:exec2–exec1",xlab="Median+/-95%CI")
points(1,res$estimate,col="red",pch=16,cex=2)
arrows(1,res$conf.int[1],1,res$conf.int[2],col="red",code=3,lwd=3,angle=90)
abline(h=0,lty=2)#Zero-effectline

