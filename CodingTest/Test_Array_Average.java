package CodingTest;

import java.util.Scanner;

public class Test_Array_Average {

	public double array_average(int arr[]) {

		double answer = 0;
		double result = 0;

		for (int i = 0; i < arr.length; i++) {

			result += arr[i];

		}

		result = (double) result / arr.length;

		return result;

	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		Test_Array_Average c = new Test_Array_Average();

		int x[] = { 1, 2, 3, 4 };
		int y[] = { 5, 5 };
		int z[] = { 23, 21, 64, 23, 19, 10 };

		System.out.println(c.array_average(x));
		System.out.println(c.array_average(y));
		System.out.println(c.array_average(z));

	}

}
