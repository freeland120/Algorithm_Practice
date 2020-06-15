package CodingTest;

import java.util.Scanner;

public class Test_Caesar_Encryption {

	public String caesar_encrypt(String s, int n) {

		String result = "";
		
		
		int length = s.length();
		char bravo;
		char start;
		for(int i=0; i<length; i++) {
			bravo = s.charAt(i);
			if(bravo != ' ') {
				start = Character.isLowerCase(bravo)? 'a':'A';
				bravo = (char)(start + (bravo+n-start)%26);
			}
			
			result += bravo;
		}
		
		

		return result;

	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		Test_Caesar_Encryption c = new Test_Caesar_Encryption();
		
		String arr1 = "abcde";
		int x = input.nextInt();
		
		
		System.out.println(c.caesar_encrypt(arr1, x));
		
	
		
		

	}

}
