#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>

std::vector<std::string> split(const std::string &str, char sep);
std::string GetToday();

int main(int argc, char *argv[]){
   std::string OUTPUTFILE = "./example.txt";
   int FILENUMBER = -1;
   if(argc==2) {
      OUTPUTFILE = argv[1];
   } else if(argc==3) {
      OUTPUTFILE = argv[1];
      FILENUMBER = std::stoi(argv[2]);
   } else {
      std::cout << "Usage : example.exe [OUTPUTFILE] " << std::endl;
      std::cout << "Usage : example.exe [OUTPUTFILE] [FILENUMBER]" << std::endl;
      return -1;
   }

   std::string fileName = OUTPUTFILE;
   if(FILENUMBER>=0) {
      std::ostringstream sout;
      sout << split(fileName, '.')[0];
      sout << std::setfill('0') << std::setw(6) << FILENUMBER << '.';
      sout << split(fileName, '.')[1];
      fileName = sout.str();
   }
   std::ofstream fout;
   fout.open(fileName);
   if(!fout) return -1;

   fout << "Hello, world!" << std::endl;
   fout << "Today is " << GetToday() << std::endl;
   fout.close();

   return 0;
}

std::vector<std::string> split(const std::string &str, char sep)
{
   std::vector<std::string> v;
   auto first = str.begin();
   while( first != str.end() ) {
      auto last = first;
      while( last != str.end() && *last != sep )
         ++last;
      v.push_back(std::string(first, last));
      if( last != str.end() )
         ++last;
      first = last;
   }
   return v;
}

std::string GetToday(){
   time_t now = time(NULL);
   const tm *pnow = localtime(&now);
   std::ostringstream sout;
   sout << std::setfill('0') << std::setw(4) << pnow->tm_year+1900 << '-';
   sout << std::setfill('0') << std::setw(2) << pnow->tm_mon + 1 << '-';
   sout << std::setfill('0') << std::setw(2) << pnow->tm_mday;
   return sout.str();
}

