// class Main{
// public static void main(String args[]) {
// 	int m[][] = {{ 1, 9, 7, 2 },{ 2, 4, 6, 5 },{ 6, 5, 3, 4 },{ 5, 4, 8, 5 }};
// 	int i, j, a=0;
// 	for(i=0; i<4; i++) {
// 	    for(j=0; j<4; j++)
//     	    a+=m[i][j];
// 	    }
// 	System.out.println(a);
//     }
// }

// class Main{
// 	public static void main(String args[]) {
// 		int m[][] = {{ 1, 9, 7, 2 },{ 2, 4, 6, 5 },{ 6, 5, 3, 4 },{ 5, 4, 8, 5 }};
// 		int i, j;
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++)
// 			    if (i==j) // diagonal matrix
// 					System.out.print(m[i][j]);
// 				else
// 				    System.out.print(" ");
// 			System.out.println();
// 			}

// 		}
// }

// class Main{
// 	public static void main(String args[]) {
// 		int m[][] = {{ 1, 9, 7, 2 },{ 2, 4, 6, 5 },{ 6, 5, 3, 4 },{ 5, 4, 8, 5 }};
// 		int i, j;
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++){
//                 System.out.print(m[i][j]);
//                 System.out.print(" ");
//             }

// 			    // if (i==j) // diagonal matrix
// 				// 	System.out.print(m[i][j]);
// 				// else
// 				//     System.out.print(" ");
// 			System.out.println();
// 			}
// 		}
// }

// // import java.util.Scanner;
// public class Main{
// 	public static void main(String args[]){
//         // Scanner sc = new Scanner(System.in);
// 		// int a;
// 		System.out.print(Integer.SIZE/8);
// 		// a = sc.nextInt();
// 		// System.out.println("mayur "+a);
// 	}
// }

// import java.util.Scanner;
// public class Main{
// 	public static void main(String args[]){
// 		Scanner sc=new Scanner(System.in);
// 		int a;
// 		float b;
// 		System.out.print("a ");
// 		a=sc.nextInt();
// 		System.out.print("b ");
// 		b=sc.nextFloat();
// 		System.out.println("a and b is "+a+" & "+b);
// 	}
// }

// class Main{
// 	public static void main(String args[]) {
//         System.out.println(Math.PI);
//     }
// } 

// // //................................Assignment-6
// //1. Write a java program to input matrix using an array and 
// //print the sum of elements of the matrix.
// import java.util.Scanner;
// class Main{
// 	public static void main(String args[]) {
// 		Scanner sc= new Scanner(System.in);
// 		int i, j, a=0;
// 		int m[][] = new int[3][3];
// 		System.out.println("enter 3*3 matrix");
// 		for(i=0; i<3; i++) {
// 			for(j=0; j<3; j++){
// 				System.out.print("M"+(i+1)+(j+1)+"=");
// 			    m[i][j]= sc.nextInt();
// 			}
// 		}
// 		System.out.println("Given matrix is");
// 		for(i=0; i<3; i++) {
//             System.out.print("|");
// 			for(j=0; j<3; j++)
//                 System.out.print(m[i][j]+" ");
//             System.out.println("|");
// 		}
//         for(i=0; i<3; i++) {
//             for(j=0; j<3; j++)
//                 a+=m[i][j];
//             }
//         System.out.println("the sum of elements of the given matrix is "+a);
//     }
// }

// //2. Write a java program to input matrix using an array and print diagonal, 
// //upper diagonal and lower diagonal elements.
// import java.util.Scanner;
// class Main{
// 	public static void main(String args[]) {
// 		Scanner sc= new Scanner(System.in);
// 		int i, j;
// 		// int m[][] = {{ 1, 9, 7, 2 },{ 2, 4, 6, 5 },{ 6, 5, 3, 4 },{ 5, 4, 8, 5 }};
// 		int m[][] = new int[4][4];
// 		System.out.println("enter 4*4 matrix");
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++){
// 				System.out.print("M"+(i+1)+(j+1)+"=");
// 			    m[i][j]= sc.nextInt();
// 			}
// 		}
// 		System.out.println("diagonal matrix");
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++)
//                 if (i==j)  // diagonal matrix
// 					System.out.print(m[i][j]+" ");
// 				else
// 				    System.out.print("  ");
// 			System.out.println();
// 		}
// 		System.out.println("upper matrix");
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++)
//                 if (i<j)  // upper matrix
// 					System.out.print(m[i][j]+" ");
// 				else
// 				    System.out.print("  ");
// 			System.out.println();
// 		}
// 		System.out.println("lower matrix");
// 		for(i=0; i<4; i++) {
// 			for(j=0; j<4; j++)
//                 if (i>j)  // lower matrix
// 					System.out.print(m[i][j]+" ");
// 				else
// 				    System.out.print("  ");
// 			System.out.println();
// 		}
// 	}
// }

