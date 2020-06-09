package CodingTest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Test_I_Hate_SameNumber {

	public int[] hate_number(int[] arr) {

		ArrayList<Integer> tempArrayList = new ArrayList<Integer>();   //tempArrayList 생성
		int preNumber = 11;    // 첫 preNumber값은 0~9가 아닌 수로!

		for (int n : arr) {
			if (preNumber != n) {	//arr의 값들을 비교
				tempArrayList.add(n);	
			}
			preNumber = n;	//
		}

		int result[] = new int[tempArrayList.size()];
		for (int i = 0; i < result.length; i++) {
			result[i] = tempArrayList.get(i).intValue();
		}

		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_I_Hate_SameNumber c = new Test_I_Hate_SameNumber();

		
		int str1[]= {1,1,3,3,0,1,1};
		int str2[]= {4,4,4,3,3};
		
		System.out.println(Arrays.toString(c.hate_number(str1)));
		System.out.println(Arrays.toString(c.hate_number(str2)));
		
		
	}

}
