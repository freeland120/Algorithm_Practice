package CodingTest;

import java.util.Scanner;

public class Test_Rectangle_Star {

	
	public int rectangle_star(int row, int column) {
		
		for(int i=0; i<column; i++) {
			for(int j=0; j<row; j++) {
				System.out.print("*");
			}
			
			System.out.println();
		}
		
		return 1;
	}
	
	
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		Test_Rectangle_Star c = new Test_Rectangle_Star();
		
		int x = input.nextInt();
		int y = input.nextInt();
		
		System.out.println(c.rectangle_star(x, y));
		
		
		
		
	}

}
