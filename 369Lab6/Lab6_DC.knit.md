---
title: 'Lab 6'
subtitle: "STATS 369"
author: "Daniel Clark"
output:
  html_document:
    highlight: pygments
    theme: readable
    toc: true
    toc_depth: 2
    toc_float: true
---



```r
# Load libraries
library(tidyverse)
```

```
## Warning: package 'tidyverse' was built under R version 4.1.3
```

```
## Warning: package 'ggplot2' was built under R version 4.1.3
```

```
## Warning: package 'tibble' was built under R version 4.1.3
```

```
## Warning: package 'tidyr' was built under R version 4.1.3
```

```
## Warning: package 'readr' was built under R version 4.1.3
```

```
## Warning: package 'purrr' was built under R version 4.1.3
```

```
## Warning: package 'dplyr' was built under R version 4.1.3
```

```
## Warning: package 'stringr' was built under R version 4.1.3
```

```
## Warning: package 'forcats' was built under R version 4.1.3
```

```
## Warning: package 'lubridate' was built under R version 4.1.3
```

```r
library(rpart)
library(ggplot2)
```

# Task 1

*A*


```r
set.seed(502)
```

*B*


```r
train.df <- suppressMessages(read_table('adult.data', col_names=F))
test.df <- suppressMessages(read_table('adult.test', col_names=F))

names.vt <- c('age', 'workclass', 'fnlwgt', 'education',
              'education_num', 'marital_status', 'occupation',
              'relationship', 'race', 'sex', 'capital_gain',
              'capital_loss', 'hours_per_week', 'native_country',
              'response')

names(train.df) = names(test.df) = names.vt
```

*C*


```r
train_h = table(train.df$response)
test_h = table(test.df$response)

hist_df = data.frame(Response=c("<=50k",">50k","<=50k",">50k"), DataSort=c("Train","Train","Test","Test"), Frequency=c(train_h[1],train_h[2],test_h[1],test_h[2]))
rownames(hist_df) <- 1:nrow(hist_df)
print(hist_df)
```

```
##   Response DataSort Frequency
## 1    <=50k    Train     24720
## 2     >50k    Train      7841
## 3    <=50k     Test     12435
## 4     >50k     Test      3846
```

*D*


```r
train.df = train.df %>% mutate(response = ifelse(response=="<=50K", 0, 1))
test.df = test.df %>% mutate(response = ifelse(response=="<=50K.", 0, 1))
```

*E*

My prediction for the relevant variables are: Capital Gain, Native Country and Education.
I believe capital gain is relevant as it tends to be the most wealthy people who are able to achieve capital gains.
I believe native country is relevant because if someone was born in the united states they are likely to have had 
a more financially stable life than someone who had to immigrate to a new country.
I believe education is relevant because people who studied for longer would be likely to achieve a higher-paying 
job than someone with less education.


# Task 2

*A*


```r
#summary(train.df)
# function to fix
fix_data_types = function(df) {
  df = df %>% mutate(capital_gain=as.numeric(gsub(',','',capital_gain)))
  df = df %>% mutate(capital_loss=as.numeric(gsub(',','',capital_loss)))
  df = df %>% mutate(workclass = factor(gsub(',','',workclass)))
  df = df %>% mutate(education = factor(gsub(',','',education)))
  df = df %>% mutate(marital_status = factor(gsub(',','',marital_status)))
  df = df %>% mutate(occupation = factor(gsub(',','',occupation)))
  df = df %>% mutate(relationship = factor(gsub(',','',relationship)))
  df = df %>% mutate(race = factor(gsub(',','',race)))
  df = df %>% mutate(sex = factor(gsub(',','',sex)))
  df = df %>% mutate(native_country = factor(gsub(',','',native_country)))
  df = df %>% mutate(response = factor(response))
  return(df)
}

train.df = fix_data_types(train.df)
test.df = fix_data_types(test.df)

tree = rpart(response~., data=train.df, method="class")
tree
```

