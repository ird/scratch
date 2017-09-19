// following to go tour 'go tools tour'

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

func main() {
	rand.Seed(time.Now().Unix())
	fmt.Printf("Now you have %g problems.", problems(1000))
}