// //3. Write a java program to input two matrices, 
// //find element wise sum and store in third matrix.
// import java.util.Scanner;
// import java.util.Arrays;
// class Main{
// 	public static void main(String args[]) {
// 		Scanner sc= new Scanner(System.in);
// 		int i, j;
// 		int m[][] = new int[3][3];
// 		int n[][] = new int[3][3];
// 		int p[][] = new int[3][3];
//         System.out.println("enter first 3*3 matrix M");
// 		for(i=0; i<3; i++) {
// 			for(j=0; j<3; j++){
// 				System.out.print("M"+(i+1)+(j+1)+"=");
// 			    m[i][j]= sc.nextInt();
// 			}
// 		}
// 		System.out.println("enter second 3*3 matrix N");
// 		for(i=0; i<3; i++) {
// 			for(j=0; j<3; j++){
// 				System.out.print("N"+(i+1)+(j+1)+"=");
// 			    n[i][j]= sc.nextInt();
// 			}
// 		}
// 		System.out.println("sum of Given matrix is");
// 		for(i=0; i<3; i++) {
// 			for(j=0; j<3; j++)
//                 System.out.print(m[i][j]+n[i][j]+" ");
// 			System.out.println();
// 		}
// 		for(i=0; i<3; i++) {
// 			for(j=0; j<3; j++)
// 		    	p[i][j]=m[i][j]+n[i][j];
// 		}
// 		System.out.println("third matrix P is");
//         System.out.print(Arrays.deepToString(p));
// 	}
// }

// // 4.Write a java program to create student class. 
// // Take student name, ID, Roll No, Age, and Gender as data members. 
// //  Write constructors. Write input and show methods.
// import java.util.Scanner;
// class Student{
//     String name;
//     int id, roll_no;
//     byte age;
//     char gender;
//     void input(){
//         Scanner sc = new Scanner(System.in);
//         System.out.print("enter name: ");
//         name=sc.next();
//         System.out.print("enter id : ");
//         id=sc.nextInt();
//         System.out.print("enter roll_no : ");
//         roll_no=sc.nextInt();
//         System.out.print("enter age: ");
//         age=sc.nextByte();
//         System.out.print("enter gender: ");
//         gender=sc.next().charAt(gender);
//     }
//     void display(){
//         System.out.println("D I S P L A Y");
//         System.out.println("name: "+name);
//         System.out.println("id: "+id);
//         System.out.println("Roll No.: "+roll_no);
//         System.out.println("age: "+age);
//         System.out.println("gender: "+gender);
//     }
// }
// class Main{
//     public static void main(String args[]){
//         Student s1 = new Student();
//         s1.input();
//         s1.display();
//     }
// }

