dt<-Exp.Tot.Cruzados_BetweenSubject_Schelling_tratam-200_replic-50_passos-800_process-6_segs-4191_final-2023-01-20-18-49-39.977032.csv
boxplot(happy_pctg~homophily,data=dt)

par(mfrow=c(2,4))

h1<-dt[dt$homophily==1,]
h2<-dt[dt$homophily==2,]
h3<-dt[dt$homophily==3,]
h4<-dt[dt$homophily==4,]
h5<-dt[dt$homophily==5,]
h6<-dt[dt$homophily==6,]
h7<-dt[dt$homophily==7,]
h8<-dt[dt$homophily==8,]

hist(h1$happy_pctg,)
hist(h2$happy_pctg,)
hist(h3$happy_pctg,)
hist(h4$happy_pctg,)
hist(h5$happy_pctg,)
hist(h6$happy_pctg,)
hist(h7$happy_pctg,)
hist(h8$happy_pctg,)






