#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <string>
#include <math.h>
using namespace std;
/*class Car
{
double speed;
public:
    Car(double s) : speed(s) // Constructor 
    {
    
    }
    ~Car() // Destructor 
    {

    }
    void displaySpeed() const 
    {
        cout << "Speed: " << speed << " km/h" << endl;
    }
};
class A
{
public: 
void fun();   // only declaration
}; 
void A::fun()
{      // function definition
cout<<"in fun()"<<endl;
} 
int main()
{ 
A obj;  
obj.fun(); 
}*/

/* // Implementation Of Stack Using Two Queues(Arrays)
int n,p,m;
int t = 0;
int y = 0;
int d = 0;
int front=0;
int rear=0;
int front1=0;
int rear1=0;
int main()
{
int ch;
cout<<"Please Enter The Value of n ";
cin>>n;
cout<<"Please Enter The Value of m ";
cin>>m;
int a[n];
int b[2*m];
int c[m+n];
void enqueue(int a[],int b[],int c[]);
void dequeue(int a[],int b[],int c[]);
void print(int a[],int b[]);
while(ch!=4)
{
cout<<"Please Enter Your Choice\n";
cout<<" 1.Enqueue\n 2.Dequeue\n 3.Print\n 4.Exit\n ";
cin>>ch;
    switch(ch)
    {
        case 1: enqueue(a,b,c);
        break;
        case 2: dequeue(a,b,c);
        break;
        case 3: print(a,b);
        break;
        case 4: break;
        default: cout<<"Wrong Choice Entered. Please Try Again"<<endl;
    }
}
}
void enqueue(int a[],int b[],int c[])
{
    int ele;
    if(rear==n || rear1==m)
    {
        cout<<"Queue Is Full\n";
        return;
    }
    cout<<"Enter The Element To Enqueue ";
    cin>>ele;
    c[y] = ele;
    y++;
    t++;
    if(ele%2 != 0)
    {
        a[rear] = ele;
        rear++;
    }
    else
    {
        b[rear1] = ele;
        rear1++;
    }
}
void dequeue(int a[],int b[],int c[])
{
    int i,j;
    p = 0;
    if(d == 1 || rear == front || rear1 == front1)
    {
        cout<<"Queue Is Empty\n";
        return;
    }
    while(i!=1)
    {
        while(rear!=front)
        {
            if(p == 0)
            b[rear1] = a[rear - 1];
            else
            b[rear1] = a[rear - 1];
            p++;
            rear--;
            rear1++;
        }
        i = 1;
    }
    for(i = 0;i<=t-1;i++)
    {
        b[0, i] = c[i];
    }
    cout<<endl;
    d++;
}
void print(int a[],int b[])
{
    if(front!=rear)
    {
        cout<<"Elements In Queue 1 Are \n";
       for(int i=front;i<rear;i++)
        cout<<a[i]<<" ";
        cout<<endl;
    }
   else
   {
       cout<<"There Is No Element In The Queue 1\n";
   }
   if(d == 1)
   {
    if(front1!=rear1)
    {
        cout<<"Elements In Queue 2 Are \n";
       for(int i=rear1-1;i>=front1;i--)
        cout<<b[i]<<" ";
    }
   else
   {
       cout<<"There Is No Element In The Queue 2\n";
   }
   }
   else
   {
    if(front1!=rear1)
    {
        cout<<"Elements In Queue 2 Are \n";
       for(int i=front1;i<rear1;i++)
        cout<<b[i]<<" ";
    }
   else
   {
       cout<<"There Is No Element In The Queue 2\n";
   }
   }
   cout<<endl;
}*/

/*class Complex
{
float real, imag, real1, imag1;
public:
int fun();
void input()
{
    cout << "Enter Two Numbers Of First Complex Number: ";
    cin >> real >> imag;
    cout << "Enter Two Numbers Of Second Complex Number: ";
    cin >> real1 >> imag1;
}
void display()
{
cout<< "The First Complex Number is: " << real << " + " << imag << "i" << endl;
cout<< "The Second Complex Number is: " << real1 << " + " << imag1 << "i" << endl;
}
void sum()
{
    float realSum = real + real1;
    float imagSum = imag + imag1;
    cout << "The Sum of Complex Numbers is: " << realSum << " + " << imagSum << "i" << endl;    
}
};
int Complex::fun()
{
cout<<"Hello World";
}
int main()
{
    Complex obj;
    //obj.input();
    //obj.display(); // Display the complex number
    //obj.sum(); // Calculate and display the sum of complex numbers
    obj.fun();
}*/

