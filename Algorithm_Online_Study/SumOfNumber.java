package Algorithm_Online_Study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class SumOfNumber {
	
	static int Sum_of_Numbers(long number) {
		
		long sum = 0;
		int addNumber = 0;
		
		while(number>=sum) {
			sum+=(++addNumber);
		}
		
		return sum== number ? addNumber:addNumber-1;
		
	}
	
	

	public static void main(String[] args) throws IOException{
		
		BufferedReader BR = new BufferedReader(new InputStreamReader(System.in));
		
		long number = Long.parseLong(BR.readLine());
		System.out.println(Sum_of_Numbers(number));
		
		
		
	}

}
