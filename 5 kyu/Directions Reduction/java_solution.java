public class DirReduction {
  
    public static String[] remove(String[] arr, int index){
      String[] new_arr = new String[arr.length - 2];
      int j = 0;
      for(int i = 0; i < arr.length; i++){
        if(i != index && i != index + 1){
          new_arr[j] = arr[i];
          j++;
        }
      }
      return new_arr;
    }
    public static String[] dirReduc(String[] arr) {
      
        int i = 0;
        while(i < arr.length){

            if(i != arr.length - 1){
                if(arr[i].equals("NORTH") && arr[i + 1].equals("SOUTH")){
                    arr = remove(arr, i);
                    i = 0;
                }
                else if(arr[i].equals("SOUTH") && arr[i + 1].equals("NORTH")){
                    arr = remove(arr, i);
                    i = 0;
                }
                else if(arr[i].equals("EAST") && arr[i + 1].equals("WEST")){
                    arr = remove(arr, i);
                    i = 0;
                }
                else if(arr[i].equals("WEST") && arr[i + 1].equals("EAST")){
                    arr = remove(arr, i);
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
