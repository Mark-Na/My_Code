
public class Factorial {
	public static int fact(int n) {
		if(n==1)
			return n;
		else
			return n*fact(n-1);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(fact(7));
	}

}