/*class Date
{
    private:
    int month,day,year;
    void setmonth(int m)
    {
        if(m < 1 || m > 12)
        {
            month = 12;
            return;
        }
        else
        month = m;
    }
    void setday(int d, int m,int y)
    {
        if(d < 1 || d > 31)
        {
            day = 31;
            return;
        }
        else if((m == 2 && d > 29) || (m == 2 && d == 29 && (y % 400 != 0 && y % 4!=0)))
        {
            day = 28;
            return;
        }
        else if((m == 4 || m == 6 || m == 9 || m == 11) && d > 30)
        {
            day = 30;
            return;
        }
        else
        day = d; 
    }
    void setyear(int y)
    {
        year = y;
    }
    public:
    void showdate()
    {
        cout << "Date: " << day << "/" << month << "/" << year << endl;
    }
    void setdate(int d, int m, int y)
    {
        day = d;
        month = m;
        year = y;
        //setmonth(m);
        //setday(d,m,y);
        //setyear(y);
    }
    void increaseday()
    {
    day++;
    if(month>12)
    {
        month = 1;
        year++;
    }
    if((month == 12) && (day = 31))
    {
        month = day = 1;
        year++;
    }
    if((month == 4 || month == 6 || month == 9 || month == 11) && day > 30)
    {
    day = 1;
    month++;
    }
    else if((month == 1 || month == 5 || month == 3 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31)
    {
    day = 1;
    month++;
    }
    else if(month == 2 && day > 28 && (year % 400!=0 && year % 4!=0))
        {
            day = 1;
            month++;
        }
    else if(month == 2 && day > 29)
        {
            day = 1;
            month++;
        }
    }
};
int main()
{
Date date1;
/*date1.setdate(29,2 ,2024);
date1.showdate();
date1.setdate(29,2, 2023);
date1.showdate();
date1.setdate(31,4, 2023);
date1.showdate();
date1.setdate(15,12,2100);
date1.showdate();
date1.setdate(29, 12, 2007);
for (int i = 0; i < 400; i++) 
{
date1.increaseday();
date1.showdate();
}
}*/
/*int main()
{
int i,j,n,count = 0;
cout<<"Enter The Size Of Array ";
cin>>n;
int a[n];
cout<<"Enter The Array Elements "<<endl;
for(i = 0;i<n;i++)
cin>>a[i];
for(i = 0;i<n;i++)
{
    for(j=i+1;j<n;j++)
    {
        if(i<j && a[i] > a[j])
        count++;
    }
}
cout<<"No Of Inversions In The Array is = "<<count;
}*/

/*int main()
{
int i,n,sum = 0,flag = 1;
cout<<"Enter The Size Of Array ";
cin>>n;
int a[n];
cout<<"Enter The Array Elements ";
for(i = 0;i<n-1;i++)
cin>>a[i];
for(i = 0;i<n;i++)
{
    if(a[i]!=sum)
    {
    cout<<"The Missing Number in The Array is = "<<sum;
    flag = 1;
    break;
    }
    sum++;
}
if(flag == 0)
cout<<"No Missing no. In The Array";
}*/

// Balanced Paranthesis Program(To Be Done)
/*int n;
int top=0;
int main()
{
int ch;
printf("Please Enter value of n");
scanf("%d", &n);
char a[n];
void push(char a[]);
void pop(char a[]);
void print(char a[]);
while(ch!=4)
{
printf("Please Enter Your Choice\n");
printf(" 1.Push\n 2.Pop\n 3.Print\n 4.Exit\n");
scanf("%d", &ch);
    switch(ch)
    {
        case 1: push(a);
        break;
        case 2: pop(a);
        break;
        case 3: print(a);
        break;
        case 4: break;
        default: printf("Wrong Choice Entered");
    }
}
}
void push(char a[])
{
    char ele[100];
    if(top==n)
    {
        printf("Stack Is Full\n");
        return;
    }
    else
    {
        printf("Enter The Element\n");
        scanf("%d", &ele);
       a[top]=ele;
       top++;
    }
}
void pop(char a[])
{
    if(top==0)
    {
        printf("Stack Is Empty\n");
        return;
    }
   else
   {
       top--;
       printf("Deleted Element Is=%d\n",a[top]);
   }
}
void print(char a[])
{
    if(top>0)
    {
        printf("Elements Are \n");
       for(int i=top-1;i>=0;i--)
    {
        printf("%d\t",a[i]);
    } 
    }
   else
   {
       printf("There Is No Element\n");
   }
}*/

