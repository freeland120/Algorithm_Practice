package CodingTest;

import java.util.Scanner;

public class Test_Integer_Sum {

	public int integer_sum(int num1, int num2) {

		int result = 0;

		if (num1 < num2) {
			for (int i = num1; i <= num2; i++) {
				result += i;
			}
		} else {
			for (int j = num2; j <= num1; j++) {
				result += j;
			}
		}
		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_Integer_Sum c = new Test_Integer_Sum();

		int a = input.nextInt();
		int b = input.nextInt();

		System.out.println(c.integer_sum(a, b));

		System.out.println(c.integer_sum(10, 20));

	}

}
