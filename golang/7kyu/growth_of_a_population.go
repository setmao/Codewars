package kata

func NbYear(p0 int, percent float64, aug int, p int) int {
	var count = 0

	for p0 < p {
		count++
		p0 = p0 + int(float64(p0)*percent/100) + aug
	}
	return count
}