// Find Missing No.(Using Linear Search)
/*int main()
{
int i,n,flag = 0;
cout<<"Enter The Size Of Array ";
cin>>n;
int a[n];
cout<<"Enter The Array Elements "<<endl;
for(i = 0;i<n-1;i++)
cin>>a[i];
for(i = 0;i<n;i++)
{
    if(a[i]!= i + 1)
    {
    cout<<"The Missing Number in The Array is = "<<i + 1;
    flag = 1;
    break;
    }
}
if(flag == 0)
cout<<"No Missing No. In The Array";
}*/

// Find Missing No.(Using Binary Search)
/*int main()
{
int i,n,flag = 0,min = 0,mid,mid1;
cout<<"Enter The Size Of Array ";
cin>>n;
int max = n-1;
int a[n];
cout<<"Enter The Array Elements "<<endl;
for(i = 0;i<n-1;i++)
cin>>a[i];
while(min<=max)
{
mid = (min + max)/2;
mid1 = ceil(mid);
if(a[mid1] == mid + 1)
min = mid + 1;
else if(a[mid1] != mid + 1)
max= mid - 1;
}
cout<<"The Missing Number In The Array is = "<< mid + 1;
}*/

/*class Demo_static
{
    private:
    static int x;
    int y;
    public:
    void init()
    {
        //x = 10;
        //y = 20;
        x++;
        y++;
    }
    void display()
    {
        cout << "x = " << x << ", y = " << y << endl;
    }
};
int Demo_static::x = 10;
int main()
{
    Demo_static obj,obj1;
    obj.init();
    obj.display();
    obj1.init();
    obj1.display();
}*/

/* // Call By Address, Call By Value and Call By Reference
class Demo
{
public:
int a;
int b;
void fun(int &a,int &b)
{
cout<< a + b; //Call By Reference(Direct Access)
}
void fun1(int *a,int *b)
{
cout<< *a + *b; // Call By Address(Indirect Access)
}
void fun2(int a,int b)
{
cout<< a + b; // Call By Value
}
};
int main()
{
Demo obj;
obj.a = 10;
obj.b = 20;
obj.fun(obj.a,obj.b);
obj.fun1(&obj.a,&obj.b);
obj.fun2(obj.a,obj.b);
}*/

/*// Friend Function
class test
{	int a, b;
    friend  void sum(test x);
    public:
	void getdata(int i, int j);
};
void test::getdata(int i, int j)
{	
    a = i;	
    b = j;	
}
void sum(test x)
{
    cout<< x.a+x.b;
}
int main()
{	test n;
	n.getdata(3, 4);
	sum(n);
}*/

/*// Program To Make Sure Every Element Occurs At Most K Times
int main() 
{
    int n, k, count = 1;
    cout << "Enter The Size Of The Array: ";
    cin >> n;
    cout << "Enter The Value Of K: ";
    cin >> k;
    int a[n];
    cout << "Enter The Array Elements (In Sorted Order): ";
    for (int i = 0; i < n; i++)
        cin >> a[i];
    int result[n]; // Result array to hold valid values
    int resIndex = 0; // Index for result array
    result[resIndex++] = a[0]; // Always keep first element
    for (int i = 1; i < n; i++) 
    {
        if (a[i] == a[i - 1]) 
            count++;
        else 
          count = 1; 
        if (count <= k) 
            result[resIndex++] = a[i];
        // Else: skip adding this duplicate
    }
    cout << "Resulting Array: ";
    for (int i = 0; i < resIndex; i++)
        cout << result[i] << " ";
}*/

