require(dplyr)
setwd("C:/Users/dcla189/OneDrive - The University of Auckland/2023 Sem2/2023.2/355JaamSim/labs/RC1")
RadiologyLabdata = read.table("radiology_lab.dat", sep="\t",
                      col.names=c("Scenario", "Replication", "TimeInSystem"),
                      skip=1)
RadiologyLabdata = na.omit(RadiologyLabdata)
head(RadiologyLabdata)

RadiologyLabdata %>%
  summarise(lower95CI=t.test(TimeInSystem)$conf.int[1], mean=mean(TimeInSystem),
            upper95CI=t.test(TimeInSystem)$conf.int[2])
