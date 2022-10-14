public class Main { //Cada línea de código que se ejecuta en Java debe estar dentro de un archivo class.
  //El nombre del archivo java debe coincidir con el nombre de la clase.
  //Al guardar el archivo, guárdelo con el nombre de la clase y agregue ".java"
    public static void main(String[] args) {  //Todos los programas de java deben contener un main para correr el progra
     System.out.println("Hellow world!!!");
      System.out.println("I am learning Java.");
      System.out.print("I will print on the same line."); //NO crea una nueva linea
      System.out.println(); //calculos matematicos
      
      //Variables
      //type variableName = value;

      //Variables finales
      final int myNum = 15; // No se puede cambiar
      //myNum = 10; XXXX NO se puede asignar

      String name = "John";
      System.out.println("Hello " + name); // concatenar variables
      String firstName = "John ";
      String lastName = "Doe";
      String fullName = firstName + lastName;
      System.out.println(fullName);
      
      //int x = 5, y = 6, z = 50; declarar variables en una sola linea
      char myVar1 = 65, myVar2 = 66, myVar3 = 67; //El char puede guardar el valor ASCII
      System.out.println(myVar1);
      System.out.println(myVar2);
      System.out.println(myVar3);

      //Convertir variables
      double myDouble = 9.78;
      int myInt = (int) myDouble;
      System.out.println(myInt);

      //Metodo String
      String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      System.out.println("The length of the txt string is: " + txt.length());
      System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
      System.out.println(txt.toLowerCase());   // Outputs "hello world"
      System.out.println(firstName.concat(lastName)); //Concatenar dos cadenas

      //Clase Math
      Math.max(5, 10); //encuentra el valor mas alto
      Math.min(5, 10); //Valor mas bajo
      Math.sqrt(64); //raiz 
      Math.random(); // numero al azar
      System.out.println(Math.max(5, 10));
    }
}