/*// Program To Print(Display Or Represent) A Sparse(Triplet) Matrix
int main()
{
int i,j,k,n,p,q;
cout<<"Enter The Total No. Of Rows Of The Sparse Matrix "<<endl;
cin>>p;
cout<<"Enter The Total No. Of Columns Of The Sparse Matrix "<<endl;
cin>>q;
cout<<"Enter The No. Of Non Zero Entries in The Sparse Matrix "<<endl;
cin>>n;
int a[3][n];
cout<<"Enter The Row Indexes "<<endl;
for(i=0;i<n;i++)
cin>>a[0][i];
cout<<"Enter The Column Indexes "<<endl;
for(j=0;j<n;j++)
cin>>a[1][j];
cout<<"Enter The Values "<<endl;
for(k=0;k<n;k++)
cin>>a[2][k];
cout<<"The Sparse Matrix is:"<<endl;
for(i=0;i<3;i++)
{
    for(j=0;j<n;j++)
    cout<<a[i][j]<<" ";
    cout<<endl;
}
k = 0;
for(i=0;i<p;i++)
{
    for(j=0;j<q;j++)
    {
        if(i == 0 && j == 0 || i == 0 && j == 1 || i == 0 && j == 2)
        {
            cout<<a[2][k]<<" ";
            k++;
            cout<<endl;
        }
        else
        cout<<0;
        
    }
}
}*/

/*// Boyer Moore Majority Algorithm: -
int main()
{
    int n,i,major,count = 0;
    cout<<"Enter The Size Of The Array ";
    cin>>n;
    int a[n];
    cout<<"Enter The Array Elements ";
    for(i=0;i<n;i++)
    cin>>a[i];
    for(i=0;i<n;i++)
    {
    if(count == 0)
{
    major = a[i];
    count = 1;
}
else if(a[i]== major)
count++;
else
count--;
}
count = 0;
for(i=0;i<n;i++)
{
    if(major == a[i])
    count++;
}
if(count > n/2)
cout<<"The Major Element is = "<<major;
else
cout<<"No Majority Element";
}*/

/*// Average Marks Of A Student Program
class STUDENT
{
int ROLL_NO;
char NAME[20];
public:
int MARKS[5];
STUDENT(){}
STUDENT(int x,char y[])
{
    ROLL_NO = x;
    strcpy(NAME,y);
}
void avgMarks()
{
int i,sum = 0;
cout<<"The Average Marks Of Roll no. "<<ROLL_NO<<" Named "<<NAME<<" Is = "<<endl;
for(i=0;i<5;i++)
sum = sum + MARKS[i];
cout<<(float)sum/5;
}
};
int main()
{
int x,i;
char y[20];
cout<<"Enter The Roll No. Of The Student ";
cin>>x;
cout<<"Enter The Name Of The Student(20 Characters Max) ";
cin>>y;
STUDENT a(x,y);
cout<<"Enter The Marks Of 5 Subjects(In Range(0-10)Only) ";
for(i=0;i<5;i++)
cin>>a.MARKS[i];
a.avgMarks();
}*/

/*// Dynamic Constructor Program
#include <iostream>
using namespace std;
class Base
{
    int *p;
    float *q;
    double z;
public:
    Base(int a,float b)
    {
        p = new int;
        *p = a;
        q = new float;
        *q = b;
        z = 30;
    }
    void display()
    {
        cout << "The Value of Integer is = " << *p << endl;
        cout << "The Value Of Float is = " << *q << endl;
        cout << "The Value Of Double is = " << z << endl;
    }
    ~Base()
    {
        delete p; 
        delete q;
    }
};
int main()
{
    Base b(10,20.5);
    b.display();
}*/

/*// PostFix Evaluation Program
int main()
{
int i,m,n,a,b,c,top=0;
cout<<"Please Enter Value Of n ";
cin>>n;
cout<<"Please Enter The No. Of Elements And Symbols For The PostFix Evaluation ";
cin>>m;
int r[n];
char s[m];
cout<<"Enter The Elements And Symbols For The PostFix Evaluation\n";
for(i=0;i<m;i++)
cin>>s[i];
for(i=0;i<m;i++)
{
if(isdigit(s[i]))
{
s[i] = s[i] - '0';
if(top==n)
    {
        printf("Stack Is Full\n");
        break;
    }
    else
    {
       r[top]=s[i];
       top++;
    }
}
if((s[i] == '+')||(s[i] == '-')||(s[i] == '*')||(s[i] == '/')||(s[i] == '^')||(s[i] == '%'))
{
if(top==0)
{
printf("Stack Is Full\n");
break;
}
else
{
top--;
b = r[top];
top--;
a = r[top];
if(s[i] == '+')
{
c = a + b;
r[top] = c;
top++;
}
if(s[i] == '-')
{
c = a - b;
r[top] = c;
top++;
}
if(s[i] == '*')
{
c = a * b;
r[top] = c;
top++;
}
if(s[i] == '/')
{
if(b==0 && a!=0)
{
cout<<"Division Is Not Possible By 0";
exit(0);
}
else
{
c = a / b;
r[top] = c;
top++;
}
}
if(s[i] == '^')
{
c = pow(a,b);
r[top] = c;
top++;
}
if(s[i] == '%')
{
if(b==0 && a!=0)
{
cout<<"Division Is Not Possible By 0, So Can't Find Remainder";
exit(0);
}
else
{
c = a % b;
r[top] = c;
top++;
}
}
}
}
}
cout<<"PostFix Evaluation Result Is = \n";
cout<<r[0];
}*/


