public class q1{
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5,6};
        int time=0;
        int max=arr[0];
        for(int i=0;i<arr.length;i++){
            if(arr[i]>max){
                max=arr[i];
            }
        }    
            for(int i=0;i<arr.length;i++){
                time+=max-arr[i];
        }
        System.out.println(time);
        System.out.println("Hello");
    }
}
