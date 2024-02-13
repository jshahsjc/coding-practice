package main

import "fmt"

func sumSlices(slices ...[]int) int {
  sum := 0
  for _, slice := range slices {
    for _, num := range slice {
      sum += num
    }
  }
  return sum
}

func main() {
  sum1 := sumSlices([]int{1,2,3}, []int{4,5,6})
  sum2 := sumSlices([]int{7,8,9,10}, []int{11,12,13,14})
  sum := sum1 + sum2
  fmt.Println("sum1: %d",sum1)
  fmt.Println("sum2: %d", sum2)
  fmt.Println("sum: %d", sum)
}
