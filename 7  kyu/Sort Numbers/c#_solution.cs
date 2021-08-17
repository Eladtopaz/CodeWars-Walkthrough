public class Kata
{
  public static int[] SortNumbers(int[] nums)
  {
    if(nums == null || nums.Length == 0)
    {
        return new int[] {};
    }
    
    int[] new_arr = new int[nums.Length];
    
    for(int i = 0; i < new_arr.Length; i++)
    {
      int min = 100000000;
      int imin = -1;
      for(int j = 0;j < nums.Length; j++)
      {
        if(nums[j] < min)
        {
          min = nums[j];
          imin = j;
        }
      }
      new_arr[i] = min;
      nums[imin] = 100000000;
    }
    return new_arr;
  }
}
