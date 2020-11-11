package kata

import (
	"strconv"
)

func CreatePhoneNumber(numbers [10]uint) string {
	var str string

	for index, number := range numbers {
		if index == 0 {
			str += "("
		} else if index == 3 {
			str += ") "
		} else if index == 6 {
			str += "-"
		}
		str += strconv.Itoa(int(number))
	}

	return str
}
