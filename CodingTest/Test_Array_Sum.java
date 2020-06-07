package CodingTest;

public class Test_Array_Sum {
	int[][] sumMatrix(int[][] A, int[][] B) {
		int[][] result = new int[A.length][A[0].length];

		for (int i = 0; i < A.length; i++) {
			for (int q = 0; q < A[i].length; q++) {
				result[i][q] = A[i][q] + B[i][q];
			}
		}

		return result;
	}

	
	public static void main(String[] args) {
		Test_Array_Sum c = new Test_Array_Sum();
		int[][] A = { { 1, 2 }, { 2, 3 } };
		int[][] B = { { 3, 4 }, { 5, 6 } };
		int[][] answer = c.sumMatrix(A, B);

		if (answer[0][0] == A[0][0] + B[0][0] && answer[0][1] == A[0][1] + B[0][1] && answer[1][0] == A[1][0] + B[1][0]
				&& answer[1][1] == A[1][1] + B[1][1]) {
			System.out.println("맞았습니다.");
		} else {
			System.out.println("틀렸습니다.");
		}
	}
}