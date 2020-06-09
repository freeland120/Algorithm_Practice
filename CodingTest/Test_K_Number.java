package CodingTest;

import java.util.Arrays;
import java.util.Scanner;

public class Test_K_Number {

	
	public int[] k_number(int[] array, int[][] commands) {
		
		int[] result = new int[commands.length];
		for(int i=0; i<commands.length; i++) {
			int[] tmp=Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
			Arrays.sort(tmp);
			result[i]=tmp[commands[i][2]-1];
		}
		
		
		return result;
		
	}
	
	
	
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		Test_K_Number c = new Test_K_Number();
		
		
		int str1[] = {1,5,2,6,3,7,4};
		
		
		
		int x = input.nextInt();
		int y = input.nextInt();
		int z = input.nextInt();
		
		
		//System.out.println(c.k_number(str1, x));
		
		
	}

}
