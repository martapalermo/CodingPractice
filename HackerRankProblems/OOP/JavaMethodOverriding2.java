// when a method in a subclass overrides a method in superclass, it is still possible to call the overridden method
// using *super*
// if you write super.func() to call the function func(), it will call the method that was defined in the superclass



class BiCycle{
    String define_me(){
        return "a vehicle with pedals";
    }
}

class MotorCycle extends BiCycle{
    String define_me(){
        return "a cycle with an engine.";
    }

    MotorCycle(){
        System.out.println("Hello I am a motorcycle, I am " + define_me());
        String temp = super.define_me();
        System.out.println("My ancestor is a cycle who is " + temp);
    }
}

class Solution{
    public static void main(String [] args){
        MotorCycle motor = new MotorCycle();
    }
}

/*
 * Code should print out: 
 * Hello I am a motorcycle, I am a cycle with an engine.
 * My ancestor is a cycle who is a vehicle with pedals.
 */