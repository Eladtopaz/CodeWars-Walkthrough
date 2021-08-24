using System;
public class DirReduction {
  
    public static string[] Remove(string[] arr, int index){
      string[] new_arr = new string[arr.Length - 2];
      int j = 0;
      for(int i = 0; i < arr.Length; i++){
        if(i != index && i != index + 1){
          new_arr[j] = arr[i];
          j++;
        }
      }
      return new_arr;
    }
    public static string[] dirReduc(string[] arr) {
        int i = 0;
        while(i < arr.Length){

            if(i != arr.Length - 1){
                if(arr[i].Equals("NORTH") && arr[i + 1].Equals("SOUTH")){
                    arr = Remove(arr, i);
                    i = 0;
                }
                else if(arr[i].Equals("SOUTH") && arr[i + 1].Equals("NORTH")){
                    arr = Remove(arr, i);
                    i = 0;
                }
                else if(arr[i].Equals("EAST") && arr[i + 1].Equals("WEST")){
                    arr = Remove(arr, i);
                    i = 0;
                }
                else if(arr[i].Equals("WEST") && arr[i + 1].Equals("EAST")){
                    arr = Remove(arr, i);
                    i = 0;
                }
                else{
                    i += 1;
                }
            }
            else{
                return arr;
            }
        }
        return arr;
    }
}