// class X
// {
// protected:
// char a[20];
// public:
// X()
// {
//     cout<<"Enter The Name Of The Person ";
//     cin>>a;
//     cout<<"Constructor Of Class X Called\n";
// }
// ~X()
// {
//     cout<<"Destructor Of Class X Called\n";
// }
// };
// class Y: public X
// {
// protected:
// char b[20];
// public:
// Y()
// {
//     cout<<"Enter The Name Of The Person's Father ";
//     cin>>b;
//     cout<<"Constructor Of Class Y Called\n";
// }
// ~Y()
// {
//     cout<<"Destructor Of Class Y Called\n";
// }
// };
// class Z: public Y
// {
// public:
// Z()
// {
// cout<<"Concatenation Of Names Is = "<<a<<b<<endl;
// cout<<"Constructor Of Class Z Called\n";
// }
// ~Z()
// {
//     cout<<"Destructor Of Class Z Called\n";
// }
// };
// int main()
// {
// Z c;
// }


// 1. Static (stack) array of objects
// Objects allocated contiguously on stack; ctors/dtors run automatically; no polymorphism via base-type array.

//Student arr[3]; // stack array of objects

// 2. Dynamic (heap) array of objects
// Single pointer to contiguous objects on heap; use delete[]; cannot new abstract base.

// Student* arr = new Science[3]; // heap array of objects
// delete[] arr;

// 3. Pointer to single heap object
// Single owning pointer to one object; use delete.

// Student* p = new Science("A",1);
// delete p;

// 4. Pointer to single stack object (non-owning)
// Pointer references a stack object; do NOT delete.

// Student s;
// Student* p = &s; // non-owning

// 5. Static (stack) array of pointers
// Array of pointers lives on stack; pointees usually on heap; delete each pointee only.

// Student* ptrs[3];
// ptrs[0] = new Science(...);
// cleanup: for (...) delete ptrs[i];

// 6. Dynamic (heap) array of pointers (pointer-array on heap)
// Pointer-array itself on heap (Student**), pointees on heap; must delete each pointee then delete[] pointer-array.

// Student** ptrs = new Student*[n];
// ptrs[0] = new Science(...);
// // cleanup: for (...) delete ptrs[i]; delete[] ptrs;

// 7. Heap arrays of objects, with a stack array of pointers pointing to them
// allocate one or more arrays of objects on the heap (new T[n]) and store their addresses in a stack array of pointers. The stack pointer-array does not own the memory; you must delete[] each heap array when done.

// // allocate two arrays of Science objects on the heap
//     Student* arr1 = new Science[3]; // arr1[0..2]
//     Student* arr2 = new Science[2]; // arr2[0..1]

//     // stack array of pointers pointing to those heap arrays
//     Student* arrays[2] = { arr1, arr2 };

//     // use: arrays[i][j]
//     arrays[0][1].info(); // arr1[1]
//     arrays[1][0].info(); // arr2[0]

//     // cleanup: delete each heap array (use delete[]), do NOT delete[] arrays (it's on stack)
//     delete[] arr1;
//     delete[] arr2;

// 8. Pointer-to-array (pointer to whole array type)
// A pointer that points to an array object (stack or heap) — non-owning or owning depending on allocation.

// Student stackA[5];
// Student (*parr)[5] = &stackA;  // pointer-to-array (non-owning)

// 9. Array (or pointer-array) of pointers to arrays (arrays-of-arrays / ragged 2D)
// Each element points to a separate array (stack or heap). Must delete[] each sub-array, then free pointer-array if heap-allocated.

// Student** arrays = new Student*[m];
// for (int i=0;i<m;++i) arrays[i] = new Science[size_i];
// // cleanup: for (i) delete[] arrays[i]; delete[] arrays;

// 10. reference-to-pointer (aliasing a pointer)

