package kata

import (
	"strings"
	"unicode"
)

func solve(str string) string {

	lowerCount := 0
	upperCount := 0

	for _, char := range str {
		if unicode.IsLower(char) {
			lowerCount++
		} else {
			upperCount++
		}
	}

	if lowerCount >= upperCount {
		return strings.ToLower(str)
	}
	return strings.ToUpper(str)

}
