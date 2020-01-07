#include<iostream>
int main(){
    char salir;
    char palabra [10];
    int count;
    std::cout<<"dime tu nombre: ";
    std::cin>>palabra;
    std::cout<<"\n";
    std::cout<<"tu nombre es: ";
    std::cout<<palabra;
    std::cout<<"\n";
    for(count=0;count<=9;count++){
        std::cout<<palabra[count];
        std::cout<<"\n";
    }
    std::cin>>salir;
}
