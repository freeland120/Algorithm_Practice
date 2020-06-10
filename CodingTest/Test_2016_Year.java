package CodingTest;

import java.util.Scanner;

public class Test_2016_Year {

	public String year_2016(int a, int b) {
		
		String day[]= {"Monday","Tuesday","Wednesday","Thursday","Friday","Sathurday","Sunday"};
		int month[]= {31,29,31,30,31,30,31,31,30,31};
		String year[]=new String[366];
		
		String result = "";
		
		int target_day = 0;
		
		
		for(int i=0; i<year.length;i++) {
			year[i] = day[(i+5)%7];
		}
		
		for(int i=0; i<a-1; i++) {
			target_day += month[i];
		}
		
		
		target_day += b-1;
		
		result += year[target_day];
		
		return result;
		
		
		
		
	}
	
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Test_2016_Year c = new Test_2016_Year();
		
		
		int x = input.nextInt();
		int y = input.nextInt();
		
	
		
		System.out.println(c.year_2016(x,y));
		
		
		
	}

}
