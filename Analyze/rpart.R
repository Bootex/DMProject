setwd("~/MinorCreator/DMProject/analyze")
data <- read.csv("InputData/data.csv", stringsAsFactors = FALSE)
str(data)

data<- data[3:9]
str(data)

model <- rpart(X20.30 ~ ., data)

plot(model)
par(xpd = TRUE)
plot(model, compress = TRUE)
text(model, use.n = TRUE)
