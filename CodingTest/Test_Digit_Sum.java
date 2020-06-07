package CodingTest;

import java.util.Scanner;

public class Test_Digit_Sum {

	public int digit_sum(int num) {

		int result = 0;

		while (num > 0) {

			result += num % 10;
			num = num / 10;

		}

		return result;

	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		Test_Digit_Sum c = new Test_Digit_Sum();

		int a = input.nextInt();

		System.out.println(c.digit_sum(a));
		System.out.println(c.digit_sum(123));

	}

}
