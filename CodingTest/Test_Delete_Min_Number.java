package CodingTest;

import java.util.Arrays;

public class Test_Delete_Min_Number {

	public int[] del_min_Num(int[] arr) {
		if (arr.length <= 1) {
			int[] result = { -1 };
			return result;

		}

		int Min = arr[0];
		for (int i = 1; i < arr.length; i++) {
			Min = Math.min(Min, arr[i]);
		}

		int[] result = new int[arr.length - 1];
		int index = 0;

		for (int i = 0; i < arr.length; i++) {
			if (arr[i] == Min) {
				continue;
			}

			result[index++] = arr[i];
		}

		return result;
	}

	public static void main(String[] args) {

		Test_Delete_Min_Number c = new Test_Delete_Min_Number();

		
		int[] array = {4,3,2,1};
		int[] array2 = {4,3,2,1,12,1,4,6,667};
		
		System.out.println(Arrays.toString(c.del_min_Num(array)));
		System.out.println(Arrays.toString(c.del_min_Num(array2)));
		
		
	}

}
