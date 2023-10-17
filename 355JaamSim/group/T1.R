require(dplyr)
library(stringr)

nullStrings = c("this.SimTime/1[h]", "Scenario", "Replication",  "this.obj",
                "Event", "EventTime")

Hospitaldata = read.table("complete_model-patient-event-logger.log", sep="\t",
                      col.names=c("LeaveTime", "Scenario", "Replication",
                      "Object", "Event", "EventTime"),
                      skip=15, na.strings=nullStrings, skipNul=TRUE)

Hospitaldata = na.omit(Hospitaldata)
Hospitaldata$Batch = ceiling(Hospitaldata$LeaveTime / (24 * 7))

EDarrival = Hospitaldata %>%
  group_by(Object, Replication) %>%
  summarise(EventTime=min(EventTime)) 

Arrivaldf = Hospitaldata %>% inner_join(EDarrival)
Arrivaldf = Arrivaldf %>%  filter(Event != 'ED.register')

EDleave = Hospitaldata %>%
  group_by(Object, Replication) %>%
  summarise(EventTime=max(EventTime))

Leavedf = Hospitaldata %>% inner_join(EDleave)

Arrivaldf$Totaltime=Arrivaldf$LeaveTime-Arrivaldf$EventTime
T1=Arrivaldf%>%group_by(Replication)%>%summarize(quantile(Totaltime,prob=0.95))
T1$`quantile(Totaltime, prob = 0.95)`
Totaltime_95=quantile(Arrivaldf$Totaltime,prob=0.95)
Totaltime_95



