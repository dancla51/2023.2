require(dplyr)
setwd("H:/EngFiles/ENGSCI355/labs/radiology_lab")
RadiologyLabdata = read.table("radiology_lab.dat", sep="\t",
                      col.names=c("Scenario", "Replication", "TimeInSystem"),
                      skip=1)
RadiologyLabdata = na.omit(RadiologyLabdata)
head(RadiologyLabdata)

RadiologyLabdata %>%
  summarise(lower95CI=t.test(TimeInSystem)$conf.int[1], mean=mean(TimeInSystem),
            upper95CI=t.test(TimeInSystem)$conf.int[2])
