
library(tidyverse)
#Set WD

# Read Data
df = read.table("complete_model-patient-event-logger.log", sep="\t",
                     col.names=c("Time", "Scenario", "Replication",
                                 "Patient", "Event", "EventTime"),
                     skip=15, skipNul=TRUE, header=TRUE)


# Check Point 5 - mean wait time
df_test = df %>% filter(Event=="Wards.wait-for-test" | Event=="Wards.perform-test") %>% pivot_wider(names_from=Event, values_from=EventTime)

df_test$`Wards.perform-test` = as.numeric(df_test$`Wards.perform-test`)
df_test$`Wards.wait-for-test` = as.numeric(df_test$`Wards.wait-for-test`)
df_test$WaitTime = df_test$`Wards.perform-test` - df_test$`Wards.wait-for-test`

mean_wait_time = mean(df_test$WaitTime) * 60
print(paste0("The average waiting time for a test is ", as.character(round(mean_wait_time, 2)), " Minutes"))




# Check Point 4 - ward observation time



DoCheck4Replication = function(df, rep_num) {
  df_obs = df %>% filter(Event=="Wards.ward-stay" | Event=="Wards.observation" | Event=="Wards.discharge")# %>% filter(Replication==rep_num)
  df_obs$EventTime = as.numeric(df_obs$EventTime)
  # Create empty df
  df_need_obs = df_obs %>% filter(Patient=="lol")
  
  # For each row
  for (row in 1:length(df_obs[,1])) {
    # If it is new stay
    if (df_obs[row,5]=="Wards.ward-stay") {
      # Add new row for when observation will be needed
      newline = df_obs[row,]
      newline$Event = "NeedObservation"
      newline$EventTime = df_obs[row,6] + 2 #2 hours
      df_need_obs = rbind(df_need_obs, newline)
    }
  }   # This takes a while
  
  
  df_combined = rbind(df_obs, df_need_obs) %>% filter(Event != "Wards.ward-stay")
  # Reorder
  df_ordered <- df_combined[order(df_combined$Patient,df_combined$EventTime),]
  
  obs_wait_times = c()
  
  # For each row
  for (row in 1:length(df_ordered[,1])) {
    # Check if is need obs
    if (df_ordered[row,5]=="NeedObservation") {
      # Calculate time
      pat = df_ordered[row,4]
      # Deal with first row issue
      if (row==1) {
        prev_disch = FALSE
      }
      else {
        prev_disch = (df_ordered[row-1,4] == pat & df_ordered[row-1,5]=="Wards.discharge")
      }
      next_disch = (df_ordered[row+1,4] == pat & df_ordered[row+1,5]=="Wards.discharge")
      # If NOT discharged instead
      if ( prev_disch | next_disch ) {
        # Then got discharged, not observed
      } else {
        # Add their discharge time to list
        obs_wait_time = df_ordered[row+1,6] - df_ordered[row,6]
        obs_wait_times <- append(obs_wait_times, obs_wait_time)
        
      }
    }
  }   # This takes a while
  DoCheck4Replication = obs_wait_times
}

# run function for each replication
times1 = DoCheck4Replication(df, 1)
times2 = DoCheck4Replication(df, 2)
times3 = DoCheck4Replication(df, 3)
times4 = DoCheck4Replication(df, 4)
times5 = DoCheck4Replication(df, 5)
# Combine results
observ_wait_times = times1

# Print results
print(paste0("The average waiting time for an observation is ", as.character(round(quantile(observ_wait_times, prob=0.95), 2)*60), " minutes"))

less15min_perc = ifelse(observ_wait_times<0.25, 1, 0) %>% mean() * 100
less15min_perc

