package kata

import "fmt"

func PrinterError(s string) string {
	asciiSlice := []rune(s)
	count := 0
	for _, value := range asciiSlice {
		if value > rune('m') {
			count++
		}
	}
	return fmt.Sprint(count, "/", len(asciiSlice))
}
