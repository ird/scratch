// following to go tour 'go tool tour'

package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func problems(x float64) float64 {
	return math.Floor(math.Sqrt(rand.Float64() * x))
}

func swap(a, b string) (string, string) {
	return b, a
}

func chessboard(size int) (result string) {
	for i:=0; i<size; i++ {
		for j:=0; j<size; j++ {
			if j % 2 == i % 2 {
				result = result + "#"
			} else {
				result = result + " "
			}
		}
		result = result + "\n"
	}
	return
}

func main() {
	rand.Seed(time.Now().Unix())
	fmt.Printf("Now you have %g problems.\n", problems(1000))
	fmt.Println(swap("World", "Hello"))
	fmt.Println(chessboard(8))
}
