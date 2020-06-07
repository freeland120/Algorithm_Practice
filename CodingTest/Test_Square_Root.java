package CodingTest;

public class Test_Square_Root {

	public long square_root(int num) {
		Double sqrt = Math.sqrt(num);

		if (sqrt == sqrt.longValue()) {

			return (long) Math.pow(sqrt + 1, 2);
		} else {
			return -1;
		}

	}

	public static void main(String[] args) {

		int x = 121;
		int y = 3;
		int z = 256;

		Test_Square_Root SR = new Test_Square_Root();
		System.out.println(SR.square_root(x));
		System.out.println(SR.square_root(y));
		System.out.println(SR.square_root(z));

	}

}
