import java.util.Scanner;

// interface in java ccan only contain method signatures + fields
// used to achieve polymorphism 


interface AdvancedArithmetic {
    int divisor_sum(int n);
}


class MyCalculator implements AdvancedArithmetic {
    int sum = 0;
    public int divisor_sum(int n){
        if (n<= 1){
            return n;
        }

        int sum = n+1;  //divisor includes 1 and n so always add 1
        for (int i = 2; i < n; i++){
            if (n% i == 0){
                sum += i;
            }
        }
        return sum;
    }

}

class Solution{
    public static void main(String []args){
        MyCalculator my_calculator = new MyCalculator();
        System.out.print("I implemented: ");
        ImplementedInterfaceNames(my_calculator);
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.print(my_calculator.divisor_sum(n) + "\n");
        sc.close();
    }
    /*
     *  ImplementedInterfaceNames method takes an object and prints the name of the interfaces it implemented
     */
    static void ImplementedInterfaceNames(Object o){
        Class[] theInterfaces = o.getClass().getInterfaces();
        for (int i = 0; i < theInterfaces.length; i++){
            String interfaceName = theInterfaces[i].getName();
            System.out.println(interfaceName);
        }
    }
}