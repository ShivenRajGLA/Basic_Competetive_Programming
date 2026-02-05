public class TargetSum {
    public static void main(String[] args) {
        int[] arr={1,2,3,5,8,11};
        int k=6;
        for(int i=0;i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]+arr[j]==k){
                    System.out.println("Pair Exists");
                    break;
                }
            }
        }
    }
}