// // 5. Write a java program to create a box class having length, breath and height as data
// // members. Write constructors. Write input, volume and show methods. Create a demo class to
// // use box class.
// import java.util.Scanner;
// class Box {
//     double width;
//     double height;
//     double depth;
//     double volume() {
//         return width * height * depth;
//     }
//     void input(){
//         Scanner sc = new Scanner(System.in);
//         System.out.print("enter width: ");
//         width = sc.nextDouble();
//         System.out.print("enter height: ");
//         height = sc.nextDouble();
//         System.out.print("enter depth: ");
//         depth = sc.nextDouble();
//     }
//     void show(){
//         System.out.println("width: "+width);
//         System.out.println("height: "+height);
//         System.out.println("depth: "+depth);
//     }
// }
// class demo {
//     public static void main(String args[]) {
//         Box mybox = new Box();
//         mybox.input();
//         mybox.show();
//         double vol;
//         vol = mybox.volume();
//         System.out.println("Volume of mybox is "+vol);
//     }
// }

// //6. Write a java program to create my number class as done in class 
// //having methods input, display, isEven, is Odd, isPrime and factorial.
// import java.util.Scanner;
// class mynumber{
//     int n,i;
//     int OE(){
//         if (n%2==0){
//             return 1;
//         }
//         else return 0;
//     }
//     int prime(){
//         int b=0;
//         double s = Math.sqrt(n);
//         for (i=2;i<s;i++){
//             if (n%i==0){
//                 b=1;
//            }
//         }
//         return b;
//     }
//     long fact(){
//         int j;
//         long a;
//         a = 1;
//         for (j=1;j<=n;j++)
//             a=a*j;
//         return a;
//     }
//     void input(){
//         Scanner sc = new Scanner(System.in);
//         System.out.print("enter number: ");
//         n = sc.nextInt();
//     }
// }
// class Main {
//     public static void main(String args[]) {
//         mynumber num = new mynumber();
//         num.input();
//         int o = num.OE();
//         int p = num.prime();
//         long f = num.fact();
//         if (o==1){
//             System.out.println("given number is even.");
//         }
//         else System.out.println("given number is odd.");
//         if (p==1) System.out.println("given number is not prime.");
//         else System.out.println("given number is prime.");
//         System.out.println("factorial of given number is "+f); 
//     }
// }

// // 7. Write a java program to create a circle class having radius as data member. Write
// // constructors. Write input, area, circumfurence and show methods. Create a demo class and
// // make objects of circle class.
// import java.util.Scanner;
// class circle{
//     float r;
//     void input(){
//         Scanner sc = new Scanner(System.in);
//         System.out.print("enter a radius of the circle: ");
//         r = sc.nextFloat();
//     }
//     void show(){
//         System.out.println("Radius = "+ r +", pi = "+Math.PI);
//     }
//     void area(){
//         System.out.println("area of the circle is "+(Math.PI)*r*r);
//     }
//     void circu(){
//         System.out.println("circumfurence of the circle is "+2*(Math.PI)*r);
//     }
// }
// class Main {
//     public static void main(String args[]) {
//         circle c = new circle();
//         c.input();
//         c.show();
//         c.area();
//         c.circu();
//     }
// }

