
public class UnsortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] x ={3,13,2,98,65};
		int temp = 0;
		for(int i=0;i<x.length;i++) {
			if(temp>x[i])
				continue;
			else
				temp = x[i];
		}
		System.out.println(temp);
		
	}

}
