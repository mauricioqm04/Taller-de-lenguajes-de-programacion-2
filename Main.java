<<<<<<< HEAD
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
=======
public class Main { // Cada línea de código que se ejecuta en Java debe estar dentro de un archivo
                    // class.
  // El nombre del archivo java debe coincidir con el nombre de la clase.
  // Al guardar el archivo, guárdelo con el nombre de la clase y agregue ".java"
  public static void main(String[] args) { // Todos los programas de java deben contener un main para correr el programa
    System.out.println("Hellow world!!!");
    System.out.println("I am learning Java.");
    System.out.print("I will print on the same line."); // NO crea una nueva linea
    System.out.println(3 + 3); // calculos matematicos
>>>>>>> 16b8624844f4cff528a8a4953983119717161451

    // Variables
    // type variableName = value;

    // Variables finales
    final int myNum = 15; // No se puede cambiar
    // myNum = 10; XXXX NO se puede asignar
    System.out.println(myNum);
    String name = "John";
    System.out.println("Hello " + name); // concatenar variables
    String firstName = "John ";
    String lastName = "Doe";
    String fullName = firstName + lastName;
    System.out.println(fullName);

<<<<<<< HEAD
      //Convertir variables
      double myDouble = 9.78;
      int myInt = (int) myDouble;
      System.out.println(myInt);
=======
    // int x = 5, y = 6, z = 50; declarar variables en una sola linea
    char myVar1 = 65, myVar2 = 66, myVar3 = 67; // El char puede guardar el valor ASCII
    System.out.println(myVar1);
    System.out.println(myVar2);
    System.out.println(myVar3);
>>>>>>> 16b8624844f4cff528a8a4953983119717161451

    // Convertir variables
    double myDouble = 9.78d;
    int myInt = (int) myDouble;
    System.out.println(myInt);

    // Metodo String
    String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    System.out.println("The length of the txt string is: " + txt.length());
    System.out.println(txt.toUpperCase()); // Outputs "HELLO WORLD"
    System.out.println(txt.toLowerCase()); // Outputs "hello world"
    System.out.println(firstName.concat(lastName)); // Concatenar dos cadenas

    // Clase Math
    Math.max(5, 10); // encuentra el valor mas alto
    Math.min(5, 10); // Valor mas bajo
    Math.sqrt(64); // raiz
    Math.random(); // numero al azar
    System.out.println(Math.max(5, 10));

    /////////////////// 13 - 10 - 2022 //////////////////
    // Sentencia if

    if (20 > 18) {
      System.out.println("20 is greater than 18");
    }

    int time = 22;
    if (time < 10) {
      System.out.println("Good morning.");
    } else if (time < 20) {
      System.out.println("Good day.");
    } else {
      System.out.println("Good evening.");
    }
    // Outputs "Good evening."

    // Operador terniario
    String result = (time < 18) ? "Good day." : "Good evening.";
    // variable = (condition) ? expressionTrue : expressionFalse;
    System.out.println(result);

    // Switch
    int day = 4;
    switch (day) {
      case 1:
        System.out.println("Monday");
        break;
      case 2:
        System.out.println("Tuesday");
        break;
      case 3:
        System.out.println("Wednesday");
        break;
      case 4:
        System.out.println("Thursday");
        break;
      case 5:
        System.out.println("Friday");
        break;
      case 6:
        System.out.println("Saturday");
        break;
      case 7:
        System.out.println("Sunday");
        break;

      default:
        System.out.println("Looking forward to the Weekend");

    }// Outputs "Thursday" (day 4)

    // Ciclo While
    int i = 0;
    System.out.print("-");
    while (i < 5) {
      System.out.print(i + "-");
      i++;
    } // end while

    // Ciclo do-While
    int l = 0;
    do {
      System.out.print(l + "-");
      l++;
    } while (l < 5);

    // Ciclo for
    for (int k = 0; k < 5; k++) {
      System.out.print(k + "-");
    } // end for

    System.out.println("Este ejemplo solo imprimirá valores pares entre 0 y 10:");
    for (int t = 0; t <= 10; t = t + 2) {
      System.out.println(t + "-");
    } // end for
      // Nota: El ciclo aumenta despues de ejecutar el bloque de codigo

    // Ciclo For-each
    String[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
    // (type variableName : arrayName) <- Estructura
    for (String j : cars) {
      System.out.println(j);
    } // end for - each

    // Sentencia break para salir de un bucle
    for (int m = 0; m < 10; m++) {
      if (m == 4) {
        break;
      }
      System.out.println(m);
    } // end for

    // Sentencia continue
    System.out.println("Sentencia continue");
    for (int q = 0; q < 10; q++) {
      if (q == 4) {
        continue;
      }
      System.out.print(q + "-");
    }

    // Arreglos
    // Para declarar una matriz, defina el tipo de variable con corchetes
    //String[] cars2;
    //String[] cars2 = {"Volvo", "BMW", "Ford", "Mazda"};
    cars[0] = "Opel"; //cambiar valor en el primer indice
    //int longitud  = cars.length;
    for (String a : cars) {
      System.out.print(" \""+ a+"\" ");
    }
  }
}