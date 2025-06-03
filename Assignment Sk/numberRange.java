public class numberRange{
	public static void main(String[] args){
	int[] numbers = {7,3,2,2,6};

		int largest = numbers [0];
		int smallest = numbers [0];
		int range = 0;
		for(int count = 0; count<numbers.length; count++){
			if(numbers[count] > largest)
			largest = numbers[count];

				if(numbers[count] < smallest)
				 smallest = numbers[count];	
                                range = largest - smallest;
				}

				System.out.printf("The range of %d%n:", range);

	
	





	}


}