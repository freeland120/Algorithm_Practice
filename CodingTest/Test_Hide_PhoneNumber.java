package CodingTest;

import java.util.Scanner;

public class Test_Hide_PhoneNumber {

	public String hide_phonenumber(String number) {

		String result = "";
		String[] array = number.split("");

		for (int i = 0; i < array.length - 4; i++) {
			array[i] = "*";
		}

		for (int j = 0; j < array.length; j++) {
			result += array[j];
		}

		return result;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		Test_Hide_PhoneNumber c = new Test_Hide_PhoneNumber();

		String number1 = input.nextLine();
		System.out.println(c.hide_phonenumber(number1));
		System.out.println(c.hide_phonenumber("01011112222"));

	}

}
