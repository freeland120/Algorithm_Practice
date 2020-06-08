package CodingTest;

import java.util.Scanner;

public class Test_Count_P_Y {

	
	public boolean count_PY(String str) {
		
		boolean result =true;
		int pcount=0;
		int ycount=0;
		
		char as[] = str.toCharArray();
		
		for(int i=0; i<as.length;i++) {
			if(as[i]=='p' || as[i]=='P') {
				pcount++;
			}else if(as[i]=='y'||as[i]=='Y') {
				ycount++;
			}
		}
		
		if(pcount == ycount) {
			return true;
		}else {
			return false;
		}
		
		
	
	}
	
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Test_Count_P_Y c = new Test_Count_P_Y();

		
		String str1 = input.nextLine();
		
		System.out.println(c.count_PY(str1));
		
		
	}

}
