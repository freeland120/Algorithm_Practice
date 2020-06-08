package CodingTest;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Test_String_Desc {

	public String string_desc(String s) {
		String answer = "";

		String str[] = s.split("");
		Arrays.sort(str);
		Collections.reverse(Arrays.asList(str));

		return String.join("", str);
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);

		Test_String_Desc c = new Test_String_Desc();
		System.out.println(c.string_desc("Zbcdefg"));
	}

}
