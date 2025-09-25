# if.test.r
iftest <- function(x) { # if-else test
  if (x %% 2 == 0) {
    cat("x는 짝수입니다\n")
  } else if (x %% 2 == 1) {
    cat("x는 홀수입니다\n")
  } else { 
    cat("x는 자연수가 아닙니다\n")
  } # end if
} # end function

# pp.81 (for r)
sum1 <- 0
for (x in 1:10) {
  sum1 <- sum1 + x^2
}
print(sum1)

# whiletest1.r (pp.83)
x <- 1
sum <- 0
while (x <= 10) {
  sum <- sum + x^2
  x <- x + 1
}
print(sum)

# pp. 85

x <- 1:5
for (j in x) {
  if (j == 3) next
  cat(j, " ")
}

x <- 1:5
for (j in x) {
  if (j == 3) break
  cat(j, " ")
}

# function_test1.r (pp. 88)

my_sums <- function(a=0, b=10) { #default 값이 a=0, b=10
  data <- a:b
  sum1 <- 0; sum2 <- 0
  for (i in data) { 
    sum1 = sum1 + i
    sum2 = sum2 + i^2
  } # end for-loop
  # sum1 <- sum(a:b); sum2 <- sum((a:b)^2)
  list(sum1=sum1, sum2 = sum2, n=length(data))
} # end of function


a <- my_sums(1,10)
mm <- a$sum1 /a$n # a$sum1 -> a변수에 있는 sum1을 불러오는것, a$n -> a의 수수
vv <- (a$sum2 -a$n* mm^2)/(a$n-1)

