package CodingTest;

import java.util.Arrays;
import java.util.Scanner;

public class Test_Interger_Desc {

	public long int_decs(long num) {
		long answer = 0;
        
        String a = "" + num;
        String[] a1 = new String[a.length()+1];
        a1 = a.split("");
        Arrays.sort(a1);
        
        for(int i=0; i<a1.length; i++) {
            answer += Integer.parseInt(a1[i]) * Math.pow(10, i);
        }
        
        return answer;
	}
	
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Test_Interger_Desc c = new Test_Interger_Desc();
		
		
		int x = input.nextInt();
		int y = 231223;
		System.out.println(c.int_decs(x));
		System.out.println(c.int_decs(y));
	}

}
