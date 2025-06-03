public class RangeOfnumber{
	public static int[] numberRanges(int[] numbers){
	int smallest = numbers[0];
	int largest = numbers[0];
		for(int count=0;count<numbers.length; count++){
			if(numbers[count] < smallest){
				smallest = numbers[count];
			}
			if(numbers[count] > largest){
				largest = numbers[count];
			}
			
		}
		int[] range = {largest - smallest};
		return range;

	}    


}