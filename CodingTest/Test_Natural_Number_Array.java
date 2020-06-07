package CodingTest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Test_Natural_Number_Array {

	
	public int[] make_array(long num) {
		 int[] result = {};
         ArrayList<Integer> arr = new ArrayList<Integer>();
         long a = 0;
         
         while(num!=0) {
             a = num%10;
             arr.add((int)a);
             num = num/10;
         }
         
         result = new int[arr.size()];
         
         for(int i=0; i<arr.size(); i++) {
             result[i]= arr.get(i);
         }
         
         return result;
	}
	
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Test_Natural_Number_Array c= new Test_Natural_Number_Array();

		int x = input.nextInt();
		int y = 231223;
		
		System.out.println(Arrays.toString(c.make_array(x)));
		System.out.println(Arrays.toString(c.make_array(y)));
		
	}

}
