
class Arithmetic {
    public int add(int x, int y){
        int sum = x+y;
        return sum;
    }
}

class Adder extends Arithmetic {
    public int callAdd(int x, int y){
        return add(x, y);
    }

}

class Solution{
    public static void main(String[] args){
        // create new adder object 
        Adder a = new Adder();

        // print name of the superclass on a new line
        System.out.println("My superclass is: " + a.getClass().getSuperclass().getName());

        // print the result of 3 calls to Adder's "add(int,int)"
        // method as 3 space-separated integers:

        System.out.print(a.add(10,32) + " " + a.add(10,3) + " " + a.add(10, 10) + "\n");
    }
}