// .......................................Assignment-6
// // 1.	Write a Java program to create a matrix class and find sum of elements, trace, determinant of a matrix
// import java.util.Scanner;
// class Main {
//     public static void main(String[] args){
//         matrix m1=new matrix();
//         m1.input();
//         m1.show();
//         m1.sum();
//         m1.trace();
//         // m1.dete();
//     }
// }
// class matrix {
//     int m[][];
//     int i,j,r,c,sum=0,t=0;
//     void input(){
//         Scanner sc=new Scanner(System.in);
//         System.out.println("Enter the number of rows: ");
//         r=sc.nextInt();
//         System.out.println("Enter the number of columns: ");
//         c=sc.nextInt();
//         m = new int[r][c]; 
//         for(i=0;i<r;i++){
//             for(j=0;j<c;j++){
//                 System.out.println("A["+(i+1)+"]["+(j+1)+"]:");
//                 m[i][j]=sc.nextInt();
//             }
//         }
//     }
//     void show(){
//         for(i=0;i<r;i++){
//             System.out.print("|");
//             for(j=0;j<c;j++){
//                 System.out.print(m[i][j]+" ");
//                 }
//             System.out.println("|");
//         }
//     }
//     void sum(){
//         for(i=0;i<r;i++){
//             for(j=0;j<c;j++){
//                 sum=sum+m[i][j];
//             }
//         }
//         System.out.println("Sum of elements= "+sum);
//     }
//     void trace(){
//         for(i=0;i<r;i++){
//             for(j=0;j<c;j++){
//                 if(i==j)
//                     t=t+m[i][j];
//             }
//         }
//         System.out.println("Trace= "+t);
//     }
//     void dete(){
//         int D;
//         if (c==r){
//             if (c==2){
//                 D = m[0][0]*m[1][1]-m[0][1]*m[1][0];
//                 System.out.println("determinant of 2*2 matrix is "+D);
//             }
//             else if(c==3){
//                 D = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]);
//                 System.out.println("determinant of 3*3 matrix is "+D);
//             }
//         }
//         else System.out.println("find a determinant is not posible for this matrix");
//     }
// }

// class box {
//     // int a;
//     // int b;
//     // int c;
//     // box(){
//     // a=5;
//     // b=8;
//     // c=9;
//     // }
//     int mul(int a) {
//         return a * a * a;
//     }

//     void mul(boolean b) {
//         System.out.println(b);
//     }

//     String mul(String c) {
//         return c;
//     }
// }

// class Main {
//     public static void main(String[] args){
//         box d=new box();
//         int i=d.mul(5);
//         d.mul(true);
//         String n = d.mul("mayur");
//         // d.a=5;
//         // d.b=7;
//         // d.c=2;
//         // int e = d.mul();
//         // System.out.println(e);
//         // System.out.println(d.a+d.b+d.c);
//         System.out.println(i);
//         // System.out.println(m);
//         System.out.println(n);
//     }
// }

// class Test {
//     int i, j;
//     Test(int i, int j) {
//     this.i = i;
//     this.j = j;
//     }
//     // return true if o is equal to the invoking object
//     boolean equals(Test o) {
//     if(o.i == i && o.j == j) { return true;}
//     else return false;
//     }
//     }
//     class Main {
//     public static void main(String args[]) {
//         Test ob1 = new Test(22, 100);
//         Test ob2 = new Test(22, 100);
//         Test ob3 = new Test(-1, -1);
//         System.out.println("ob1 == ob2: " + ob2.equals(ob1));
//         System.out.println("ob1 == ob3: " + ob2.equals(ob3));
//         // System.out.println(o.i);
//     }
// }

// Here, Box allows one object to initialize another.
// class Box {
//   // private double width;
//   // private double height;
//   // private double depth;
//   double width;
//   double height;
//   double depth;
//     // construct clone of an object
//     // Box(Box b) { // pass object to constructor
//     // width = b.width;
//     // height = b.height;
//     // depth = b.depth;
//     // }
//     // constructor used when all dimensions specified
//     Box(){}
//     Box(double w, double h, double d) {
//     width = w;
//     height = h;
//     depth = d;
//     }
//     // constructor used when no dimensions specified
//     // Box() {
//     // width = -1; // use -1 to indicate
//     // height = -1; // an uninitialized
//     // depth = -1; // box
//     // }
//     // constructor used when cube is created
//     // Box(double len) {
//     // width = height = depth = len;
//     // }
//     // compute and return volume
//     double volume() {
//     return width * height * depth;
//     }
// }
// class boxwht extends Box{
//   double weight;
  
