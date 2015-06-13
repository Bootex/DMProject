setwd("/home/creator/MinorCreator")
data <- read.csv("data.csv", stringsAsFactors = FALSE)
str(data)

data_raw <- data[4:17]
str(data_raw)

model <- rpart(X20.30??.?Î±???À² ~ ., data_raw)
plot(model)
par(xpd = TRUE)
plot(model, compress = TRUE)
text(model, use.n = TRUE)