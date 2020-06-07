package CodingTest;

import java.util.Scanner;

public class Test_String_To_Integer {

	public int strToInt(String str) {

		int result = Integer.parseInt(str); // Integer.parseInt()로 String을 int로 변환할 수 있다. but 문자열 안에 문자가 껴있으면 에러가 발생!

		return result;
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_String_To_Integer c = new Test_String_To_Integer();

		String str1 = input.nextLine();

		System.out.println(c.strToInt(str1));

	}

}
