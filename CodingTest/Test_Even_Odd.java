package CodingTest;

import java.util.Scanner;

public class Test_Even_Odd {

	public String Even_Odd(int num) {

		String result = "";
		int check = num % 2;

		if (check == 0) {
			result = "Even";
		} else {
			result = "Odd";
		}
		return result;

	}

	public static void main(String[] args) {

	}

}
