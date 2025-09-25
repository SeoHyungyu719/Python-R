# p. 106 
## birthyear.r
birthyear <- function() {
  age <- readline(prompt="Enter age: ")
  curyear <- as.numeric( format(Sys.Date(), "%Y") )
  b.year <- curyear-as.numeric(age)
  list(born.year=b.year)
}

# p.110

myiris <- read.table("D:\\대학\\2학년 2학기\\데이터분석\\python_R\\rpy\\chap5_data\\iris.txt", header=T)
#myiris <- read.table("K:/HWP/books/PR4DS/iris.txt", header=T)
#myiris <- read.table(file.choose(), header=T)
#myiris <- read.table(url("http://jupiter.hallym.ac.kr/ftpdata/data/iris.txt"), 
                     skip=9, 
                     col.names=c("No", "SepalLength"," SepalWidth","PetalLength","PetalWidth","Species"))

#myiris <- read.table("http://jupiter.hallym.ac.kr/ftpdata/data/iris.txt", 
                     skip=9, 
                     col.names=c("No", "SepalLength"," SepalWidth","PetalLength","PetalWidth","Species"))

head(myiris) #위에서부터 6개로
tail(myiris) #아래에서부터 6개로

# p. 116
# write.table in r

write.table(mtcars, "")
write.table(mtcars, "", row.names=F, quote=F)
write.table(mtcars, "D:/대학/2학년 2학기/데이터분석/실습코드_서현규/mtars_L6.csv", row.names=T, quote=F, sep=",",
            fileEncoding="UTF-8")

write.table(mtcars, file.choose(), quote=F, sep=",")

# p. 121
#install.packages('readxl')
library(readxl)

getwd() #현재 위치 확인
setwd("D:/대학/2학년 2학기/데이터분석/실습코드_서현규") #기본위치 설정
