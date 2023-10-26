#include <iostream>
#include <fstream>
using namespace std;

void login() {
  
}

void registrationpPage(){
    string userName;
    string passwd;
    string confirmPasswd;
    
    ofstream outputFile;
    outputFile.open("Users.txt");

    cout << "Enter Username: ";
    cin >> userName;
    cout << "Enter Password: ";
    cin >> passwd;
    cout << "Re-enter Password: ";
    cin >> confirmPasswd;

    if(passwd != confirmPasswd){
        cout << "passwords don't match, please try again" ;
        registrationpPage();
    }

    outputFile << userName << ": " << passwd << endl;
    outputFile.close();
}

int main() {
    cout << "Welcome to the Bank Management App";
    char quit;

    

    while(quit != 'q') {
        cout << "Options from 1 - 10";
        cout << "1 - Open an account";
        cout << "2 - Close an account";
        cout << "3 - Deposit Money";
        cout << "4 - Withdraw Money";
        cout << "5 - Open an account";
    }
}