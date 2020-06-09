package CodingTest;

import java.util.Scanner;

public class Test_Workout_Clothes {

	public int workout_clothes(int total, int[] lost, int[] reserve) {

		int result = 0;
		int lost1 = 0;
		int count = 0;

		for (int i = 0; i < lost.length; i++) { // 옷 잃어버린 사람과 여유분으로 옷 가져온 사람이 같을 때
			for (int j = 0; j < reserve.length; j++) {
				if (lost[i] == reserve[j]) {

					lost1++;
					lost[i] = -1;
					reserve[j] = -1;
					break;
				}
			}
		}

		for (int i = 0; i < lost.length; i++) { // 옷을 빌려주면 가지고 있는 옷이 없도록 reserve[j]=-1 처리!
			for (int j = 0; j < reserve.length; j++) {
				if (lost[i] == reserve[j] - 1 || lost[i] == reserve[j] + 1) {

					count++;

					reserve[j] = -1;
					break;
				}
			}
		}
		
		
		result += (total-lost.length) + lost1 + count;
		
		

		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_Workout_Clothes c = new Test_Workout_Clothes();

		int x = input.nextInt();
		// int y = input.nextInt();

		int lost_students1[] = { 2, 4 };
		int reserve_students1[] = { 1, 3, 5 };
		
		
		int lost_students2[] = { 2, 4 };
		int reserve_students2[] = {  3 };

		System.out.println(c.workout_clothes(x, lost_students1, reserve_students1));
		System.out.println(c.workout_clothes(x, lost_students2, reserve_students2));

	}

}
