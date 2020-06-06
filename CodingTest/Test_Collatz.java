package CodingTest;

public class Test_Collatz {

	public int collatz(int num) {

		long check = (long) num;

		for (int i = 0; i < 500; i++) {
			if (check == 1) {
				return i;
			}
			check = (check % 2 == 0) ? check / 2 : check * 3 + 1;
		}
		return -1;
	}

	public static void main(String[] args) {

		Test_Collatz c = new Test_Collatz();
		int x = 6;
		int y = 626331;
		int z = 81;
		System.out.println(c.collatz(x));
		System.out.println(c.collatz(y));
		System.out.println(c.collatz(z));
	}

}
