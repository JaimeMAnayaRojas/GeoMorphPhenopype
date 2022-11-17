####

# To install pagages do install.packages("name of package")

library(dplyr)

library(ggplot2)

#install.packages("ggpubr")
library(ggpubr)

rm(list=ls(all=TRUE)) # clean R's memory to start fresh

# How can I get the data from phenopype?

result_folder <- "_temp/project_2/data/"

folders <-  list.files(result_folder)

files <- list.files(paste(result_folder, folders[5], sep="/"))
files 


# first collect the reference data set to correct the values from pixels to mm
ref_file <- paste(result_folder, folders[5], "reference_v1.csv",sep='/')
ref1 <- read.csv(ref_file)
ref1


# get the shape_features_v1.csv data set
target_file <- paste(result_folder, folders[5], "shape_features_v1.csv",sep='/')
df1 <- read.csv(target_file)

head(df1)

# keep only the data for the largest area

df1a <- df1 %>% filter(area == max(area)) %>%
  select(image_name,area, circularity, diameter, compactness, min_rect_max, min_rect_min, perimeter_length, rect_height, rect_width)

df1a[,-1] <- df1a[,-1] / ref1$distance
df1a

### How can you do it for all your data?
# hit use the following functions:
# loops
# cbind(dataset1, dataset2)



