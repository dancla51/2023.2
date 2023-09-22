require(dplyr)

nullStrings = c("this.SimTime/1[h]",  "this.obj",
                "[Simulation].ReplicationNumber", "this.obj.TotalTime / 1[h]")

RC2data = read.table("RC2-PatientLogger.log", sep="\t",
                      col.names=c("SimTime", "Object",
                      "Replication", "TimeInSystem", "Priority"),
                      skip=13, na.strings=nullStrings, skipNul=TRUE)

RC2data = na.omit(RC2data)
RC2data$TimeInSystem = as.numeric(RC2data$TimeInSystem)


TIS90 = RC2data %>%
          group_by(Priority, Replication) %>%
          summarise(TimeInSystem_90=quantile(TimeInSystem, probs=0.9))

TIS90 %>% summarise(lower95CI=t.test(TimeInSystem_90)$conf.int[1],
                    mean=mean(TimeInSystem_90),
                    upper95CI=t.test(TimeInSystem_90)$conf.int[2])