// Student* p = new Science("X");
// Student*& pref = p;   // pref is a reference to pointer p
// pref->info();         // same as p->info()
// delete p;

// 11. Reference-to-array (non-owning alias to an array)

// Student arr[3];
// Student (&refArr)[3] = arr;   // ref to whole array
// refArr[1].info();

// 12. Pointer-to-array type (already saw) vs. reference-to-pointer

// Student* arrHeap = new Science[4];        // heap array
// Student** pp = &arrHeap;                  // pointer-to-pointer (can modify arrHeap)
// Student*& refToPtr = arrHeap;             // reference to pointer
// refToPtr[2].info();
// delete[] arrHeap;

// 13. Pointer-to-member-data and pointer-to-member-function (different kind of pointer)

// int Student::* pdata = &Student::roll;           // pointer to data member
// void (Student::*pmf)() = &Student::info;         // pointer to member function

// Student s("X", 1);
// s.*pdata = 42;
// (s.*pmf)();

// 14. Array of function pointers (functions producing/returning pointers)

// Student* makeSci() { return new Science("F"); }
// Student* (*factories[])() = { makeSci };

// Student* p = factories[0](); // call factory -> new object
// delete p;

// 15. Pointer-to-pointer for jagged 2D (Student*** variant) — fully dynamic ragged 2D

// int rows = 2;
// Student*** table = new Student**[rows];
// table[0] = new Student*[2]; table[1] = new Student*[3];
// table[0][0] = new Science("a"); /* ... */
// for (...) delete table[i][j];
// delete[] table[0]; delete[] table[1]; delete[] table;

// 16. Pointer-to-member-pointer (rarely useful, but possible)

// Student* p = new Science("Y");
// Student** pp = &p;
// (*pp)->info();
// delete *pp; // frees object

// class Config 
// {
// private:
//     string language;
//     static int activePlayerCount;
//     // Private constructor for internal use, such as for the static reference object.
//     // It has a unique signature to prevent accidental use.
//     Config(int) : language("English"){}
// public:
//     // Public constructor for players to specify a language.
//     Config(const string& specifiedLanguage) : language(specifiedLanguage) 
//     {
//         cout << "Language set to '" << this->language << "'." << endl;
//         activePlayerCount++;
//     }
//     // Default constructor for players without a specified language.
//     // This delegates to the parameterized constructor with the default language.
//     Config() : Config("English") 
//     {
//         cout << "As no language was specified, default language set to '" << this->language << "'." << endl;
//     }
//     Config(const Config& other) : language(other.language) // Custom copy constructor for copying language settings.
//     {
//         // Here we can use the default_config object, as it is now properly defined.
//         if (other.language == Config::default_config.language) 
//         {
//             cout << "Copied default language setting to player. Language is now '" << this->language << "'." << endl;
//         } 
//         else 
//         {
//             cout << "Copied language from another player. Language is now '" << this->language << "'." << endl;
//         }
//         activePlayerCount++;
//     }
//     static void displayPlayerCount()  // Static function to display the number of active players.
//     {
//         cout << "\nTotal active players: " << activePlayerCount << endl;
//     }
//     static Config default_config; // Static reference object representing the default language settings.
// };
// int Config::activePlayerCount = 0;
// // 2. Define and initialize the static default_config object.
// // We use the private constructor `Config(int)` to prevent output messages.
// Config Config::default_config(0);
// int main() 
// {
//     Config player1; // Player 1 uses the default language.
//     Config player2("Spanish"); // Player 2 specifies their own language.
//     Config player3 = Config::default_config; // Player 3 copies the language from the static default object.
//     Config player4 = player2; // Player 4 copies the language from another player.
//     Config::displayPlayerCount(); // Display the total number of active players.
// }

// Operator +Overloading
// class Time
// {
// int h,m,s;
// public:
// Time(){}
// Time(int h,int m,int s)
// {
// this->h = h;
// this->m = m;
// this->s = s;
// }
// void show()
// {
// cout<<"The Addition Of The Two Time's Is: "<<h<<":"<<m<<":"<<s;
// }
// friend Time operator+(Time t1,Time t2);
// };
// Time operator+(Time t1,Time t2)
// {
// Time h;
// h.h = t1.h + t2.h;
// h.m = t1.m + t2.m;
// h.s = t1.s + t2.s;
// return h;
// }
// int main()
// {
// Time t1(5,15,34),t2(9,53,58),t3;
// t3 = operator+(t1,t2);
// t3.show();
// }

