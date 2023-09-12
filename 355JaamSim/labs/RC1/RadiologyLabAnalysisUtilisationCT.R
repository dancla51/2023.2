# Same but for utilisation

require(dplyr)
setwd("C:/Users/dcla189/OneDrive - The University of Auckland/2023 Sem2/2023.2/355JaamSim/labs/RC1")
RadiologyLabdata = (3 - read.table("radiology_lab_util.dat", sep="\t",
                      col.names=c("Scenario", "Replication", "Utilisation"),
                      skip=1) )/ 3
RadiologyLabdata = na.omit(RadiologyLabdata)
head(RadiologyLabdata)

RadiologyLabdata %>%
  summarise(lower95CI=t.test(Utilisation)$conf.int[1], mean=mean(Utilisation),
            upper95CI=t.test(Utilisation)$conf.int[2]) %>% round(3)

