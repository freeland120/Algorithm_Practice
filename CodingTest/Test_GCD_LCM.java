package CodingTest;

import java.util.Arrays;
import java.lang.ArithmeticException;

public class Test_GCD_LCM {

	
	public int[] gcd_lcm(int a, int b) {
		int[] result = new int[2];
		
		result[0] = gcd(a,b);
		result[1] = (a*b)/result[0];
		
		return result;
	}
	
	
	public static int gcd(int x, int y) {
		if(y==0) return x;
		return gcd(y, x%y);
	}
	
	
	
	public static void main(String[] args) {
		
		Test_GCD_LCM c = new Test_GCD_LCM();
		
		System.out.println(Arrays.toString(c.gcd_lcm(3,12)));
		

	}

}
