package CodingTest;

import java.util.Scanner;

public class Test_Marathoner {

	public String marathoner(String[] participant, String[] completion) {

		String result = "";

		for (int i = 0; i < participant.length; i++) {

			boolean flag = true;

			for (int j = 0; j < completion.length; j++) {
				if (participant[i].equals(completion[j])) {
					flag = false;
					break;
				}

			}

			if (flag) {
				result += participant[i];
			}

		}

		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_Marathoner c = new Test_Marathoner();

		String str1_p[] = { "leo", "kiki", "eden" };
		String str1_c[] = { "eden", "kiki" };

		String str2_p[] = { "marina", "josipa", "nikola", "vinko", "filipa" };
		String str2_c[]= {"josipa","filipa","marina","nikola"};
		
		System.out.println(c.marathoner(str1_p, str1_c));
		System.out.println(c.marathoner(str2_p, str2_c));

	}

}
