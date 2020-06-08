package CodingTest;

import java.util.Scanner;

public class Test_Weird_String {

	public String weird_string(String s) {

		int index = 0;
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == ' ') {
				sb.append(' ');
				index = 0;
			} else {
				if (index % 2 != 0) {
					sb.append(Character.toLowerCase(s.charAt(i)));
					index++;
				} else {
					sb.append(Character.toUpperCase(s.charAt(i)));
					index++;
				}
			}
		}

		return sb.toString();

	}

	public static void main(String[] args) {
		Scanner inupt = new Scanner(System.in);
		Test_Weird_String c = new Test_Weird_String();

		String string1 = "try ydg world!";

		System.out.println(c.weird_string(string1));

	}

}
