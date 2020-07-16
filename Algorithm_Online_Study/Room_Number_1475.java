package Algorithm_Online_Study;

import java.util.Scanner;

public class Room_Number_1475 {

	static int arr[] = new int[10];
	static int count = 0;

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		String N = input.nextLine();
		int number[] = new int[N.length()];

		for (int i = 0; i < N.length(); i++) {
			number[i] = N.charAt(i) - '0';
		}

		for (int i = 0; i < N.length(); i++) {

			if (arr[number[i]] == 0) {
				if (number[i] == 6 && arr[9] != 0) {
					arr[9] -= 1;
					continue;
				} else if (number[i] == 9 && arr[6] != 0) {
					arr[6] -= 1;
					continue;
				} else {
					for (int j = 0; j < 10; j++) {
						arr[j] += 1;
					}
					count++;
					arr[number[i]] -= 1;
				}
			}

			
		}
		System.out.println(count+"세트가 필요합니다.");
		input.close();
	}

}
