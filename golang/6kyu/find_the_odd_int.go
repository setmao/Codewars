package kata

func FindOdd(seq []int) int {
	var numbers []int
	for _, value := range seq {
		var found = false
		for index, number := range numbers {
			if value == number {
				found = true
				numbers = append(numbers[:index], numbers[index+1:]...)
			}
		}
		if !found {
			numbers = append(numbers, value)
		}
	}

	return numbers[0]
}
