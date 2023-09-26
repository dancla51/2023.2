require(dplyr)
library(stringr)
setwd("H:\\EngFiles\\ENGSCI355\\labs\\RC3")

nullStrings = c("this.SimTime/1[h]", "Scenario", "Replication",  "this.obj",
                "Event", "EventTime")

RC3data = read.table("RC3-PatientEventLogger.log", sep="\t",
                      col.names=c("LeaveTime", "Scenario", "Replication",
                      "Object", "Event", "EventTime"),
                      skip=15, na.strings=nullStrings, skipNul=TRUE)

RC3data = na.omit(RC3data)
RC3data$Batch = ceiling(RC3data$LeaveTime / (24 * 7))
scenario_indices = str_split_fixed(RC3data$Scenario, '-', 2)
RC3data$CTMachineScenario = scenario_indices[,1]
RC3data$ReceptionistScenario = scenario_indices[,2]

checkInWaits = RC3data %>% filter(Event == "WaitForCheckIn")
checkInWaits$CheckInWaitTime = (RC3data %>% filter(Event == "CheckIn") %>% select(EventTime))$EventTime - checkInWaits$EventTime

CheckInWait90 = checkInWaits %>%
          group_by(CTMachineScenario, ReceptionistScenario, Batch) %>%
          summarise(CheckInWait_90=quantile(CheckInWaitTime, probs=0.9))



scanWaits = RC3data %>% filter(Event == "WaitForScan")
scanWaits$ScanWaitTime = (RC3data %>% filter(Event == "Scan") %>% select(EventTime))$EventTime - scanWaits$EventTime

ScanWait90 = scanWaits %>%
  group_by(CTMachineScenario, ReceptionistScenario, Batch) %>%
  summarise(ScanWait_90=quantile(ScanWaitTime, probs=0.9))

CheckInWait90$ScanWait_90 = ScanWait90$ScanWait_90

CheckInWait90 %>% 
  group_by(CTMachineScenario, ReceptionistScenario) %>%
  summarise(CheckInWait=mean(CheckInWait_90),
            ScanWait=mean(ScanWait_90))