```
## n= 32561 
## 
## node), split, n, loss, yval, (yprob)
##       * denotes terminal node
## 
##  1) root 32561 7841 0 (0.75919044 0.24080956)  
##    2) relationship=Not-in-family,Other-relative,Own-child,Unmarried 17800 1178 0 (0.93382022 0.06617978)  
##      4) capital_gain< 7073.5 17482  872 0 (0.95012012 0.04987988) *
##      5) capital_gain>=7073.5 318   12 1 (0.03773585 0.96226415) *
##    3) relationship=Husband,Wife 14761 6663 0 (0.54860782 0.45139218)  
##      6) education=10th,11th,12th,1st-4th,5th-6th,7th-8th,9th,Assoc-acdm,Assoc-voc,HS-grad,Preschool,Some-college 10329 3456 0 (0.66540807 0.33459193)  
##       12) capital_gain< 5095.5 9807 2944 0 (0.69980626 0.30019374) *
##       13) capital_gain>=5095.5 522   10 1 (0.01915709 0.98084291) *
##      7) education=Bachelors,Doctorate,Masters,Prof-school 4432 1225 1 (0.27639892 0.72360108) *
```

*B*


```r
pred = predict(tree, test.df, type="class")
pred = as.data.frame(pred)
confusion_df = data.frame(pred$pred, test.df$response)
confusion_df$HighPHigh = confusion_df$pred.pred==1 & confusion_df$test.df.response==1
confusion_df$HighPLow = confusion_df$pred.pred==0 & confusion_df$test.df.response==1
confusion_df$LowPHigh = confusion_df$pred.pred==1 & confusion_df$test.df.response==0
confusion_df$LowPLow = confusion_df$pred.pred==0 & confusion_df$test.df.response==0

confusion_matrix = matrix(c(sum(confusion_df$HighPHigh), sum(confusion_df$HighPLow), sum(confusion_df$LowPHigh), sum(confusion_df$LowPLow)), nrow=2)
rownames(confusion_matrix) <- c("Prediction Above 50k", "Prediction Below 50k")
colnames(confusion_matrix) <- c("Actually Above 50k", "Actually Below 50k")

print(confusion_matrix)
```

```
##                      Actually Above 50k Actually Below 50k
## Prediction Above 50k               1945                630
## Prediction Below 50k               1901              11805
```

# Task 3

*A*

There will be more predictions as above 50k, and less as below 50k. This is because misclassifying someone as below 50k is five time worse than misclassifying as above it. We will include some penalty to try and minimise the bottom left corner of the above prediction matrix, and by doing so will shift some error into the top right square of the matrix too (because we will classify less as under 50k to try and avoid this particular misclassification).


*B*


```r
tree2 = rpart(response~., data=train.df, method="class", parms = list(loss=matrix(c(0,1,5,0), byrow=T, nrow=2)))

# Another confusion matrix
pred = predict(tree2, test.df, type="class")
pred = as.data.frame(pred)
confusion_df = data.frame(pred$pred, test.df$response)
confusion_df$HighPHigh = confusion_df$pred.pred==1 & confusion_df$test.df.response==1
confusion_df$HighPLow = confusion_df$pred.pred==0 & confusion_df$test.df.response==1
confusion_df$LowPHigh = confusion_df$pred.pred==1 & confusion_df$test.df.response==0
confusion_df$LowPLow = confusion_df$pred.pred==0 & confusion_df$test.df.response==0

confusion_matrix = matrix(c(sum(confusion_df$HighPHigh), sum(confusion_df$HighPLow), sum(confusion_df$LowPHigh), sum(confusion_df$LowPLow)), nrow=2)
rownames(confusion_matrix) <- c("Prediction Above 50k", "Prediction Below 50k")
colnames(confusion_matrix) <- c("Actually Above 50k", "Actually Below 50k")

print(confusion_matrix)
```

```
##                      Actually Above 50k Actually Below 50k
## Prediction Above 50k               3443               4057
## Prediction Below 50k                403               8378
```

# Task 4

The loss matrix applied in task 3 penalises the misclassifications in an appropriate way to minimise the worse form of misclassification. Because of this, that outcome has been reduced from 1901 occasions, to only 403 occasions. Along with this, as I predicted, the number of misclassifications in the other directions has increased, going from 630, 4057.



