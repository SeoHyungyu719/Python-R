xv <- c(1,10,20,50,100)
is.vector(xv)
xv[2]
x<-c(1,2,'a',TRUE)
is.character(x[2])
xx<-c(1,2,TRUE)
length(xv) #벡터의 길이를 반환하는 메서드

#################################################
#R에서 matrix 함수로 만들수 있다.

xm <- matrix(1:9, nrow=3, byrow=F,
             dimnames=list(c('r1', 'r2', 'r3'), c('col1','col2', 'col3')))
###################################################

x <- seq(1,10,by=2)
y <- letters[1:length(x)]
df <-data.frame(id=x, name=y)
df
df[1,] # 1행 출력
df[1,2] # 1행 2열 출력

########################################

xv <- seq(1,10,by=2)
xv <-c(xv,11)

xv[-3]# 3번째 원소 삭제
xv[-c(1,3,4)] # xv의 1,3,4 번째 원소 삭제

xm <-matrix(1:8, nrow = 2, byrow = T)
xm

y1 <- c(9:12)
xm2 <- rbind(xm, y1) # xm행렬 다음에 y1 행렬을 추가
xm2

rbind(xm3[1,],13:17,xm3[2:3,]) # 행렬 중간에 추가 하고 싶을 때 
########################################

xv1 <- seq(1:10)
ones <- seq(1:10)
xv1 + ones
onetwo <- c(1,2) #열마다 끊어서 더한다.
xv1 + onetwo

mx1 <-matrix(1:6, ncol=3,byrow=T)
mx2 <-cbind(rep(1,3),rep(2,3))
mx1 %*% mx2
mx2
mx1
