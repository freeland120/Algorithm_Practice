package CodingTest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Test_Sort_String {

	public String[] sort_string(String[] strings, int num) {
		
		int th = num;
	      
        for(int i = 0 ; i < strings.length; i++) {
            strings[i] = strings[i].charAt(num) + strings[i];
        }
        Arrays.sort(strings);
        String[] ans = new String[strings.length];
        for(int i = 0 ; i < strings.length; i++) {
            ans[i] = strings[i].substring(1,strings[i].length());
        }
      return ans;
	}
	
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		Test_Sort_String c = new Test_Sort_String();
		
		ArrayList<Integer> arrayList = new ArrayList<>();
		
		String str1[]= {"sun","bed","car"};
		String str2[]= {"abce","abcd","cdx"};
		
		
		int x = input.nextInt();
		
		System.out.println(str1[0]);
		
		System.out.println(Arrays.toString(c.sort_string(str1,x)));
		
		
	}

}
