package CodingTest;

import java.util.Scanner;

public class Test_Aliquot_Sum {

	public int aliquot_sum(int num) {

		int sum = 0;

		for (int i = 1; i <= num; i++) {
			if (num % i == 0) {
				sum += i;
			}
		}

		return sum;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Test_Aliquot_Sum c = new Test_Aliquot_Sum();

		System.out.println(c.aliquot_sum(12));
		System.out.println(c.aliquot_sum(5));

		int a = input.nextInt();
		System.out.println(c.aliquot_sum(a));

	}

}
