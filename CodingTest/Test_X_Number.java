package CodingTest;

import java.util.Arrays;
import java.util.Scanner;

public class Test_X_Number {

	public long[] x_number(long a, int b) {

		long[] array = new long[b];
		for (int i = 0; i < b; i++) {
			array[i] = a * (i + 1);
		}

		return array;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_X_Number c = new Test_X_Number();

		long x = input.nextLong();
		int N = input.nextInt();

		System.out.println(Arrays.toString(c.x_number(x, N)));
	}

}
