package CodingTest;

import java.util.Scanner;

public class Test_WaterMelon {

	public String watermelon(int num) {

		String result = "";

		for (int i = 1; i <= num; i++) {

			if (i % 2 == 1) {
				result += "¼ö";
			} else if (i % 2 == 0) {
				result += "¹Ú";
			}

		}

		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_WaterMelon c = new Test_WaterMelon();

		int x = input.nextInt();
		int y = 27;
		System.out.println(c.watermelon(x));
		System.out.println(c.watermelon(y));

	}

}
