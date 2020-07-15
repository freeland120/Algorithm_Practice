package Algorithm_Online_Study;

import java.util.Scanner;

public class Group_Words_1316 {

	static Scanner in = new Scanner(System.in);

	public static boolean Group_Words_Check() {
		boolean[] check = new boolean[26];
		int prev = 0;
		String str = in.next();

		for (int i = 0; i < str.length(); i++) {
			int now = str.charAt(i);

			if (prev != now) {
				if (check[now - 'a'] == false) {
					check[now - 'a'] = true;
					prev = now;
				} else {
					return false;
				}
			} else {
				continue;
			}
		}

		return true;
	}

	public static void main(String[] args) {

		int count = 0;
		int N = in.nextInt();
		
		for(int i=0; i<N; i++) {
			if(Group_Words_Check()==true) {
				count++;
			}
		}
		System.out.println(count);
		
	}

}