//   boxwht(double w, double h, double d, double t){
//     width = w;
//     height = h;
//     depth = d;
//     weight = t;
//   }
// }
// class Main {
//     public static void main(String args[]) {
//     // create boxes using the various constructors
//     boxwht mybox1  = new boxwht(10, 20, 15,500);
//     // Box mybox2 = new Box();
//     // Box mycube = new Box(7);
//     // Box myclone = new Box(mybox2);
//     double vol;
//     // get volume of first box
//     vol = mybox1.volume();
//     System.out.println("Volume of mybox1 is " + vol);
//     System.out.println("Box Whight is " + mybox1.weight);
//     // get volume of second box
//     // vol = mybox2.volume();
//     // System.out.println("Volume of mybox2 is " + vol);
//     // // get volume of cube
//     // vol = mycube.volume();
//     // System.out.println("Volume of cube is " + vol);
//     // // get volume of clone
//     // vol = myclone.volume();
//     // System.out.println("Volume of clone is " + vol);
//   }
// }


// class Main{
//   int a,b;
//   Main(){
//     a = 5;
//     b = 6;
//   }
//   public static void main(String args[]) {
//     int i,j;
//     Main a = new Main();
//     a.show();
//     for (i=1;i<7;i++){
//       System.out.print("*");
//       for(j=1;j<5;j++){
//         if (i==1 || i==6){
//           System.out.print("*");
//         }
//         else {
//           System.out.print(" ");
//         }  
//       }
//       System.out.println("*");
//     }
//   }
//   void show(){
//     System.out.println(a+"*"+b);
//   }
// }

// import java.util.Scanner;
// public class Main
// {
//     public static void main(String[] args){
//       int n;
//       Scanner sc = new Scanner(System.in);
//       System.out.println("Enter 1 for play music ");
//       System.out.println("Enter 2 for puse music ");
//       System.out.println("Enter 3 for stop music ");
//       System.out.print("Enter 4 for resume music : ");
//       n = sc.nextInt();
//       MyMusic m = new MyMusic();
//       if (n==1){
//         m.play();
//       }
//       else if (n==2){
//         m.puse();
//       }
//       else if (n==3){
//         m.stop();
//       }
//       else {
//         m.resume();
//       }
//     }
// }


// interface audioplayer{
//     void play();
//     void puse();
//     void stop();
//     void resume();
// }


// class MyMusic implements audioplayer{ 
//   public void play(){
//     System.out.println("Music is playing....");
//   }
//   public void puse(){
//     System.out.println("Music is pused....");
//   }
//   public void stop(){
//     System.out.println("Music is stop");
//   }
//   public void resume(){
//     System.out.println("Music is resuming....");
//   }
// }


// import java.util.Scanner;

// public class Main {

//     public static void main(String arg[]) {
// //  System.out.println("hello");
//         Complex c = new Complex();
//         c.input();
//         c.add();
//         c.sub();
//         c.show();
//     }
// }

// class Complex {

//     int R1, R2;
//     int I1, I2;
//     int a, b, c, d;

//     Complex() {
//     }

//     void input() {

//         Scanner sc = new Scanner(System.in);
//         System.out.println("enter two complex numbers :");
//         System.out.println("enter complex number1 Z1:");
//         System.out.println("R1");
//         R1 = sc.nextInt();
//         System.out.println("I1");
//         I1 = sc.nextInt();
//         System.out.println("enter complex number1 Z2:");
//         System.out.println("R2");
//         R2 = sc.nextInt();
//         System.out.println("I2");
//         I2 = sc.nextInt();

//     }

//     void add() {
// //int a, b;
//         a = R1 + R2;
//         b = I1 + I2;
//     }

//     void sub() {
//         c = R1 - R2;
//         d = I1 - I2;
//     }

//     void show() {
//         System.out.println("Z1 = " + R1 + "+(" + I1 + "i)");
//         System.out.println("Z2 = " + R2 + "+(" + I2 + "i)");
//         System.out.println("Z1 + Z2 = " + a + "+(" + b + "i)");
//         System.out.println("Z1 - Z2 = " + c + "+(" + d + "i)");
//     }
// }