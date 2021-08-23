public class AreSame {
	
	public static boolean comp(int[] a, int[] b) {
    
    if(a == null || b == null)
    {
      return false;
    }
    if(a.length != b.length)
    {
      return false;
    }
    for(int i = 0;i < a.length; i++)
    {
      int new_number = a[i] * a[i];
      boolean ok = false;
      for(int j = 0;j < b.length;j++)
      {
        if(b[j] == new_number)
        {
          ok = true;
          b[j] = -1;
          break;
        }
      }
      if(!ok)
      {

        return false;
      }
    }
    return true;
  }
}
