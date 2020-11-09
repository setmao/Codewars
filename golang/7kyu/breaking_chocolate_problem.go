package kata

func BreakChocolate(n, m int) int {

	if n*m == 0 {
		return 0
	}

	if n > m {
		return (n - 1) + (m-1)*n
	}

	return (m - 1) + (n-1)*m
}