// Function Overriding
// class A
// {
// int a;
// public:
// A()
// {
// a = 10;
// }
// virtual void print() = 0; //Pure Virtual Function, Abstract Class
// };
// class B: public A
// {
// int b;
// public:
// B()
// {
// b = 20;
// }
// void print()
// {
// cout<<"b = "<<b;
// }
// };
// int main()
// {
// // B a;
// // A *a = new B();
// // a->print(); //Late Binding(Run Time)
// // B b;
// // A *a = &b;
// // a->print(); //Early Binding(Compile Time)
// // A *a = new B();
// // a->print(); //Early Binding(Compile Time)
// // A *a = new A();
// // B *b = new B();
// // a->print(); //Early Binding(Compile Time)
// // b->print(); //Early Binding(Compile Time)
// // a.print(); //Early Binding(Compile Time)
// // b.print(); //Early Binding(Compile Time)
// }

// class Student
// {
// public:
// Student(){}
// virtual void print()= 0;
// virtual ~Student(){}
// };
// class Engineering: public Student
// {
// public:
// Engineering(){}
// void print() override
// {
// cout<<"10"<<endl;
// }
// };
// class Medicine: public Student
// {
// public:
// Medicine(){}
// void print() override
// {
// cout<<"20"<<endl;
// }
// };
// class Science: public Student
// {
// public:
// Science(){}
// void print() override
// {
// cout<<"30";
// }
// };
// int main()
// {
// Student *a[3];
// // Student **a = new Student*[3];
// a[0] = new Engineering();
// a[0]->print();
// a[1] = new Medicine();
// a[1]->print();
// a[2] = new Science();
// a[2]->print();
// for(int i=0;i<3;i++)
// delete a[i];
// // delete [] a;
// }

// class Shape
// {
// public:
// Shape(){}
// virtual void Area() = 0;
// virtual void Display(){}
// virtual ~Shape() = default;
// };
// class Circle: public Shape
// {
// float r,area;
// public:
// Circle(float r){this->r = r;}
// void Area() override
// {
// area = 3.14*r*r;
// }
// void Display() override
// {
// cout<<"The Area Of Circle Is = "<<area<<" square units"<<endl;
// }
// };
// class Rectangle: public Shape
// {
// float l,b,area;
// public:
// Rectangle(float l,float b){this->l = l; this->b = b;}
// void Area() override
// {
// area = l*b;
// }
// void Display() override
// {
// cout<<"The Area Of Rectangle Is = "<<area<<" square units"<<endl;
// }
// };
// class Triangle: public Shape
// {
// float b,h,area;
// public:
// Triangle(float b,float h){this->b = b; this->h = h;}
// void Area() override
// {
// area = 0.5*b*h;
// }
// void Display() override
// {
// cout<<"The Area Of Triangle Is = "<<area<<" square units"<<endl;
// }
// };
// int main()
// {
// Shape **s = new Shape*[3];
// s[0] = new Circle(3);
// s[1] = new Rectangle(3,4);
// s[2] = new Triangle(3,4);
// for(int i = 0; i < 3; i++) 
// {
// s[i]->Area();
// s[i]->Display();
// }
// for(int i=0;i<3;i++)
// delete s[i];
// delete [] s;
// }

// Max SubArray Sum

// Approach 1(Brute Force(O(n^2)))
// int main()
// {
// int n,i,j,maxsum = 0,sum;
// cout<<"Enter The Size Of The Array ";
// cin>>n;
// int arr[n];
// cout<<"Enter The Elements Of The Array "<<endl;
// for(i=0;i<n;i++)
// cin>>arr[i];
// for(i=0;i<n;i++)
// {
// sum = 0;
// for(j = i;j<n;j++)
// {
// sum = sum + arr[j];
// if(sum > maxsum)
// maxsum = sum;
// }
// }
// cout<<"The Maximum Sum Of The Subarray In The Given Array Is = "<<maxsum;
// }

// Approach 2(Using Recursion(O(nlogn))
// int MaxsubarraySum(int [],int );
// int main()
// {

// }
// int MaxsubarraySum(int arr[],int n)
// {

// }

// Approach 3(O(n))
// int main()
// {
// int n,i,maxsum = 0,sum = 0;
// cout<<"Enter The Size Of The Array ";
// cin>>n;
