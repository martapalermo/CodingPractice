import java.util.Scanner;

// abstract class in java is a class that can't be instantiated 
// aka - cannot create new instances of an abstract class 
// base for subclasses 

abstract class Book {
    String title;
    abstract void setTitle(String s);
    String getTitle(){
        return title;
    }
}

class MyBook extends Book {

    @Override
    void setTitle(String s) {
        this.title = s;
    }
    
}

public class JavaAbstractClass{
    public static void main(String[] args){
        // Book new_novel = new Book();
        // ^ line will throw error book is abstract and cannot be instantiated 

        Scanner sc = new Scanner(System.in);
        String title = sc.nextLine();
        MyBook new_novel = new MyBook();
        new_novel.setTitle(title);
        System.out.println("The title is: " + new_novel.getTitle());
        sc.close();
    }
}