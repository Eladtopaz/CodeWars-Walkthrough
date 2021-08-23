class AreTheySame
{
  public static bool comp(int[] a, int[] b)
  {
    if(a == null || b == null)
    {
      return false;
    }
    if(a.Length != b.Length)
    {
      return false;
    }
    for(int i = 0;i < a.Length; i++)
    {
      int new_number = a[i] * a[i];
      bool ok = false;
      for(int j = 0;j < b.Length;j++)
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
